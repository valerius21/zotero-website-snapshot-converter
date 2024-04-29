import os
from pathlib import Path
from typing import Dict, Optional, List, Any
from urllib.parse import urlparse

import httpx
from loguru import logger
from pyzotero import zotero as pyzot

from .attachment_response import attachment_response_from_dict
from .top_item_response import top_item_response_from_dict, TopItemResponseElement, AttachmentType

API_URL: str = "https://api.zotero.org"
LIBRARY_TYPE: str = 'users'
VERSION: str = '3'


class ZoteroClient:
    """Zotero client - a client for the Zotero API."""

    def __init__(self, api_key: Optional[str] = "", library_id: Optional[str] = ""):
        """Initialize the client. It will use the environment variables if the values are not provided."""
        self.ZOTERO_API_KEY = os.getenv('ZOTERO_API_KEY') or api_key
        self.LIBRARY_ID = os.getenv('ZOTERO_LIBRARY_ID') or library_id
        self.ZOTERO_API_VERSION = VERSION
        self.ZOTERO_LIBRARY_PREFIX = f"{LIBRARY_TYPE}/{self.LIBRARY_ID}"
        self.BASE_URL = f"{API_URL}/{self.ZOTERO_LIBRARY_PREFIX}"
        self.http_client = httpx.Client(headers=self.get_headers(), timeout=10, follow_redirects=True)
        self.pyzot = pyzot.Zotero(self.LIBRARY_ID, 'user', self.ZOTERO_API_KEY)

    def get_headers(self) -> Dict[str, str]:
        """Get the headers for the HTTP client."""
        return {
            'Zotero-API-Key': self.ZOTERO_API_KEY,
            'Zotero-API-Version': self.ZOTERO_API_VERSION
        }

    def get_top_items(self) -> List[TopItemResponseElement]:
        """Get the top items from the API."""
        url = f"{self.BASE_URL}/items/top"
        res = self.http_client.get(url, headers=self.get_headers())
        if res.status_code != 200:
            raise Exception(f"Failed to fetch top items: {res.text}")
        items = top_item_response_from_dict(res.json())
        return ZoteroClient.filter_for_attachment_items(items)

    def get_attachment_html(self, href: str) -> str:
        """Get the attachment HTML."""
        res = self.http_client.get(href, headers=self.get_headers())
        if res.status_code != 200:
            raise Exception(f"Failed to fetch attachment html: {res.text}")
        attachment_response = attachment_response_from_dict(res.json())
        snapshot_link = attachment_response.links.enclosure.href
        attachment_type = attachment_response.links.enclosure.type
        if attachment_type != 'text/html':
            raise Exception(f"Attachment is not a webpage: {attachment_type}")
        return self.get_snapshot_html(snapshot_link)

    def get_snapshot_html(self, snapshot_href: str) -> str:
        """Get the snapshot HTML."""
        res = self.http_client.get(snapshot_href, headers=self.get_headers())
        return res.text

    @staticmethod
    def filter_for_attachment_items(items: List[TopItemResponseElement]) -> List[TopItemResponseElement]:
        """Filter the items for the ones that have an attachment and are not already converted."""
        return [item for item in items if
                item.links.attachment is not None and
                '#converted' not in item.data.extra and
                item.links.attachment.attachment_type is AttachmentType.TEXT_HTML]

    def upload_pdf(self, item_key: str, pdf_path: Path) -> Dict[str, List]:
        """Upload the PDF to the item."""
        results = self.pyzot.attachment_simple([str(pdf_path)], item_key)
        if len(results['failure']) > 0:
            raise Exception(f"Failed to upload pdf: {results['failure']}")
        return results

    def add_extra_key_for_handled_conversion_in_zotero(self, item_key: str) -> Any:
        """Add an extra key to the item to mark it as converted."""
        item: Any = self.pyzot.item(item_key)
        item['data']['extra'] += ' #converted'
        return self.pyzot.update_item(item)

    def set_date_to_access_date(self, item_key: str) -> Any:
        """Set the date to the access date."""
        item: Any = self.pyzot.item(item_key)
        item['data']['date'] = item['data']['accessDate']
        return self.pyzot.update_item(item)

    def set_author_name_to_domain_name(self, item_key: str) -> Any:
        """Set the author name to the domain name."""
        item = self.pyzot.item(item_key)
        if len(item['data']['creators']) == 0:
            return self.update_to_url_author(item)

    def update_to_url_author(self, item: Any):
        """Update the author to the domain name."""
        new_author = ZoteroClient.get_domain(item['data']['url'])
        logger.info(f'Author is empty, setting to domain name: {new_author}')
        item['data']['creators'] = [{'creatorType': 'author',
                                     'firstName': '',
                                     'lastName': new_author}]
        return self.pyzot.update_item(item)

    @staticmethod
    def get_domain(url: str) -> str:
        """Get the domain from the URL. It will return the last two parts of the domain."""
        parsed_url = urlparse(url)
        domain_parts = parsed_url.netloc.split('.')
        if len(domain_parts) > 2:
            return '.'.join(domain_parts[-(len(domain_parts) - 1):])
        else:
            return parsed_url.netloc

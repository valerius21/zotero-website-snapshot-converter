import os
from typing import Dict, Optional, List
from .top_item_response import top_item_response_from_dict, TopItemResponseElement, AttachmentType, AlternateType
from .attachment_response import attachment_response_from_dict

import httpx

API_URL: str = "https://api.zotero.org"
LIBRARY_TYPE: str = 'users'
VERSION: str = '3'


class ZoteroClient:

    def __init__(self, api_key: Optional[str] = "", library_id: Optional[str] = ""):
        self.ZOTERO_API_KEY = os.getenv('ZOTERO_API_KEY') or api_key
        self.LIBRARY_ID = os.getenv('ZOTERO_LIBRARY_ID') or library_id
        self.ZOTERO_API_VERSION = VERSION
        self.ZOTERO_LIBRARY_PREFIX = f"{LIBRARY_TYPE}/{self.LIBRARY_ID}"
        self.BASE_URL = f"{API_URL}/{self.ZOTERO_LIBRARY_PREFIX}"

    def get_headers(self) -> Dict[str, str]:
        return {
            'Zotero-API-Key': self.ZOTERO_API_KEY,
            'Zotero-API-Version': self.ZOTERO_API_VERSION
        }

    def get_top_items(self) -> List[TopItemResponseElement]:
        url = f"{self.BASE_URL}/items/top"
        res = httpx.get(url, headers=self.get_headers())
        if res.status_code != 200:
            raise Exception(f"Failed to fetch top items: {res.text}")
        items = top_item_response_from_dict(res.json())
        return ZoteroClient.filter_for_attachment_items(items)

    def get_attachment_html(self, href: str) -> str:
        res = httpx.get(href, headers=self.get_headers())
        if res.status_code != 200:
            raise Exception(f"Failed to fetch attachment html: {res.text}")
        attachment_response = attachment_response_from_dict(res.json())
        snapshot_link = attachment_response.links.enclosure.href
        attachment_type = attachment_response.links.enclosure.type
        if attachment_type != 'text/html':
            raise Exception(f"Attachment is not a webpage: {attachment_type}")
        return self.get_snapshot_html(snapshot_link)

    def get_snapshot_html(self, snapshot_href: str) -> str:
        res = httpx.get(snapshot_href, headers=self.get_headers())
        if res.status_code != 200:
            raise Exception(f"Failed to fetch snapshot html: {res.text}")
        return res.text

    @staticmethod
    def filter_for_attachment_items(items: List[TopItemResponseElement]) -> List[TopItemResponseElement]:
        return [item for item in items if
                item.links.attachment is not None and
                item.links.attachment.attachment_type is AttachmentType.TEXT_HTML]

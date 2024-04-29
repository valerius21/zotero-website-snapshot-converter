import os
from typing import Dict, Optional

import httpx

API_URL: str = "https://api.zotero.org"
LIBRARY_TYPE: str = 'users'
VERSION: str = '3'


class ZoteroClient:

    def __init__(self, api_key: Optional[str] = "", library_id: Optional[str] = ""):
        self.ZOTERO_API_KEY = os.getenv('ZOTERO_API_KEY') or api_key
        self.LIBRARY_ID = os.getenv('LIBRARY_ID') or library_id
        self.ZOTERO_API_VERSION = VERSION
        self.ZOTERO_LIBRARY_PREFIX = f"{LIBRARY_TYPE}/{self.LIBRARY_ID}"
        self.BASE_URL = f"{API_URL}/{self.ZOTERO_LIBRARY_PREFIX}"

    def get_headers(self) -> Dict[str, str]:
        return {
            'Zotero-API-Key': self.ZOTERO_API_KEY,
            'Zotero-API-Version': self.ZOTERO_API_VERSION
        }

    def get_top_items(self):
        url = f"{self.BASE_URL}/items/top"
        res = httpx.get(url, headers=self.get_headers())
        return res.json()

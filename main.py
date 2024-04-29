from zotero.client import ZoteroClient

if __name__ == '__main__':
    zot = ZoteroClient()
    items = zot.get_top_items()
    print(items)

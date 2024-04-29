from zotero.client import ZoteroClient

if __name__ == '__main__':
    zot = ZoteroClient()
    items = zot.get_top_items()
    html = zot.get_attachment_html(items[0].links.attachment.href)
    print(html)

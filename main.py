from pdf_converter.create_pdf import create_pdf_from_html
from zotero.client import ZoteroClient

if __name__ == '__main__':
    zot = ZoteroClient()
    items = zot.get_top_items()
    html = zot.get_attachment_html(items[0].links.attachment.href)
    create_pdf_from_html(html, 'output.pdf')

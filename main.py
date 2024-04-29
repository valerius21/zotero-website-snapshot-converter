from pdf_converter.create_pdf import create_pdf_from_html
from zotero.client import ZoteroClient

mark_as_converted: bool = True
rename_date_from_access_date: bool = True

if __name__ == '__main__':
    zot = ZoteroClient()
    items = zot.get_top_items()
    for item in items:
        print(item.data.title)
        html = zot.get_attachment_html(item.links.attachment.href)
        path, title = create_pdf_from_html(html, f'snapshot-output-{item.key}.pdf')
        upload_results = zot.upload_pdf(item.key, path)
        if mark_as_converted:
            zot.add_extra_key_for_handled_conversion_in_zotero(item.key)
        if rename_date_from_access_date:
            zot.set_date_to_access_date(item.key)
        break

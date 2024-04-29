from pdf_converter.create_pdf import create_pdf_from_html
from zotero.client import ZoteroClient
from loguru import logger

mark_as_converted: bool = True
rename_date_from_access_date: bool = True
rename_empty_author_to_domain_name: bool = True


def main():
    """Main function."""
    zot = ZoteroClient()
    items = zot.get_top_items()
    process_items(items, zot)


def process_items(items, zot):
    """Process the items."""
    for item in items:
        logger.info(f'Processing "{item.data.title}"')
        html = zot.get_attachment_html(item.links.attachment.href)
        path, title = create_pdf_from_html(html, f'snapshot-output-{item.key}.pdf')
        upload_results = zot.upload_pdf(item.key, path)
        post_process_options(item, zot)
        logger.success(f'Processed "{item.data.title}"')
        break


def post_process_options(item, zot):
    """Apply post processing options to the item."""
    if mark_as_converted:
        logger.info(f'Marking item as converted for "{item.data.title}"')
        zot.add_extra_key_for_handled_conversion_in_zotero(item.key)
    if rename_date_from_access_date:
        logger.info(f'Setting date to access date for "{item.data.title}"')
        zot.set_date_to_access_date(item.key)
    if rename_empty_author_to_domain_name:
        logger.info(f'Setting author name to domain name for "{item.data.title}"')
        zot.set_author_name_to_domain_name(item.key)


if __name__ == '__main__':
    main()

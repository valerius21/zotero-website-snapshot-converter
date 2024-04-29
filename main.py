from loguru import logger
import streamlit as st

from pdf_converter.create_pdf import create_pdf_from_html
from zotero.client import ZoteroClient

mark_as_converted: bool = True
rename_date_from_access_date: bool = True
rename_empty_author_to_domain_name: bool = True


def process_items(items, zot):
    """Process the items."""
    for item in items:
        logger.info(f'Processing "{item.data.title}"')
        html = zot.get_attachment_html(item.links.attachment.href)
        path, title = create_pdf_from_html(html, f'snapshot-output-{item.key}.pdf')
        zot.upload_pdf(item.key, path)
        post_process_options(item, zot)
        logger.success(f'Processed "{item.data.title}"')
        ui_bar.progress((items.index(item) + 1) / len(items), text=f'Processed {item.data.title}')
        break


def post_process_options(item, zot):
    """Apply post-processing options to the item."""
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
    st.write('### Credentials')
    if 'zot' not in st.session_state:
        st.session_state.zot = None

    with st.form(key='credentials', border=False):
        api_key = st.text_input('Zotero API Key', type='password')
        user_id = st.text_input('Zotero User ID')
        submit_button = st.form_submit_button('Connect to Zotero')
    if not submit_button and not st.session_state.zot:
        st.stop()

    zot = ZoteroClient(api_key, user_id)
    st.session_state.zot = zot
    st.success('Connected to Zotero')

    with st.spinner('Fetching top-level items...'):
        items = zot.get_top_items()
        st.session_state['items'] = items
    st.success(f'Fetched top-level items with snapshots ({len(items)})')

    st.write('### Options')
    with st.form(key='options'):
        mark_as_converted = st.checkbox('Mark as converted', key='mark_as_converted')
        rename_date_from_access_date = st.checkbox('Rename date from access date', key='rename_date_from_access_date')
        rename_empty_author_to_domain_name = st.checkbox('Rename empty author to domain name',
                                                         key='rename_empty_author_to_domain_name')
        another_submit = st.form_submit_button('Process items')
    if not another_submit:
        st.stop()
    ui_bar = st.progress(0, text="Press the button above to start processing items")
    process_items(items, zot)

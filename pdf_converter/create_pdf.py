from playwright.sync_api import sync_playwright


def create_pdf_from_html(html: str, output_path: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_content(html)
        page.pdf(path=output_path)
        browser.close()

from pathlib import Path
from typing import Optional, Tuple

from playwright.sync_api import sync_playwright


def create_pdf_from_html(html: str, output_file_path: str, timeout: Optional[float] = 30.) -> Tuple[Path, str]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(html)
        # Wait for the page to load
        # See https://playwright.dev/dotnet/docs/api/class-page#page-wait-for-load-state
        page.wait_for_load_state('domcontentloaded', timeout=timeout)
        title = page.title()
        page.pdf(path=output_file_path)
        browser.close()
    return Path(output_file_path), title

from pathlib import Path
from typing import Optional, Tuple, Literal

from playwright.sync_api import sync_playwright

# See https://playwright.dev/dotnet/docs/api/class-page#page-wait-for-load-state
LOAD_STATE: Literal["domcontentloaded", "load", "networkidle"] | None = 'domcontentloaded'


def create_pdf_from_html(html: str, output_file_path: str, timeout: Optional[float] = 30.) -> Tuple[Path, str]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(html)
        page.wait_for_load_state(LOAD_STATE, timeout=timeout)
        title = page.title()
        page.pdf(path=output_file_path)
        browser.close()
    return Path(output_file_path), title

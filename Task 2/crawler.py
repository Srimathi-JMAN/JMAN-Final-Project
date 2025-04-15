from playwright.sync_api import sync_playwright

def scrape_all_text(start_url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(start_url, wait_until="networkidle")

        content = page.content()
        text = page.inner_text("body")
        browser.close()
        return text

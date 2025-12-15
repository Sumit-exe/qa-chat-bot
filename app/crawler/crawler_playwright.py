from playwright.sync_api import sync_playwright

def crawl_with_playwright(url: str):
    texts = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=30000)
        page.wait_for_load_state("networkidle")

        content = page.content()
        texts.append(content)

        browser.close()

    return texts
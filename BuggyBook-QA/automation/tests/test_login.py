from playwright.sync_api import sync_playwright

def test_homepage_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # use headless=True to run in background
        page = browser.new_page()
        page.goto("http://books.toscrape.com/")
        assert "Books to Scrape" in page.title()
        browser.close()

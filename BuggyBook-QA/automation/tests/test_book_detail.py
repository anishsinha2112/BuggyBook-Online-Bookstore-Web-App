from playwright.sync_api import sync_playwright

def test_book_detail_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://books.toscrape.com/")
        page.click("article.product_pod h3 a")  # Click first book
        assert "£" in page.text_content(".price_color")  # Check for price
        browser.close()

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()

try:
    page.goto("https://duckduckgo.com/", timeout=10000)
    page.wait_for_timeout(100)
    page.fill("#searchbox_input", "Playwright")
    page.wait_for_timeout(100)
    page.press("#searchbox_input", "Enter")
    page.wait_for_timeout(10000)
    if "Playwright at DuckDuckGo" in page.title():
        print("ОК")
    else:
        print("НЕ ОК")

except Exception as e:
    print(f"Ошибка {e}")

finally:
    browser.close()
    playwright.stop()
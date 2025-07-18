from playwright.sync_api import sync_playwright, expect

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()

try:
    # Открыть страницу в браузере
    page.goto("https://www.leafground.com", timeout=10000)
    page.wait_for_timeout(1000)

    # Кликнуть по кнопке Element в менюшке
    page.click("#menuform\:j_idt40")
    page.wait_for_timeout(1000)

    # Перейти по кнопке checkbox
    page.click("#menuform\:m_checkbox")
    page.wait_for_timeout(1000)

    # Нажать на поле "Select Multiple"
    page.click("#j_idt87\:multiple")
    page.wait_for_timeout(1000)

    # Получаем все значения
    text_content = page.locator("#j_idt87\:multiple").text_content()
    page.wait_for_timeout(1000)

    # Проверка текста London
    locator = page.locator("#j_idt87\:multiple")
    expect(locator).to_contain_text("London")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    browser.close()
    playwright.stop()



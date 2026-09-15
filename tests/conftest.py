import pytest
from playwright.sync_api import sync_playwright, Page

# 1. Фикстура за споделяне на базовата конфигурация (например URL адреса)
@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://practicesoftwaretesting.com"

# 2. Фикстура, която управлява жизнения цикъл на браузъра (оптимизирана за Chromium)
@pytest.fixture(scope="function")
def page() -> Page:
    # Стартираме Playwright
    with sync_playwright() as p:
        # Стартираме само Chromium в headed режим (с видим прозорец) за Windows локална среда
        # Можете да промените headless=True, ако искате тестът да върви на заден план
        browser = p.chromium.launch(headless=False)
        
        # Създаваме чист контекст (нова сесия на браузъра)
        context = browser.new_context()
        
        # Отваряме нова страница
        page = context.new_page()
        
        # Предоставяме страницата на теста
        yield page
        
        # След като тестът приключи, почистваме (Teardown)
        page.close()
        context.close()
        browser.close()

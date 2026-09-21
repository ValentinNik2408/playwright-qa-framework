from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    
    # Act
    login_page.navigate()
    login_page.login("admin@practicesoftwaretesting.com", "welcome01")
    
    # Assert
    expect(page).to_have_url("https://practicesoftwaretesting.com/admin/dashboard")
    page.wait_for_timeout(2500)
    
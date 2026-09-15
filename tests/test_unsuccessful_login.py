from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    
    # Act
    login_page.navigate()
    login_page.login("invalid@gmail.com", "Ribame4?")
    
    # Assert
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Invalid email or password")
    page.wait_for_timeout(1500)
    
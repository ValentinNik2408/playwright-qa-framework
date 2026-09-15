from pages.home_page import HomePage
from pages.login_page import LoginPage

from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("testing111@gmail.com", "Ribame4?")
    
    expect(page).to_have_url("https://practicesoftwaretesting.com/account")
    page.wait_for_timeout(500)

    #Act
    home_page = HomePage(page)
    home_page.home_button.click()

    expect(page).to_have_url("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(500)
    expect(home_page.main_image).to_be_visible()
    expect(home_page.web_page_logo).to_be_visible()
    
    
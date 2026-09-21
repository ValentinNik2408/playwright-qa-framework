from pages.home_page import HomePage
from pages.login_page import LoginPage

from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("admin@practicesoftwaretesting.com", "welcome01")
    
    expect(page).to_have_url("https://practicesoftwaretesting.com/admin/dashboard")
    page.wait_for_timeout(500)

    #Act
    home_page = HomePage(page)
    home_page.home_button.click()

    #Assert
    expect(page).to_have_url("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(500)
    expect(home_page.main_image).to_be_visible()
    expect(home_page.web_page_logo).to_be_visible()

    #Set
    sorting_dropdown = page.locator(".form-select")
    first_element = page.locator("a:nth-child(1) div:nth-child(2) h5:nth-child(1)")
    second_element = page.locator("a:nth-child(2) div:nth-child(2) h5:nth-child(1)")
    search_bar = page.locator(".form-control")
    search_button = page.locator("button[type=submit]")

    #Act
    sorting_dropdown.select_option("Price (High - Low)")
    page.wait_for_timeout(500)
    search_bar.fill("drill")
    search_button.click()

    #Assert
    expect(first_element).to_have_text(" Cordless Drill 20V ")
    page.wait_for_timeout(500)
    if second_element.all_inner_texts() != " Cordless Drill 18V ":
        raise AssertionError ("Sorting is wrong")
    # expect(second_element).to_have_text(" Cordless Drill 18V ")
    page.wait_for_timeout(500)
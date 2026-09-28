from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

from playwright.sync_api import Page, expect

def test_checkout_flow(page: Page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    checkout_page = CheckoutPage()

    #Login page
    login_page.navigate()
    login_page.login("admin@practicesoftwaretesting.com", "welcome01")
    expect(page).to_have_url("https://practicesoftwaretesting.com/admin/dashboard")

    #Home page
    home_page.home_button.click()
    expect(page).to_have_url("https://practicesoftwaretesting.com/")

    #Adding first element to cart
    button_add_to_cart = page.locator("#btn-add-to-cart")
    page.get_by_text(" Combination Pliers ").click()
    button_add_to_cart.click()
    cart_count = page.locator("#lblCartCount")
    expect(cart_count).to_have_text("1")

    #Adding second element to cart
    home_page.home_button.click()
    page.get_by_role("heading", name="Pliers", exact=True).click()
    button_add_to_cart.click()
    cart_count = page.locator("#lblCartCount")
    expect(cart_count).to_have_text("2")

    #Checkout page
    checkout_button = page.locator('.nav-link[aria-label="cart"]')
    checkout_button.click()
    expect(page).to_have_url("https://practicesoftwaretesting.com/checkout")

    #Checking if correct items are added to cart
    checkout_page.correct_items_added(page, "Combination Pliers", "Pliers")
    #Checking if the calculation is correct for the added items in cart
    checkout_page.calculate_total_price(page, 26.16)
    page.locator(".btn[data-test='proceed-1']").click()

    expect(page.get_by_text("Hello John Doe, you are already logged in. You can proceed to checkout.")).to_be_visible()
    page.locator(".btn[data-test='proceed-2']").click()

    page.locator("#country").select_option("Bulgaria")
    page.locator("#postal_code").fill("1000")
    page.locator("#house_number").fill("15")
    page.locator("#street").fill("Tsarigradsko Shose")
    page.locator("#city").fill("Sofia")
    page.locator("#city").fill("Sofia")
    page.locator("#state").fill("Sofia")
    page.locator(".btn[data-test='proceed-3']").click()
    page.locator("#payment-method").select_option("cash-on-delivery")
    page.locator(".btn[data-test='finish']").click()
    
    expect(page.locator(".help-block")).to_be_visible()
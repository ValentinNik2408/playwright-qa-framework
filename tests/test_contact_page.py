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

    page.locator(".nav-link[data-test='nav-contact']").click()
    expect(page).to_have_url("https://practicesoftwaretesting.com/contact")

    # Act
    page.locator("#subject").select_option("status-of-order")
    message_input_box = page.locator("#message")
    message_input_box.fill("What is the status of my order?")
    page.wait_for_timeout(2500)
    submit_button = page.locator(".btnSubmit")
    submit_button.click()

    # Assert
    alert_message = page.locator("#message_alert")
    expect(alert_message).to_have_text("Message must be minimal 50 characters")
    page.wait_for_timeout(2500)

    # Act
    message_input_box.fill("Hello, I'm writing about the status of my order. Can you please provide the status of the order? Thanks in advance. Best regards, Admin User")
    page.wait_for_timeout(500) 
    submit_button.click()   #After first press no message appears
    page.wait_for_timeout(500)
    submit_button.click()   #After second press message appears

    # Assert
    successful_message = page.get_by_role("alert")
    expect(successful_message).to_have_text(" Thanks for your message! We will contact you shortly. ")
    page.wait_for_timeout(500)
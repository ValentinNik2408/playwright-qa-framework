from playwright.sync_api import Page, expect

def billing_adress(page:Page):
    page.locator("#country").select_option("Bulgaria")
    page.locator("#postal_code").fill("1000")
    page.locator("#house_number").fill("15")
    page.wait_for_timeout(500)
    page.locator("#street").fill("Tsarigradsko Shose")
    page.locator("#city").fill("Sofia")
    page.locator("#state").fill("Sofia")
    page.wait_for_timeout(1000)
    page.locator(".btn[data-test='proceed-3']").click()

def cash_on_delivery_option(page:Page):
    page.locator("#payment-method").select_option("cash-on-delivery")
    page.locator(".btn[data-test='finish']").click()
    page.wait_for_timeout(500)
    expect(page.locator(".help-block", has_text='Payment was successful')).to_be_visible()

def bank_transfer_option(page: Page):
    page.locator("#payment-method").select_option("bank-transfer")

    #Bank Name field
    expect(page.locator("#bank_name")).to_be_visible()
    page.locator("#bank_name").fill("Bank1")
    expect(page.locator(".alert", has_text="Bank name can only contain letters and spaces.")).to_be_visible()
    page.locator("#bank_name").fill("Bank One")
    expect(page.locator(".alert", has_text="Bank name can only contain letters and spaces.")).not_to_be_visible()

    #Account Name field
    expect(page.locator("#account_name")).to_be_visible()
    page.locator("#account_name").click()
    page.locator("#bank_name").click()
    expect(page.locator(".alert", has_text='Account name can contain letters, numbers, spaces, periods, apostrophes, and hyphens.')).to_be_visible()
    page.wait_for_timeout(500)
    page.locator("#account_name").fill("User1")
    expect(page.locator(".alert", has_text='Account name can contain letters, numbers, spaces, periods, apostrophes, and hyphens.')).not_to_be_visible()

    #Account Number field
    expect(page.locator("#account_number")).to_be_visible()
    page.locator("#account_number").fill("account number 123")
    expect(page.locator(".alert", has_text='Account number must be numeric.')).to_be_visible()
    page.wait_for_timeout(500)
    page.locator("#account_number").fill("123")
    expect(page.locator(".alert", has_text='Account number must be numeric.')).not_to_be_visible()
    
    page.locator(".btn[data-test='finish']").click()
    expect(page.locator(".help-block", has_text='Payment was successful')).to_be_visible()
    page.wait_for_timeout(500)

def credit_card_option(page:Page):
    page.locator("#payment-method").select_option("credit-card")
    
    #Credit Card Number field
    page.locator("#credit_card_number").fill("0")
    page.wait_for_timeout(500)
    expect(page.locator(".alert", has_text="Invalid card number format.")).to_be_visible()
    page.locator("#credit_card_number").fill("0000 1234 5678 0000")
    page.wait_for_timeout(500)
    expect(page.locator(".alert", has_text="Invalid card number format.")).to_be_visible()
    page.locator("#credit_card_number").fill("0000-1234-5678-0000")
    page.wait_for_timeout(500)
    expect(page.locator(".alert", has_text="Invalid card number format.")).not_to_be_visible()

    #Expiration date field
    page.locator("#expiration_date").fill("1")
    page.wait_for_timeout(500)
    expect(page.locator(".alert", has_text="Invalid date format. Use MM/YYYY.")).to_be_visible()
    page.locator("#expiration_date").fill("01/2026")
    page.wait_for_timeout(500)
    expect(page.locator(".alert", has_text="Expiration date must be in the future.")).to_be_visible()
    page.locator("#expiration_date").fill("10/2056")
    page.wait_for_timeout(500)
    expect(page.locator(".alert", has_text="Expiration date must be in the future.")).not_to_be_visible()
    expect(page.locator(".alert", has_text="Invalid date format. Use MM/YYYY.")).not_to_be_visible()

    # CVV field
    page.locator("#cvv").fill("abc123")
    page.wait_for_timeout(500)
    expect(page.locator(".alert", has_text="CVV must be 3 or 4 digits.")).to_be_visible()
    page.locator("#cvv").fill("12")
    page.wait_for_timeout(500)
    expect(page.locator(".alert", has_text="CVV must be 3 or 4 digits.")).to_be_visible()
    page.locator("#cvv").fill("123")
    page.wait_for_timeout(500)
    expect(page.locator(".alert", has_text="CVV must be 3 or 4 digits.")).not_to_be_visible()

    # Card Holder Name field
    page.locator("#card_holder_name").fill("123")
    page.wait_for_timeout(500)
    #expect(page.locator(".alert", has_text="Card Holder Name can only contain letters and spaces.")).to_be_visible()

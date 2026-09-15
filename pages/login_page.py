class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.login_button = page.locator(".btnSubmit")

    def navigate(self):
        self.page.goto("https://practicesoftwaretesting.com/auth/login")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

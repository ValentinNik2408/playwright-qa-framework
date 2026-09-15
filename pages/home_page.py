class HomePage:
    def __init__(self, page):
        self.page = page
        self.home_button = page.locator(".nav-link.active")
        self.main_image = page.locator(".img-fluid")
        self.web_page_logo = page.locator("#Layer_1")
        self.items = page.locator(".card-img-top")
        
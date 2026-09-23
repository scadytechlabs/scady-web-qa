from playwright.sync_api import Page, expect
from config.settings import BASE_URL


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("[data-test='username']")
        self.password = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def verify_login_successful(self):
        expect(self.page).to_have_url(f"{BASE_URL}inventory.html")

    def verify_error_contains(self, message: str):
        expect(self.error_message).to_contain_text(message)
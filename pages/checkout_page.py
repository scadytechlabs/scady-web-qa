from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.error_message = page.locator("[data-test='error']")
        self.complete_header = page.locator(
            "[data-test='complete-header']"
        )

    def enter_customer_details(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()

    def continue_without_details(self):
        self.continue_button.click()

    def verify_error_contains(self, message: str):
        expect(self.error_message).to_contain_text(message)

    def finish_order(self):
        self.finish_button.click()

    def verify_order_success(self):
        expect(self.complete_header).to_have_text(
            "Thank you for your order!"
        )
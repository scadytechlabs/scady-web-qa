from playwright.sync_api import Page, expect


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("[data-test='checkout']")

    def verify_product_in_cart(self, product_name: str):
        expect(
            self.page.locator(".inventory_item_name")
        ).to_have_text(product_name)

    def proceed_to_checkout(self):
        self.checkout_button.click()
from playwright.sync_api import Page, expect


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator(
            "[data-test='checkout']"
        )

    def verify_product_in_cart(self, product_name: str):
        product = self.page.locator(
            ".cart_item .inventory_item_name",
            has_text=product_name,
        )

        expect(product).to_be_visible()
        expect(product).to_have_text(product_name)

    def proceed_to_checkout(self):
        self.checkout_button.click()
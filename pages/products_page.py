from playwright.sync_api import Page, expect


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator(".title")
        self.cart_link = page.locator(".shopping_cart_link")

    def verify_products_page(self):
        expect(self.page_title).to_have_text("Products")

    def add_product_to_cart(self, product_name: str):
        product_id = product_name.lower().replace(" ", "-")
        self.page.locator(
            f"[data-test='add-to-cart-{product_id}']"
        ).click()

    def open_cart(self):
        self.cart_link.click()
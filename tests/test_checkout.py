from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from config.settings import STANDARD_USER, PASSWORD


def test_customer_can_complete_purchase(page):

    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Login
    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    # Products
    products_page.verify_products_page()
    products_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    # Cart
    products_page.open_cart()
    cart_page.verify_product_in_cart(
        "Sauce Labs Backpack"
    )

    # Checkout
    cart_page.proceed_to_checkout()

    checkout_page.enter_customer_details(
        "Scady",
        "TechLabs",
        "600001",
    )

    checkout_page.finish_order()
    checkout_page.verify_order_success()
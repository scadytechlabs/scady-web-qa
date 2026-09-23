import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from config.settings import STANDARD_USER, PASSWORD


@pytest.mark.regression
def test_customer_can_remove_product_from_cart(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # Login
    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    # Add product
    products_page.verify_products_page()
    products_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    # Open cart
    products_page.open_cart()

    cart_page.verify_product_in_cart(
        "Sauce Labs Backpack"
    )

    # Remove product
    cart_page.remove_product(
        "Sauce Labs Backpack"
    )

    # Verify removal
    cart_page.verify_product_not_in_cart(
        "Sauce Labs Backpack"
    )
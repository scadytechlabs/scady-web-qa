import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.settings import STANDARD_USER, PASSWORD


@pytest.mark.regression
@pytest.mark.negative
def test_checkout_requires_first_name(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    products_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )
    products_page.open_cart()

    cart_page.proceed_to_checkout()

    checkout_page.continue_without_details()

    checkout_page.verify_error_contains(
        "First Name is required"
    )
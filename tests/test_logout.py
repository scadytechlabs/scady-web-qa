import pytest

from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from config.settings import STANDARD_USER, PASSWORD


@pytest.mark.smoke
@pytest.mark.regression
def test_user_can_logout(page):
    login_page = LoginPage(page)
    menu_page = MenuPage(page)

    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)
    login_page.verify_login_successful()

    menu_page.logout()

    login_page.verify_login_page()
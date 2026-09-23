import pytest

from pages.login_page import LoginPage
from config.settings import STANDARD_USER, PASSWORD
from data.login_data import INVALID_LOGIN_DATA


@pytest.mark.smoke
@pytest.mark.regression
def test_standard_user_can_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)
    login_page.verify_login_successful()


@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.parametrize(
    "username,password,expected_error",
    INVALID_LOGIN_DATA,
)
def test_invalid_login_scenarios(
    page,
    username,
    password,
    expected_error,
):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)
    login_page.verify_error_contains(expected_error)
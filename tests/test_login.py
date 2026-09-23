import pytest

from pages.login_page import LoginPage
from config.settings import STANDARD_USER, PASSWORD


def test_standard_user_can_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)
    login_page.verify_login_successful()


@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        (
            "invalid_user",
            PASSWORD,
            "Username and password do not match",
        ),
        (
            STANDARD_USER,
            "wrong_password",
            "Username and password do not match",
        ),
        (
            "",
            PASSWORD,
            "Username is required",
        ),
        (
            STANDARD_USER,
            "",
            "Password is required",
        ),
    ],
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
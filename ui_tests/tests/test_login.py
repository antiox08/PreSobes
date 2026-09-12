import os

import allure
import pytest

from ui_tests.pages.home_page import HomePage
from ui_tests.pages.login_page import LoginPage


@pytest.mark.ui
@allure.feature("login")
@pytest.mark.xfail(
    reason="Внешний GitHub login нестабилен (DOM/2FA/сеть)",
    strict=False,
)
@pytest.mark.parametrize(
    "user, password",
    [
        (os.getenv("GH_USER"), os.getenv("GH_PASS")),
        (os.getenv("GH_USER2"), os.getenv("GH_PASS2")),
    ],
)
def test_positive_login(page, user: str, password: str) -> None:
    if not user or not password:
        pytest.skip("No credentials")

    with allure.step("Open login page"):
        login = LoginPage(page)
        login.open()
    with allure.step(f"Login as {user}"):
        login.login(user, password)
    with allure.step("Verify avatar is visible"):
        login.avatar_should_be_visible()

    with allure.step("check login in url"):
        assert "github.com/login" not in login.get_current_url()

    home = HomePage(page)
    assert home.dashboard_button_is_visible()


@pytest.mark.ui
@allure.feature("login")
@pytest.mark.xfail(
    reason="GitHub: Sign in находит 2 кнопки (strict mode) / внешний UI",
    strict=False,
)
def test_negative_login(page):
    user = os.getenv("GH_USER")
    password = os.getenv("GH_PASS_FAKE")

    if not user or not password:
        pytest.skip("No credentials")

    with allure.step("Open the page"):
        login = LoginPage(page)
        login.open()

    with allure.step(f"Invalid login as {user}"):
        login.login(user, password)

    with allure.step("error is visible"):
        login.expect_login_error()

import os
import pytest
from PreSobes.ui_tests.pages.login_page import LoginPage

@pytest.mark.ui
def test_positive_login(page):
    user = os.getenv('GH_USER')
    password = os.getenv('GH_PASS')

    if not user or not password:
        pytest.skip('No credentials')

    login = LoginPage(page)
    login.open()
    login.login(user, password)
    login.avatar_should_be_visible()

@pytest.mark.ui
def test_negative_login(page):
    user = os.getenv('GH_USER')
    password = os.getenv('GH_PASS_FAKE')

    if not user or not password:
        pytest.skip('No credentials')

    login = LoginPage(page)
    login.open()
    login.login(user, password)
    login.expect_login_error()

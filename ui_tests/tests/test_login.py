import os
import pytest
from PreSobes.ui_tests.pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.parametrize('user, password', [
    (os.getenv('GH_USER'), os.getenv('GH_PASS')),
    (os.getenv('GH_USER2'), os.getenv('GH_PASS2')),
])
def test_positive_login(page, user, password):
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

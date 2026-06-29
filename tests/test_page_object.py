from pages.LoginPage import LoginPage


def test_login_success():

    page = LoginPage(None)

    page.open()

    result = page.login('Anton', '123')

    assert result == "Anton logged in"

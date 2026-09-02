from pages.LoginPage import LoginPage


def test_login_success() -> None:

    page = LoginPage(None)

    page.open()

    result = page.login("Anton", "123")

    assert result == "Anton logged in"

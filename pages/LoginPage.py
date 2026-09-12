from pages.BasePage import BasePage


class LoginPage(BasePage):

    def open(self) -> None:
        print("Открываем страницу логина")

    def login(self, username: str, password: str) -> str:
        return f"{username} logged in"

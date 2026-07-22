from pages.BasePage import BasePage


class LoginPage(BasePage):

    def open(self):
        print("Открываем страницу логина")

    def login(self, username, password):
        return f"{username} logged in"

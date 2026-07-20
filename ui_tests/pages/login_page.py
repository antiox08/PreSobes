from playwright.sync_api import Page
from playwright.sync_api import expect


class LoginPage:

    URL = "https://github.com/login"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def get_current_url(self) -> str:
        return self.page.url

    def login(self, username, password):

        self.page.locator("#login_field").fill(username)
        self.page.locator("#password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()

    def avatar_should_be_visible(self):
        expect(self.page.get_by_test_id('github-avatar')).to_be_visible()

    def expect_login_error(self):
        expect(self.page.locator("#js-flash-alert")).to_be_visible()

from playwright.sync_api import Page


class HomePage:

    URL = "https://github.com/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def go_to_solutions(self):
        """Кликаем по Solutions в верхнем меню"""
        self.page.get_by_role("button", name="Solutions").click()

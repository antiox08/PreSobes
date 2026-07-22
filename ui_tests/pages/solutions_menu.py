from playwright.sync_api import Page


class SolutionsMenu:

    def __init__(self, page: Page):
        self.page = page

    def select_cicd(self):
        """Клик по CI/CD в выпадающем меню"""
        self.page.get_by_role("link", name="CI/CD").click()

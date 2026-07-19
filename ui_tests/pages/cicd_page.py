from playwright.sync_api import Page


class CiCdPage:

    def __init__(self, page: Page):
        self.page = page

    def click_contact_sales(self):
        """Кликаем по Contact sales"""
        self.page.get_by_test_id("Hero-grid") \
            .get_by_role("link", name="Contact sales") \
            .click()

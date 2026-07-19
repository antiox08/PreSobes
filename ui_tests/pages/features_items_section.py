from playwright.sync_api import Page


class FeaturesItemsSection:
    URL = 'https://automationexercise.com/'

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> None:
        self.page.goto(self.URL)

    def get_features_items_section(self):
        """Возвращает секцию 'Features Items'"""
        return self.page.locator('.features_items').filter(has=self.page.get_by_text("Features Items"))

    def get_visible_product_names(self):
        section = self.get_features_items_section()
        return section.locator('.productinfo p').all_inner_texts()

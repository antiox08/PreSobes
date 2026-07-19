from playwright.sync_api import Page


class DuckDuckGo:
    URL = 'https://duckduckgo.com'
    SEARCH_INPUT = '#searchbox_input'
    RESULT = '[data-testid="result"]'

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> None:
        self.page.goto(self.URL)

    def input_searchbox(self, query: str):
        searchbox = self.page.locator(self.SEARCH_INPUT)
        searchbox.fill(query)
        searchbox.press("Enter")

    def get_result(self):
        return self.page.locator(self.RESULT)

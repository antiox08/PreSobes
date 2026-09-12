import pytest
import allure
from playwright.sync_api import Page, expect

from ui_tests.pages.duck_duck_go_page import DuckDuckGo


@pytest.mark.parametrize("query", ["qa", "aqa", "python"])
def test_search_return_result(page: Page, query: str) -> None:
    with allure.step(f"Open DuckDuckGo"):
        duck = DuckDuckGo(page)
        duck.open()

    with allure.step(f"Search for query: {query}"):
        duck.input_searchbox(query)

    with allure.step(f'Проверить результаты для query: {query}'):
        result = duck.get_result()
        expect(result.first).to_be_visible()
        expect(result.nth(4)).to_be_visible()

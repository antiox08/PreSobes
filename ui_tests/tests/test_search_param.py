import pytest
from playwright.sync_api import Page, expect
from PreSobes.ui_tests.pages.duck_duck_go_page import DuckDuckGo


@pytest.mark.parametrize('query', ["qa", "aqa", "python"])
def test_search_return_result(page: Page, query: str) -> None:
    duck = DuckDuckGo(page)
    duck.open()
    duck.input_searchbox(query)

    result = duck.get_result()
    expect(result.first).to_be_visible()
    expect(result.nth(4)).to_be_visible()

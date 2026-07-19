import pytest
from playwright.sync_api import Page
from PreSobes.ui_tests.pages.features_items_section import FeaturesItemsSection


@pytest.mark.ui
def test_features_items_contains_expected_products(page: Page) -> None:
    home = FeaturesItemsSection(page)
    home.open()

    actual = home.get_visible_product_names()
    expected = ["Blue Top", "Men Tshirt", "Stylish Dress"]

    assert set(expected).issubset(set(actual))

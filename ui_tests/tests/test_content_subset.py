import pytest
import allure
from playwright.sync_api import Page, expect
from ui_tests.pages.features_items_section import FeaturesItemsSection


@pytest.mark.ui
def test_features_items_contains_expected_products(page: Page) -> None:
    with allure.step(f"Open products page"):
        home = FeaturesItemsSection(page)
        home.open()

    with allure.step(f'Проверить видимость секции категорий'):
        expect(home.get_features_items_section()).to_be_visible()

    expected = ["Blue Top", "Men Tshirt", "Stylish Dress"]
    with allure.step(f'Сравнить продукты: expected={expected}'):
        actual = home.get_visible_product_names()
        assert set(expected).issubset(set(actual))

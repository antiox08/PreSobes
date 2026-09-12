import allure

from ui_tests.contact_sales_data import contact_sales_data
from ui_tests.pages.cicd_page import CiCdPage
from ui_tests.pages.home_page import HomePage
from ui_tests.pages.solutions_menu import SolutionsMenu
from ui_tests.pages.сontact_sales_page import ContactSalesPage


def test_contact_sales_form_is_filled(page):
    with allure.step("Open GitHub homepage"):
        home = HomePage(page)
        home.open()

    with allure.step("Open solutions page"):
        home.go_to_solutions()

    with allure.step("Click cicd link"):
        solutions_menu = SolutionsMenu(page)
        solutions_menu.select_cicd()

    with allure.step("Open contact sales page"):
        cicd = CiCdPage(page)
        cicd.click_contact_sales()

    with allure.step("Fill form contact sales page"):
        sales = ContactSalesPage(page)
        sales.fill_form(contact_sales_data)

    with allure.step(f"Сравнить заполненные поля: expected={contact_sales_data}"):
        assert sales.get_field_values() == contact_sales_data

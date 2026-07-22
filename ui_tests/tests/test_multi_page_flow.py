from ui_tests.pages.home_page import HomePage
from ui_tests.pages.solutions_menu import SolutionsMenu
from ui_tests.pages.cicd_page import CiCdPage
from ui_tests.pages.сontact_sales_page import ContactSalesPage
from ui_tests.contact_sales_data import contact_sales_data


def test_contact_sales_form_is_filled(page):
    home = HomePage(page)
    home.open()
    home.go_to_solutions()

    solutions_menu = SolutionsMenu(page)
    solutions_menu.select_cicd()

    cicd = CiCdPage(page)
    cicd.click_contact_sales()

    sales = ContactSalesPage(page)
    sales.fill_form(contact_sales_data)

    assert sales.get_field_values() == contact_sales_data

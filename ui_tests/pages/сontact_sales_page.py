from playwright.sync_api import Page


class ContactSalesPage:

    FIRST_NAME = "#form-field-first_name"
    LAST_NAME = "#form-field-last_name"
    COMPANY = "#form-field-company"
    JOB_TITLE = '[name="job_title"]'
    EMAIL = '[name="email"]'

    def __init__(self, page: Page):
        self.page = page

    def fill_form(self, data):
        """Заполняем поля"""
        self.page.locator(self.FIRST_NAME).click()
        self.page.locator(self.FIRST_NAME).fill(data["first_name"])
        self.page.locator(self.LAST_NAME).fill(data["last_name"])
        self.page.locator(self.COMPANY).fill(data["company"])
        self.page.locator(self.JOB_TITLE).fill(data["job_title"])
        self.page.locator(self.EMAIL).fill(data["email"])

    def get_field_values(self):
        """Проверяем поля"""
        return {
            "first_name": self.page.locator(self.FIRST_NAME).input_value(),
            "last_name": self.page.locator(self.LAST_NAME).input_value(),
            "company": self.page.locator(self.COMPANY).input_value(),
            "job_title": self.page.locator(self.JOB_TITLE).input_value(),
            "email": self.page.locator(self.EMAIL).input_value(),
        }

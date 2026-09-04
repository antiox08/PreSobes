from pathlib import Path

import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

# Credentials for UI login tests (os.getenv in parametrize runs at collection time).
load_dotenv(Path(__file__).resolve().parent / ".env")

pytest_plugins = ["pytest_playwright"]


class AllureReporter:
    """Класс-репортер. Связь с Неделей 2: инкапсуляция логики в класс."""

    @staticmethod
    def attach_ui(page: Page, test_name: str) -> None:
        screenshot = page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name=f"screenshot_{test_name}",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            page.content(),
            name="page_html",
            attachment_type=allure.attachment_type.HTML,
        )

    @staticmethod
    def attach_api(item: pytest.Item) -> None:
        response = getattr(item, "last_response", None)
        if response is None:
            return

        allure.attach(
            response.text,
            name="response body",
            attachment_type=allure.attachment_type.TEXT,
        )

    @pytest.hookimpl(hookwrapper=True, tryfirst=True)
    def pytest_runtest_makereport(self, item: pytest.Item, call: pytest.CallInfo) -> None:
        """Хук после каждого этапа теста: attachments при падении."""
        outcome = yield
        report = outcome.get_result()

        if report.when != "call" or not report.failed:
            return

        page = item.funcargs.get("page")
        if page is not None:
            self.attach_ui(page, item.name)

        if item.get_closest_marker("api") is not None:
            self.attach_api(item)


def pytest_configure(config: pytest.Config) -> None:
    config.pluginmanager.register(AllureReporter(), "allure_reporter")

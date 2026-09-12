import allure
import pytest


@allure.feature("demo")
@pytest.mark.xfail(reason="Учебный демо-флак для Allure Flaky category", strict=False)
def test_flaky_demo_for_allure_report() -> None:
    """Учебный тест для категории Flaky tests в Allure."""
    with allure.step("Demo flaky failure"):
        pytest.fail("flaky: demo test for Allure Flaky category")

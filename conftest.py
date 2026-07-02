import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_google(driver):
    driver.get("https://google.com")
    assert "Google" in driver.title

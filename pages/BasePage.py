from typing import Any


class BasePage:

    def __init__(self, driver: Any) -> None:
        self.driver = driver

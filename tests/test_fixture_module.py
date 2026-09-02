from typing import Generator

import pytest


@pytest.fixture(scope="module")
def counter() -> Generator[int, None, None]:
    print("Создаем счетчик")
    yield 0


def test_one(counter: int) -> None:
    pass


def test_two(counter: int) -> None:
    pass


def test_three(counter: int) -> None:
    pass

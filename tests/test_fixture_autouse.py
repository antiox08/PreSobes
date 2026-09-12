from typing import Generator

import pytest

db: list[str] = []


@pytest.fixture(autouse=True)
def db_fixture() -> Generator[None, None, None]:
    db.clear()
    yield
    db.clear()


def test_add_user() -> None:
    db.append("user")
    assert len(db) == 1


def test_add_admin() -> None:
    db.append("admin")
    assert len(db) == 1

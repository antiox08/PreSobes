import pytest

db = []


@pytest.fixture(autouse=True)
def db_fixture():
    db.clear()
    yield
    db.clear()


def test_add_user():
    db.append("user")
    assert len(db) == 1


def test_add_admin():
    db.append("admin")
    assert len(db) == 1

import pytest
from requests import Session


@pytest.fixture
def session():
    with Session() as http_session:
        yield http_session

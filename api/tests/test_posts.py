import pytest
from api.client import get_post


@pytest.mark.api
def test_get_post_has_required_fields(session):
    post = get_post(session, 1)

    for field in ("id", "userId", "title", "body"):
        assert field in post

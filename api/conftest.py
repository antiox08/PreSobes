import pytest
from requests import Session


@pytest.fixture
def session(request: pytest.FixtureRequest):
    with Session() as http_session:
        original_get = http_session.get
        original_post = http_session.post
        original_delete = http_session.delete

        def get(url, **kwargs):
            response = original_get(url, **kwargs)
            request.node.last_response = response
            return response

        def post(url, **kwargs):
            response = original_post(url, **kwargs)
            request.node.last_response = response
            return response

        def delete(url, **kwargs):
            response = original_delete(url, **kwargs)
            request.node.last_response = response
            return response

        http_session.get = get
        http_session.post = post
        http_session.delete = delete

        yield http_session

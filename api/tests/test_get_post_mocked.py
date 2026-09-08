import pytest
import responses
from pydantic import BaseModel, ConfigDict, Field
from requests import Session
from requests.exceptions import HTTPError

from api.client import BASE_URL, get_post


class Post(BaseModel):
    model_config = ConfigDict(extra="ignore")

    userId: int = Field(gt=0, description="ID автора поста")
    id: int = Field(gt=0)
    title: str = Field(min_length=10, max_length=200)
    body: str = Field(min_length=10)


@pytest.mark.api
@responses.activate
def test_post_200_validated_with_pydantic(session: Session):

    fake_post = {
        "userId": 1,
        "id": 1,
        "title": "Это заголовок статьи",
        "body": "Это тело статьи",
    }

    responses.add(responses.GET, url=f"{BASE_URL}/posts/1", json=fake_post, status=200)

    result = get_post(session, 1)
    post = Post.model_validate(result)

    assert post.id == 1
    assert post.title == "Это заголовок статьи"


@pytest.mark.api
@responses.activate
def test_post_404_invalid(session):
    responses.add(responses.GET, url=f"{BASE_URL}/posts/1", status=404)

    with pytest.raises(HTTPError):
        get_post(session, 1)


@pytest.mark.api
@responses.activate
def test_post_500_invalid(session):
    responses.add(responses.GET, url=f"{BASE_URL}/posts/1", status=500)

    with pytest.raises(HTTPError):
        get_post(session, 1)

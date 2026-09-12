from unittest.mock import Mock

import pytest
from pydantic import BaseModel, ConfigDict, Field
from requests import Session

from api.client import get_post


class Post(BaseModel):
    model_config = ConfigDict(extra="ignore")

    userId: int = Field(gt=0, description="ID автора поста")
    id: int = Field(gt=0)
    title: str = Field(min_length=10, max_length=200)
    body: str = Field(min_length=10)


@pytest.mark.api
def test_get_200_with_mocker(session: Session, mocker):

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "userId": 1,
        "id": 1,
        "title": "Это заголовок статьи - 2",
        "body": "Это тело статьи - 2",
    }

    mock_response.raise_for_status.return_value = None

    mocker.patch.object(session, "get", return_value=mock_response)

    result = get_post(session, 1)

    post = Post.model_validate(result)
    assert post.id == 1

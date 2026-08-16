from pydantic import BaseModel, ConfigDict, Field, field_validator
from requests.exceptions import HTTPError, Timeout

class Post(BaseModel):
    model_config = ConfigDict(extra="ignore")

    userId: int = Field(gt=0, description="ID автора поста")
    id: int = Field(gt=0)
    title: str = Field(min_length=10, max_length=200)
    body: str = Field(min_length=10)

    @field_validator("title")
    @classmethod
    def clean_title(cls, title):
        title = title.strip()

        if not title:
            raise ValueError("Поле title не может быть пустым")

        return title


class User(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int = Field(gt=0)
    name: str = Field(min_length=2)
    username: str = Field(min_length=2)
    email: str
    posts: list[Post]


def test_post_validation():
    data = {
        "userId": 1,
        "id": 1,
        "title": "  Hello world  ",
        "body": "Hello world this is post",
    }

    post = Post.model_validate(data)

    assert post.userId == 1
    assert post.title == "Hello world"


def test_get_user_with_post():
    data = {
        "id": 1,
        "name": "Anton",
        "username": "anton",
        "email": "test@test.com",
        "posts": [
            {
                "userId": 1,
                "id": 1,
                "title": "Hello world test",
                "body": "Hello world this is post",
            }
        ],
    }

    user = User.model_validate(data)

    assert user.id == 1
    assert len(user.posts) == 1
    assert isinstance(user.posts[0], Post)
    assert user.posts[0].title == "Hello world test"

from pydantic import BaseModel, ConfigDict, Field

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


class Post(BaseModel):
    model_config = ConfigDict(extra="ignore")

    userId: int = Field(gt=0, description="ID автора поста")
    id: int = Field(gt=0, description="ID поста")
    title: str = Field(min_length=10, max_length=200, description="Заголовок поста")
    body: str = Field(min_length=10, max_length=2000, description="Содержание поста")


def test_get_post_validates_with_pydantic(session):
    """Проверка контракта полей"""

    response = session.get(url=f"{BASE_URL}/posts/1", timeout=TIMEOUT)

    assert response.status_code == 200

    post = Post.model_validate(response.json())

    assert post.id == 1


def test_get_posts_by_user_id(session):
    response = session.get(
        url=f"{BASE_URL}/posts", params={"userId": 1}, timeout=TIMEOUT
    )

    assert response.status_code == 200

    posts = response.json()
    assert len(posts) > 0

    for item in posts:
        post = Post.model_validate(item)
        assert post.userId == 1


def test_create_post_returns_201_and_validates(session):
    payload = {
        "userId": 1,
        "title": "Hello world",
        "body": "Hello world this is post",
    }

    response = session.post(url=f"{BASE_URL}/posts", json=payload, timeout=TIMEOUT)

    assert response.status_code == 201

    post = Post.model_validate(response.json())
    assert post.id == 101


def test_delete_post_returns_200_or_204(session):
    response = session.delete(url=f"{BASE_URL}/posts/1", timeout=TIMEOUT)

    assert response.status_code in (200, 204)

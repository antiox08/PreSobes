import pytest
import allure
from api.client import get_post


@pytest.mark.api
def test_get_post_has_required_fields(session):
    post_id = 1
    with allure.step(f'Запрос пост id={post_id}'):
        post = get_post(session, post_id)

    with allure.step('Проверить, что есть обязательные поля в ответе'):
        for field in ("id", "userId", "title", "body"):
            assert field in post


from requests import Session
from requests.exceptions import HTTPError, Timeout

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def create_post(session: Session, payload: dict) -> dict:
    """Создать пост"""
    try:
        response = session.post(
            url=f"{BASE_URL}/posts",
            json=payload,
            timeout=TIMEOUT,
        )

        response.raise_for_status()

        return response.json()

    except Timeout:
        raise RuntimeError(
            f"Таймаут {TIMEOUT} с при создании поста на {BASE_URL}/posts. "
            "Проверьте сеть или увеличьте TIMEOUT."
        )

    except HTTPError as exc:
        raise HTTPError(
            f"Не удалось создать пост. HTTP статус: {exc.response.status_code}"
        )


def get_post(session: Session, post_id: int) -> dict:
    """Получить пост"""

    try:
        response = session.get(
            url=f"{BASE_URL}/posts/{post_id}",
            timeout=TIMEOUT,
        )

        response.raise_for_status()

        return response.json()

    except Timeout:
        raise RuntimeError(
            f"Таймаут {TIMEOUT} с при получении поста "
            f"на {BASE_URL}/posts/{post_id}. "
            "Проверьте сеть или увеличьте TIMEOUT."
        )

    except HTTPError as exc:
        raise HTTPError(f"ошибка получения поста {exc.response.status_code}")

# PreSobes

Учебный проект автотестов: **pytest + Playwright (POM) + requests/API + Allure + GitHub Actions**.

## Структура

```text
PreSobes/
├── .github/workflows/     # CI (quality-gate + тесты)
├── api/                   # API-клиент и API-тесты (api/tests/)
├── pages/                 # Page Object для учебных UI-тестов (tests/)
├── tests/
│   ├── ui/                # UI-тесты Playwright (учебные)
│   └── ...                # фикстуры, practice, page object тесты
├── ui_tests/              # UI-тесты POM (DuckDuckGo / GitHub / login)
├── conftest.py            # общие фикстуры + Allure attachments
├── pytest.ini
├── requirements.txt
├── pyproject.toml         # black / isort / mypy
├── .pre-commit-config.yaml
└── reports/allure/        # Allure results (+ categories.json)
```


## Быстрый старт

```bash
git clone https://github.com/antiox08/PreSobes.git
cd PreSobes

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
# source .venv/bin/activate

pip install -r requirements.txt
playwright install chromium

# секреты не коммитим — копируем шаблон
copy .env.example .env   # Windows
# cp .env.example .env   # macOS / Linux
```

## Запуск тестов

### Все тесты (как локально)

```bash
pytest -q
```

### Только API

```bash
pytest api/ -q -m api
# или
pytest api/tests/ -q
```

### Только UI

```bash
pytest ui_tests/ tests/ui/ -q -m ui
```

### Стабильный набор как в CI

В CI UI к внешним сайтам часто нестабилен, поэтому pipeline гоняет:

```bash
pytest api/ tests/ --ignore=tests/ui -n auto --alluredir=reports/allure
```

### Allure-отчёт

После прогона результаты в `reports/allure/`. Просмотр (если установлен Allure CLI):

```bash
allure serve reports/allure
```

## Качество кода (перед коммитом)

В `requirements.txt`: **black**, **flake8**, **isort**, **mypy**, **pre-commit**.

```bash
black .
flake8 . --max-line-length=88 --extend-ignore=E203,W503
isort . --profile black
mypy tests/ --strict --follow-imports=skip

# или через pre-commit
pre-commit install
pre-commit run --all-files
```

## CI (GitHub Actions)

Workflow: `.github/workflows/tests.yml`

1. **quality-gate** — black / flake8 / isort / mypy  
2. **test-ui-api** — pytest (matrix Python 3.11 / 3.12) + артефакт Allure  

Статус: вкладка **Actions** в репозитории. К успешному run можно приложить ссылку/скрин в описании PR.

## Безопасность

- Файл **`.env`** в git **не** попадает (см. `.gitignore`).
- В репозитории только шаблон **`.env.example`** без реальных паролей/токенов.
- Не коммитьте `venv/`, `__pycache__/`, `.idea/`, `.vscode/`.

## Page Object

- Локаторы и действия — в `pages/` и `ui_tests/pages/`.
- В тестах — сценарии и **assert** / `expect()`, без дублирования селекторов.
- Без `time.sleep()` в UI: ожидания через Playwright auto-wait и `expect()`.

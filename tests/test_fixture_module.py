import pytest

@pytest.fixture(scope="module")
def counter():
    print('Создаем счетчик')
    yield 0

def test_one(counter):
    pass

def test_two(counter):
    pass

def test_three(counter):
    pass
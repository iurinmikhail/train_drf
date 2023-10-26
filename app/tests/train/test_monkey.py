import pytest


def some_function():
    return "Real function result"


def test_with_monkeypatch(monkeypatch):
    # Подменяем функцию some_function на собственную реализацию
    def fake_function():
        return "Fake function result"

    # Применяем monkeypatch.setattr для подмены функции
    monkeypatch.setattr("tests.train.test_monkey.some_function", fake_function)

    result = some_function()

    assert result == "Fake function result"


# В этом тесте функция some_function использует оригинальную реализацию
def test_without_monkeypatch():
    result = some_function()

    assert result == "Real function result"

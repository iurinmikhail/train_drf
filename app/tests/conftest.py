import pytest
from django.conf import settings



class CustomError(Exception):
    def __init__(self, message):
        self.message = message


@pytest.fixture(scope='session', autouse=True)
def setup_db():
    print('Запуск очистки базы данных')
    # assert settings.MODE == 'TEST', 'Нельзя запускать тесты на рабочей базе данных'
    if not settings.MODE == 'TEST':
        print('Нельзя запускать тесты на рабочей базе данных')
        raise CustomError('Нельзя запускать тесты на рабочей базе данных')
    yield
    print('Очистка базы данных')

import pytest
# Module - Действует на начало первого теста и в конце последнего теста
# function -

@pytest.fixture()
def set_up():
    print("Вход в систему")
    yield
    print('Выход из системы')

@pytest.fixture(scope='function')
def some():
    print("Начало")
    yield
    print('Конец')
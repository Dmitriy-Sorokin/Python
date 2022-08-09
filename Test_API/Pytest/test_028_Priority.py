import pytest

# Написать в терминале pytest -s -v
# fixture - это действия до тестов например авторизация на сайте
# yield - это действия после теста например выход из системы
# mark.run - очерёдность запуска тестов

@pytest.mark.run(order=5)
def test_sending_mail_piority():
    print('Priority')

@pytest.mark.run(order=6)
def test_sending_mail_Priority_1():
    print('Priority_1')

@pytest.mark.run(order=4)
def test_sending_mail_piority_2():
    print('Priority_2')

@pytest.mark.run(order=3)
def test_sending_mail_Priority_3():
    print('Priority_3')

@pytest.mark.run(order=2)
def test_sending_mail_piority_4():
    print('Priority_4')

@pytest.mark.run(order=1)
def test_sending_mail_Priority_5():
    print('Priority_5')

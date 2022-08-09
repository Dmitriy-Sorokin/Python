import pytest

# Написать в терминале pytest -s -v
# fixture - это действия до тестов например авторизация на сайте
# yield - это действия после теста например выход из системы


def test_sending_mail_10(set_up, some):
    print('Письмо отправлено')

def test_sending_mail_20(set_up, some):
    print('Письмо отправлено')


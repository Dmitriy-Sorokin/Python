import pytest

# Написать в терминале pytest -s -v
@pytest.fixture()
def set_up():
    print("Вход в систему")

def test_sending_mail(set_up):
    print('Письмо отправлено')

def test_sending_mail_1(set_up):
    print('Письмо отправлено')


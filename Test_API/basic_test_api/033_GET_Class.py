import requests
import json


class New_joke():
    '''Создание новой шутки'''

    def __init__(self):
        pass

    def create_new_random_joke(self):
        '''Создание рандомной шутки'''

        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print('status code: ' + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Create")
        else:
            print("ERROR")
        result.encoding = 'utf-8'

        print(result.text)
        check = result.json()
        # check_info = check.get("categories")
        # print(check_info)
        # assert check_info == []
        # print("Right all")
        check_info_value = check.get('value')
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
            print('Good')
        else:
            print('Not good')

random_joke = New_joke()

random_joke.create_new_random_joke()



# def create_new_random_joke():
#     '''Создание рандомной шутки'''
#
#     url = "https://api.chucknorris.io/jokes/random"
#     print(url)
#     result = requests.get(url)
#     print('status code: ' + str(result.status_code))


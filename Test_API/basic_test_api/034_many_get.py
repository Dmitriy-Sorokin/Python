import requests
import json


class New_joke():
    '''Создание новой шутки'''

    def __init__(self):
        pass

    def create_new_category(self):
        '''create new catgory'''
        category = "spor"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print('status code: ' + str(result.status_code))
        assert 404 == result.status_code
        if result.status_code == 404:
            print("Create")
        else:
            print("ERROR")
        result.encoding = 'utf-8'

        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["sport"]
        print("Right all")
        # check_info_value = check.get('value')
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print('Good')
        # else:
        #     print('Not good')



sport_joke = New_joke()
sport_joke.create_new_category()


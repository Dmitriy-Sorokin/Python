import requests
import json
import pprint


class New_location():
    '''Working with new location'''

    def create_new_location(self):
        '''create new location'''

        base_url = "https://rahulshettyacademy.com"  # Basic url
        key = "?key=qaclick123"  # Key

        '''Create method post'''
        post_resource = "/maps/api/place/add/json"  # Resource method post

        post_url = base_url + post_resource + key
        print(post_url)
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)
        print('status code: ' + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Create")
        else:
            print("ERROR")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("status code: " + str(check_info_post))
        assert check_info_post == "OK"
        print("Status TRUE")

        place_id = check_post.get("place_id")
        print("place_id: " + str(place_id))

        '''check create new location'''

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        # json_result_get = json.re
        pprint.pprint(result_get.text)

        print('status code: ' + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("TRUE")
        else:
            print("FALSE")

        '''change new location'''
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        json_for_update_new_location = {"place_id": place_id,
                                        "address": "100 Lenina street, RU",
                                        "key": "qaclick123"
                                        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        pprint.pprint(result_put.text)
        print('status code: ' + str(result_put.status_code))
        assert 200 == result_put.status_code
        if result_put.status_code == 200:
            print("TRUE")
        else:
            print("FALSE")

        check_put = result_put.json()
        check_put_info = check_put.get('msg')
        print('Mesage :' + check_put_info)
        assert check_put_info == "Address successfully updated"
        print("TRUE")

        '''check change new location'''

        result_get = requests.get(get_url)
        pprint.pprint(result_get.text)

        print('status code: ' + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("TRUE")
        else:
            print("FALSE")
        check_address = result_get.json()
        check_address_info = check_address.get("address")
        print('Mesage :' + check_address_info)
        assert check_address_info == "100 Lenina street, RU"
        print("TRUE")

        '''Delete new location'''

        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        print('status code: ' + str(result_delete.status_code))
        assert 200 == result_delete.status_code
        if result_delete.status_code == 200:
            print("TRUE")
        else:
            print("FALSE")
        check_status = result_delete.json()
        check_status_info = check_status.get("status")
        print('Mesage :' + check_status_info)
        assert check_status_info == "OK"
        print("TRUE")

        '''check delete new location'''

        result_get = requests.get(get_url)
        pprint.pprint(result_get.text)

        print('status code: ' + str(result_get.status_code))
        assert 404 == result_get.status_code
        if result_get.status_code == 404:
            print("TRUE")
        else:
            print("FALSE")
        check_address = result_get.json()
        check_address_info = check_address.get("msg")
        print('Mesage :' + check_address_info)
        assert check_address_info == "Get operation failed, looks like place_id  doesn\'t exists"
        print("TRUE")

new_place = New_location()

new_place.create_new_location()

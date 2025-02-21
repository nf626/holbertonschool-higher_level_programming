import json
import requests


def fetch_and_print_posts():
    """get api data and prints status and data"""
    api_url = 'https://jsonplaceholder.typicode.com/todos/1'
    response = requests.get(api_url, timeout=10)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        data = response.json()
        new_list = list(x for x in data)
        print(new_list)
    else:
        print("Failed to retrieve data".format(response.status_code))

def fetch_and_save_posts():
    pass

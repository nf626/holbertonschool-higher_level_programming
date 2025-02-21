import json
import requests


def fetch_and_print_posts():
    """get api data and prints status and data"""
    api_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(api_url, timeout=5)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        post = response.json()
        for key in post:
            print(f"{key['title']}")
    else:
        print("Failed to retrieve data".format(response.status_code))

def fetch_and_save_posts():
    pass

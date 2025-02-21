import json
import requests


def fetch_and_print_posts():
    """get api data and prints status and data"""
    api_url = 'https://jsonplaceholder.typicode.com/todos/1'
    response = requests.get(api_url)
    print(response.status_code)
    print(response.json())

def fetch_and_save_posts():
    pass

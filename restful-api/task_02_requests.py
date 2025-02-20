import requests
import json

def fetch_and_print_posts():
    api_url = 'https://jsonplaceholder.typicode.com/todos/1'
    response = requests.get(api_url)


def fetch_and_save_posts():

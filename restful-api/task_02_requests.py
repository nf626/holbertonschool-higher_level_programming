import json
import requests
import csv


def fetch_and_print_posts():
    """get api data and prints status and posts"""
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
    """get api data and store posts"""
    api_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(api_url, timeout=5)

    if response.status_code == 200:
        posts = response.json()
        for item in posts:
            post_list_dict = [{"id": item["id"], "title": item["title"], "body": item["body"]}]

        with open("posts.csv", mode="w", encoding="utf-8") as csv_file:
            field_names = ["id", "title", "body"]
            writer = csv.DictWriter(csv_file, fieldnames=field_names)

            writer.writeheader()
            writer.writerows(post_list_dict)
    else:
        print("Failed to retrieve data".format(response.status_code))

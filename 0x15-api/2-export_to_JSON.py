#!/usr/bin/python3
"""
Export to JSON
"""
import requests
from sys import argv
import json


if __name__ == "__main__":

    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    users_url = "https://jsonplaceholder.typicode.com/users/"
    id = argv[1]

    name = requests.get(users_url + id).json().get("username")
    task = requests.get(todos_url, params={"userId": id}).json()

    with open(id + '.json', 'w') as outfile:
        json.dump({id: [{"task": tt.get("title"), "completed": tt.get(
            "completed"), "username": name} for tt in task]}, outfile)

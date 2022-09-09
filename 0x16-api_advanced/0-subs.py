#!/usr/bin/python3
"""
returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    How many subs
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0 Win64x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'}

    response = requests.get(url, headers=header)
    json_response = response.json()

    if response.status_code == 404:
        return 0

    subscribers = json_response.get("data")
    return subscribers.get("subscribers")

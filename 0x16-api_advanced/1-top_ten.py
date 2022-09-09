#!/usr/bin/python3
"""
"""
import requests


def top_ten(subreddit):
    """
    How many subs
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0 Win64x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84'}

    response = requests.get(url, headers=header, params={"limit": 10}, allow_redirects=False)
    json_response = response.json()
    
    if response.status_code == 200:
        for i in json_response['data']['children']:
            print(i['data']['title'])

    elif response.status_code == 404:
        print(None)

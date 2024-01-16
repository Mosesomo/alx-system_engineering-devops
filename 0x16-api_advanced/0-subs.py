#!/usr/bin/python3
"""returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'my_app/1.0'}
    response = requests.get(url=url, headers=headers)
    if response.status_code >= 300:
        return 0
    data = response.json()
    return data['data']['subscribers']
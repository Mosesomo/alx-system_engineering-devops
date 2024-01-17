#!/usr/bin/python3
"""prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the
        titles of the first 10 hot posts listed for a given subreddit.
    """
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers, allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    data = response.json()
    [print(post.get('data').get('title'))
    for post in data.get("data").get("children")]
#!/usr/bin/python3
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Write a function that queries the Reddit API and returns the number of subscribers
    :param subreddit:  (not active users, total subscribers) for a given subreddit.
    :return: If an invalid subreddit is given, the function should return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/owoyemi)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")





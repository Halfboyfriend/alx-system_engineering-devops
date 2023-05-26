#!/usr/bin/python3
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Write a function that queries the Reddit API and returns the number of subscribers
    :param subreddit:  (not active users, total subscribers) for a given subreddit.
    :return: If an invalid subreddit is given, the function should return 0.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    response = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
    v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    suscriber = response.get("data", {}).get("subscribers", 0)
    return suscriber





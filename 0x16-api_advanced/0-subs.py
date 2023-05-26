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
    header = {
        'User-Agent': '0x16-api_advanced:project:\
        v1.0.0 (by /u/firdaus_cartoon_jr)'
    }
    response = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     params=header).json()
    suscriber = response.get("data", {}).get("subscribers", 0)
    return suscriber





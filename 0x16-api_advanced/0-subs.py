#!/usr/bin/python3
"""MOdules"""
import requests


def number_of_subscribers(subreddit):
    """numer"""
    Url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(Url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        dd = response.json()
        subscribers = dd['data']['subscribers']
        return subscribers
    else:
        return 0

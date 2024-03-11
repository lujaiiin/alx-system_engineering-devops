#!/usr/bin/python3
"""
    Modules
"""
import requests


def number_of_subscribers(subreddit):
    """
        numbers_of_sub
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:Python (by/AjwadG)"}

    data = requests.get(url, headers=headers, allow_redirects=False)

    if data.ok:
        value = data.json().get("data").get("subscribers")
        return value if value is not None else 0
    return 0

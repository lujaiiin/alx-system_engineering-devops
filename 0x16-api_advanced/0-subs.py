#!/usr/bin/python3
"""Modules"""
import requests


def number_of_subscribers(subreddit):
    """number"""
    
    RLl = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    hed = {"User-Agent": "ubuntu:Python (by/lujaiiin)"}
    dd = requests.get(RLl, headers=hed, allow_redirects=False)
    if dd.ok:
        v = dd.json().get("data").get("subscribers")
        return v if v is not None else 0
    return 0

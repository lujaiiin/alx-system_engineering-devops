#!/usr/bin/python3
"""Modules"""
import re
import requests
import sys as s


API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(s.argv) > 1:
        if re.fullmatch(r'\d+', s.argv[1]):
            id = int(s.argv[1])
            req = requests.get('{}/users/{}'.format(API, id)).json()
            task = requests.get('{}/todos'.format(API)).json()
            name = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task))
            completed = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    name,
                    len(completed),
                    len(tasks)
                )
            )
            if len(completed) > 0:
                for task in completed:
                    print('\t {}'.format(task.get('title')))

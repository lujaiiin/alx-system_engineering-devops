#!/usr/bin/python3
"""Modules"""
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    resp = requests.get(url)
    name = resp.json().get('name')

    Url = url + "/todos"
    resp = requests.get(Url)
    tasks = resp.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, name, task.get('completed'),
                               task.get('title')))

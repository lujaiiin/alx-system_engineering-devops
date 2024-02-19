#!/usr/bin/python3
"""Modules"""
import requests
import sys

if __name__ == '__main__':
    employeeId = int(sys.argv[1])
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + str(employeeId)

    resp = requests.get(url)
    name = resp.json().get('name')

    todosUrl = "https://jsonplaceholder.typicode.com/todos?userId=" + str(employeeId)
    resp = requests.get(todosUrl)
    tasks = resp.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, name, task.get('completed'),
                               task.get('title')))

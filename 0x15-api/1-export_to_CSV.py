#!/usr/bin/python3
"""Modules"""
import csv
import requests
import sys

if __name__ == '__main__':
    # Convert the employee ID to an integer
    employeeId = int(sys.argv[1])
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + str(employeeId)

    resp = requests.get(url)
    name = resp.json().get('name')

    # Define the URL for todos with the correct user ID
    todosUrl = "https://jsonplaceholder.typicode.com/todos?userId=" + str(employeeId)
    resp = requests.get(todosUrl)
    tasks = resp.json()

    # Write the tasks to a CSV file
    with open('{}.csv'.format(employeeId), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employeeId, name, task.get('completed'), task.get('title')])

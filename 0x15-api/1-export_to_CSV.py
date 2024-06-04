#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys


def fetch_user_data(user_id):
    """Fetches user data from the API."""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()


def fetch_todos(user_id):
    """Fetches todos for a specific user ID from the API."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id})
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user = fetch_user_data(user_id)
        username = user.get("username")
        if not username:
            print(f"No user found with ID {user_id}")
            sys.exit(1)

        todos = fetch_todos(user_id)

        with open("{}.csv".format(user_id), "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(["User ID", "Username", "Completed", "Title"])
            for todo in todos:
                writer.writerow([
                  user_id, username, todo.get("completed"), todo.get("title")
                ])

    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
        sys.exit(1)

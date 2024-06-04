#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.

This script takes an employee ID as a command-line argument and exports
the corresponding user information and to-do list to a JSON file.
"""

import json
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

        data_to_export = {
            user_id: [
                {
                    "task": t.get("title"),
                    "completed": t.get("completed"),
                    "username": username
                }
                for t in todos
            ]
        }

        with open("{}.json".format(user_id), "w") as jsonfile:
            json.dump(data_to_export, jsonfile, indent=4)

    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
        sys.exit(1)

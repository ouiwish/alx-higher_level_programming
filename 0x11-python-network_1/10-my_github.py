#!/usr/bin/python3
"""
Python script that takes GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        user_info = response.json()
        github_id = user_info.get('id')
    else:
        return None
    print(github_id)
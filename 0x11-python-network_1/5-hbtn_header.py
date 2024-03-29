#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""
import requests
import sys

def get_request_id(url):
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)

if __name__ == "__main__":
    url = sys.argv[1]
    get_request_id(url)

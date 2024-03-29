#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.
"""
from  urllib import request
import sys

def fetch_x_request_id(url):
    """
    Fetches the URL and displays the value of the X-Request-Id header.
    """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)

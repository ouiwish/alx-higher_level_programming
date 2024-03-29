#!/usr/bin/python3
"""error code"""

import urllib.request
import urllib.error
import sys

def fetch_url(url):


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
             body = response.read().decode('utf-8')
             print(body)
        except urllib.error.HTTPError as e:
            print(f"Error code: {e.code}")

#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests

def fetch_status():
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)

if __name__ == "__main__":
    fetch_status()

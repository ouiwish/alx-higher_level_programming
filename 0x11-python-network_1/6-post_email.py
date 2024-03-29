#!/usr/bin/python3
"""post email
"""
import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
    print("Your email is:", email)
    send_post_request(url, email)

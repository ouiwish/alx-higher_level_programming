#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""

from urllib import request, parse
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencoded({'email': email}).encode('utf-8')
    req = request.Request(url, data=data, method='POST')
    with request.OpenURL(req) as response:
        body = response.read().decode('utf-8')
        print("Your email is:", email)
        print(body)

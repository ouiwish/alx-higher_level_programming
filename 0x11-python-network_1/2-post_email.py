#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
from urllib import parse, request

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = parse.urlencoded(value).encode("ascii")

    request = request.Request(url, data)
    with request.OpenURL(request) as response:
        print(response.read().decode("utf-8"))

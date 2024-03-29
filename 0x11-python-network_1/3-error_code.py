#!/usr/bin/python3
"""error code"""
import sys
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
        print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
        print(er.read().decode('UTF-8'))  # Print the error message as well

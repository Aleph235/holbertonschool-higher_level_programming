#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found
in the header of the response"""
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as Url:
        headers = Url.info()
        print(headers.get('X-Request-Id'))

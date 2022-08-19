#!/usr/bin/python3
import urllib.request
""" fetches https://intranet.hbtn.io/status """
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
print("\t- type:", type(html))
print("\t- content:", html)
print("\t- utf8 content:", html.decode("utf-8"))

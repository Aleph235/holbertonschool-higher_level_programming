#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests
    r = requests.get('https://intranet.hbtn.io/status')
    text = r.text
    print("Body response:")
    print("\t- type:", type(text))
    print("\t- content:", text)

#!/usr/bin/python3
"""Request to a server using urllib"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        print("- Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
except urllib.error.HTTPError as e:
    print("Error:", e.code)
except urllib.error.URLError as e:
    print("Error:", e.reason)

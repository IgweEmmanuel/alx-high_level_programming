#!/usr/bin/python3
"""Request to a server using urllib"""
import urllib


if __name__ == '__main__':

    url = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    with urllib.request.urlopen(url) as response:
        output = response.read()
        utf8 = output.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(output))
    print("\t- content", output)
    print("\t- utf8 content:", utf8)

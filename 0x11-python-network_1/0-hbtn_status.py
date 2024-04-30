#!/usr/bin/python3
"""Request to a server using urllib"""
import urllib.request


if __name__ == "__main__":
    """This prints reads the url response using with"""
    url = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(url) as response:
        output = response.read()
        utf8 = output.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(output)))
        print("\t- content {}".format(output))
        print("\t- utf8 content: {}".format(utf8))

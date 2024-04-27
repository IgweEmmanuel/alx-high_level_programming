#!/usr/bin/python3
"""Use request module to request to url"""
import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res = request.get(url)
    print("Body response:")
    print("\t -type: ", type(res.text))
    print("\t -content: ", res.text)   

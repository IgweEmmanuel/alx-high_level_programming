#!/usr/bin/python3
"""Gets X-Request-I"""
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv != 2):
        sys.exit(1)

    url_args = sys.argv[1]

    if not url_args.startswith('http://') and not url_args.startswith('https://'):
        sys.exit(1)

    url = urllib.request.Request(url_args)

    with urllib.request.urlopen(url) as response:
        value = response.headers.get('X-Request-Id')
        if value:
            print(value)
        else:
            sys.exit(1)

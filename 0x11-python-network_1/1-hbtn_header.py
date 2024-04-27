#!/usr/bin/python3
# Gets X-Request-Id

import urllib.request
import sys

if (len(sys.argv) != 2):
    sys.exit(1)

url_args = sys.argv[1]

if not url_args.startswith('http://') and not url_args.startswith('https://'):
    sys.exit(1)

with urllib.request.urlopen(url_args) as response:
    value = response.headers.get('X-Request-Id')
    if value:
        print(value)
    else:
        sys.exit(1)

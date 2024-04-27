#!/usr/bin/python3
#Gets X-Request-Id

import urllib.request
import sys

if (len(sys.argv) != 2):
    sys.exit(1)

with urllib.request.urlopen(sys.argv[1]) as response:
    value = response.headers.get('X-Request-Id')
    if value:
        print(value)
    else:
        sys.exit(1)

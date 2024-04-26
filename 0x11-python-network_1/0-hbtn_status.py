#!/usr/bin/python3
# Request to a server using urllib
import urllib.request


req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    output = response.read()

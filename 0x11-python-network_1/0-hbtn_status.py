#!/usr/bin/python3
# Request to a server using urllib
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    output = response.read()
    utf8 = output.decode('utf-8')
print('Body response:')
print('\t - content:', type(output))
print('\t - utf8 content:', utf8)

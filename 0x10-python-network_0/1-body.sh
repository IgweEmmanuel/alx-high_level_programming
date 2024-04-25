#!/bin/bash
#http status code
curl -s -w "%{http_code}" -o /dev/null "$1" | grep -q 200 && curl -s "$1"

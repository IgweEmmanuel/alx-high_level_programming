#!/bin/bash
#http status code
curl -sL -w "%{http_code}" "$1" | grep -eq "200" | curl -s "$1"

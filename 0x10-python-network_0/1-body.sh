#!/bin/bash
#http status code
curl -sL -w "%{http_code}" -o /dev/null "$1"

#!/bin/bash
#http status code
curl -s -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"

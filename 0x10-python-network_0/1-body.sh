#!/bin/bash
#http status code
curl -s -w "%{http_code}" "$1"

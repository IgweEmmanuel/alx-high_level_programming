#!/bin/bash
#http status code
curl -sL -w "%{http_code}" "$1"

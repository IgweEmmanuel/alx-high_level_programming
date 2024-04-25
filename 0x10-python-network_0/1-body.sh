#!/bin/bash
#http status code
curl -sL $1 | grep -q 200


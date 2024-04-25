#!/bin/bash
#sends request to URL and displays the size of the body of response
curl -s -o /dev/null -w "%{size_download}" $1

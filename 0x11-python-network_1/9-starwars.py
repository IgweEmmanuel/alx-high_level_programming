#!/usr/bin/python3
"""Search request for a given string to the Star War"""
import sys
import requests


if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    params = {"search": sys.argv[1]}
    results = requests.get(url, params=params).json()

    print("Number of results: {}".format(results.get("count")))
    [print(r.get("name")) for r in results.get("results")]

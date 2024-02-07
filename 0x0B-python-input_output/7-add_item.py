#!/usr/bin/python3
"""Python write into file"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = load_from_json_file("add_item.json") or []

filename.extend(sys.argv[1:])

save_to_json_file(filename, "add_item.json")

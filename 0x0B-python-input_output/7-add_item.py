#!/usr/bin/python3
"""Python write into file"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = load_from_json_file("add_item.json")
with open(filename, 'w', encoding='utf-8') as myFile:
    myFile = []
myFile.extend(sys.argv[1:])
save_to_json_file(myFile, "add_item.json")

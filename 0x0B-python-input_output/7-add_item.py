#!/usr/bin/python3
"""Python write into file"""
import json

save = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

json.dump(save(load_from_json_file(filename), filename), filename)

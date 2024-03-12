#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    # Check if the file exists, load its content into data
    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []

    # Add all arguments to the list
    data.extend(sys.argv[1:])

    # Save the list as a JSON representation to add_item.json
    save_to_json_file(data, "add_item.json")

if __name__ == "__main__":
    main()


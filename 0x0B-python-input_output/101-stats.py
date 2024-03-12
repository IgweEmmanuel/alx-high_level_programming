#!/usr/bin/python3
"""stats to generte code"""
import sys

def print_statistics(total_size, status_counts):
    """prints statistics"""
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_counts.items()):
        print("{}: {}".format(status_code, count))

total_size = 0
status_counts = {}

try:
    for i, line in enumerate(sys.stdin, start=1):
        try:
            ip_address = line.split()[0]
            status_code = line.split()[11]
            file_size = line.split()[12]
            total_size += int(file_size)
            status_counts[status_code] = status_counts.get(status_code, 0) + 1
        except (ValueError, IndexError):
            continue

        if i % 10 == 0:
            print_statistics(total_size, status_counts)
except KeyboardInterrupt:
    print_statistics(total_size, status_counts)


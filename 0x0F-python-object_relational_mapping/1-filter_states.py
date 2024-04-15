#!/usr/bin/python3
"""
This script filters the table row
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    This is the filtering section
    of the code
    """
    if len(argv) != 4:
    print('You should use this format:
            {}, user, password, database', format(argv[0]))
    sys.exit(1)

username = argv[1]
password = argv[2]
database = argv[3]

db = MySQLdb.connect(host='localhost',
                    user=username, port=3306,
                    passwd=password, db=database)

cursor = db.cursor

cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")

states = cursor.fetchall()

for state in states:
    print(state)

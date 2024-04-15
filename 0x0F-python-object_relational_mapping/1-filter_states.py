#!/usr/bin/python3
"""
This script filters the table row
"""


import MySQLdb
import sys

if __name__ == '__main__':
    """
    This is the filtering section
    of the code
    """
    if len(sys.argv) != 4:
    print('You should use this format:
            {}, user, password, database', format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host='localhost',
                    port=3306, user=username,
                    passwd=password, db=database)

cursor = db.cursor

cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")

states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
db.close()

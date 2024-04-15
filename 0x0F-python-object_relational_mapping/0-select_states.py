#!/usr/bin/python3
"""
This script get all states from
the database 
"""
import MySQLdb
import sys

if __name__ == '__main__':
    """
    This side of the script accesses
    the database and gets the states
    """

    db = MySQLdb.connect(
                        host='localhost',
                        port=3306, user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3])

cursor = db.cursor

cursor.execute("SELECT * FROM states")

states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
db.close()

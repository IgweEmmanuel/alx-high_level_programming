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
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
                        host='localhost',
                        user=username, port=3306,
                        passwd=password,
                        db=database)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states\
                    WHERE name LIKE BINARY %(name)s\
                    ORDER BY states.id ASC", {'name':argv[4]})

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()

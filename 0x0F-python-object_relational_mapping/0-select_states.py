#!/usr/bin/python3
import MySQLdb
import sys

if len(sys.argv) != 4:
    print('You should use this format: {}, user, password, database', format(sys.argv[0]))
    exit(1)
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host='localhost', user=username, port=3306, passwd=password, db=database)

cursor = db.cursor

cursor.execute("SELECT * FROM states ORDER BY id ASC")

states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
db.close()

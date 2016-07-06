#!/usr/bin/python
import dbconnect

db = dbconnect.dbconnect();

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT name FROM employee order by name;")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]

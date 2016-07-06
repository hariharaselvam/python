#!/usr/bin/python
import MySQLdb

def dbconnect():
	db1 = MySQLdb.connect(host="localhost", user="root",  passwd="root", db="test")
	return db1;




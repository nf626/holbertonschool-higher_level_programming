#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb


MY_HOST = 'localhost'
MY_USER = 'root'
MY_DB = 'hbtn_0e_0_usa'
MY_PORT = 3306

db = MySQLdb.connect(host=MY_HOST, user=MY_USER, port=MY_PORT, passwd='', db=MY_DB) 
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS states ("
"id INT NOT NULL AUTO_INCREMENT,"
"name VARCHAR(256) NOT NULL,"
"PRIMARY KEY (id))"
)
db.close()

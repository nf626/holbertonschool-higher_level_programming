#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    # Connect to Database
    MY_HOST = 'localhost'
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    MY_PORT = 3306

    # Connect method
    db = MySQLdb.connect(
        host=MY_HOST,
        user=MY_USER,
        port=MY_PORT,
        passwd=MY_PASS,
        db = MY_DB
    )

    # Cursor
    # interact with and manipulate the results of a database query
    cur = db.cursor()

    # Parameterized query

    # executing SQL queries on the database
    cur.execute()

    # Fetch all rows in column
    records = cur.fetchall()

    # Show column and values

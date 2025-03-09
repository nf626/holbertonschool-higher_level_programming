#!/usr/bin/python3
"""takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys


if __name__ == '__main__':
    # Connect to Database
    MY_HOST = 'localhost'
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    MY_PORT = 3306
    STATE_NAME = sys.argv[4]

    # Connect method
    db = MySQLdb.connect(
        host=MY_HOST,
        user=MY_USER,
        port=MY_PORT,
        passwd=MY_PASS,
        db=MY_DB
    )

    # Cursor
    # interact with and manipulate the results of a database query
    cur = db.cursor()

    # executing SQL queries on the database
    # SQL commands   
    records = cur.execute(
        "SELECT * FROM states\
        WHERE BINARY name LIKE '{}' ORDER BY id ASC".format(STATE_NAME))

    # Fetch all rows in column
    records = cur.fetchall()

    # SHow column and values
    for row in records:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()

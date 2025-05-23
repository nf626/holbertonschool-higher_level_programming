#!/usr/bin/python3
"""takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""
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

    # Parameterized query
    operation = "SELECT cities.id, cities.name, states.name\
        FROM states, cities\
        WHERE cities.state_id = states.id\
        AND BINARY states.name LIKE %s\
        ORDER BY cities.id ASC"

    # tuple to insert at placeholder
    data = (STATE_NAME,)

    # executing SQL queries on the database
    cur.execute(operation, data)

    # Fetch all rows in column
    records = cur.fetchall()

    # Show values
    cities = ", ".join([row[1] for row in records])
    print(cities)

    # Close cursor and database connection
    cur.close()
    db.close()

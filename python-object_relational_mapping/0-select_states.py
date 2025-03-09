#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb

if __name__ == '__main__':

    # Connect to Database
    MY_HOST = 'localhost'
    MY_USER = 'root'
    MY_DB = 'hbtn_0e_0_usa'
    MY_PORT = 3306

    # Connect method
    db = MySQLdb.connect(
        host=MY_HOST,
        user=MY_USER,
        port=MY_PORT,
        passwd='',
        db=MY_DB
        ) 

    # Cursor
    # interact with and manipulate the results of a database query
    cur = db.cursor()

    # executing SQL queries on the database
    # SQL commands
    records = cur.execute("SELECT * FROM states")
    
    # Fetch all rows in database
    records = cur.fetchall()

    # Show column and values
    for state in records:
        print(state)

    # Close cursor and database connection
    cur.close()
    db.close()

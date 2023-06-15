#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
the script takes 3 arguments
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL connection parameters from command line arguments
    username, password, database = sys.argv[1:4]

    # Create connection object and cursor
    connection = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = connection.cursor()

    # Execute query and fetch results
    cursor.execute("SELECT * FROM states")
    results = cursor.fetchall()

    # Print results
    for state in results:
        print(state)

    # Close cursor and connection
    cursor.close()
    connection.close()

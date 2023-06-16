#!/usr/bin/python3
"""
 lists all states from the database hbtn_0e_0_usa
should connect to a MySQL server running on localhost
""" 
import sys
import MySQLdb

if __name__ == "__main__":
    # Get my SQL connection parameters from the command line #
    username, password, database = sys.argv[1:4]

    #Create connection object and cursor#
    connection = MySQLdb.connect(host="localhost", user="username", password="password", db="database")
    cursor = cursor.connect()

    # Execute query and fetch results
    cursor.execute("SELECT * FROM states")
    # Fetch the results
    results = cursor.fetchall()

    #print results
    for states in results:
        print(states)

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

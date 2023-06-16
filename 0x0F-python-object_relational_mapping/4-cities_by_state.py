#!/usr/bin/python3
"""
Listsall cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL dbwith provided credentials#
    connection = MySQLdb.connect(user=[argv1], passwd=[argv2], db=[argv3])

    # Create a cursor object
    cur = connection.cursor()

    # Execute SQL query that lists cities from corresponding names#
    cur.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities JOIN states ON cities.state_id = states.id
                    ORDER BY cities.id ASC""")

    # Fetch  and print/display cities#
    [print(city), for city in cur.fetchall()]

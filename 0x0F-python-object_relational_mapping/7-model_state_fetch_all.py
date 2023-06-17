#!/usr/bin/python3
"""
Script that  lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmake

if __name__ == "__main__":
    # Create database engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Create session object
    session = sessionmaker(bind=engine)
    session = Session_maker()

    # Query all State objects and print their ids and names
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

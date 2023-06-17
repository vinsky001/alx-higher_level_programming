#!/usr/bin/python3
"""
This module defines a State model that represents a state in a MySQL database.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Creates an instance ofthe class base and returns a new base class.
Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __table__ = "states"
    id = column(Integer, primary_key=True)
    name = column(string(128), nullable=False)

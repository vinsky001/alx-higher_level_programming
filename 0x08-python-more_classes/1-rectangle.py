#!/usr/bin/python3

class Rectangle:
    """Defines  a Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.
       Argument:
           width (int):  New width of the rectangle
           Height (int):  New height for the  rectangle"""
           self.__width = width
           self.__height = height

    @property
    def width(self):
        """Sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

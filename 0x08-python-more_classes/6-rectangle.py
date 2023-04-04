#!/usr/bin/python3

"""defines a rectangle class"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes/creates a new Rectangle
         Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
            """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """sets the height the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        "returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """returns the printable representation of the rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        return (("#" * self.width) + "\n") * self.height

    def __repr__(self):
        """returns the string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """returns the printable message after every deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

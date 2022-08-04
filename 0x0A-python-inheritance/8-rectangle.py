#!/usr/bin/python3
"""BaseGeometry class module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle geometry class"""

    def __init__(self, width, height):
        """Sets the width and height of a Rectangle instance

            width (int): The width of the Rectangle
            height (int): The height of the Rectange
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

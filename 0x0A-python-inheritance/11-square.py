#!/usr/bin/python3
"""BaseGeometry class module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represent a Square"""

    def __init__(self, size):
        """Sets the square size.

            Args:
                size (int): The size of the Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

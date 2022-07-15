#!/usr/bin/python3
"""Define an object name Square.
"""



class Square:
<<<<<<< HEAD
    """ Object Square [a class]"""

=======
    """ Object Square [class]
    """
>>>>>>> 55994b7e531d2d3e1545b9c3a515301c3f8ecdc3
    def __init__(self, size=0):
        """ Initialize method.
        Args:
            self (class): This class
            size (int): Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

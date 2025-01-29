#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise Square attributes and methods"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """"The propery of size as the len of a side of Square
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """property of the coordinates of this Square
        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Get the area of a Square
        Returns: The size squared
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for i in range(self.position[1]):
            pos = pos + "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                pos = pos + " "
            for k in range(self.size):
                pos = pos + "#"
            pos = pos + "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')

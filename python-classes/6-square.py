#!/usr/bin/python3
"""Access and update private attribute"""


class Square:
    """Class to create square"""
    __size = None
    __position = None
# initialise method
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

# Size property and setter
    @property
    def size(self):
        """size getter method"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size setter method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

# Position property and setter
    @property
    def position(self):
        """position getter method"""
        return (self.__position)
    @position.setter
    def position(self, value):
        """position setter method"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

# Area of square
    def area(self):
        """Calculate area"""
        return (self.__size ** 2)

# Print square
    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end='')
                print("#" * self.size)

#!/usr/bin/python3
"""Access and update private attribute"""


class Square:
    """Class to create square"""
    __size = None
    __position = None
# initialise method

    def __init__(self, size=0, position=(0, 0)):
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
        """set the position of this Square"""
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    # Area of square
    def area(self):
        """Calculate area"""
        return (self.__size ** 2)

# Print square
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

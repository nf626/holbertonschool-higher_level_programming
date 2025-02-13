#!/usr/bin/python3
"""Student to JSON with filter module"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation"""
        if attrs is None:
            return self.__dict__
        else:
            # return {k: v for k, v in self.__dict__.items() if k in attrs}
            for key, value in self.__dict__.items():
                if key in attrs:
                    i = {key:value}
                    return i

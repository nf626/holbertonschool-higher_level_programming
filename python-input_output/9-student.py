#!/usr/bin/python3
"""Student class module"""
class_to_json = __import__('8-class_to_json').class_to_json


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation"""
        return class_to_json(self)

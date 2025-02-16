#!/usr/bin/env python3
"""Pickle module"""
import pickle


class CustomObject:
    """custom object class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """convert to"""
        with open(filename, mode="wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """convert back"""
        try:
            with open(filename, mode="rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return None

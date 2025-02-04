#!/usr/bin/env python3
"""Animal ABS Module"""
from abc import *


class Animal(ABC):
    """Animal class"""
    @abstractmethod
    def sound(self):
        """Animal sound"""
        raise NotImplementedError("sound() must be implemented")

class Dog(Animal):
    """Dog class"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Cat class"""
    def sound(self):
        return "Meow"

#!/usr/bin/env python3
"""Flying Fish module"""


class Fish:
    """Fish class"""
    def swim(self):
        """swim method"""
        print("The fish is swimming")

    def habitat(self):
        """fish habitat method"""
        print("The fish lives in water")

class Bird:
    """Bird class"""
    def fly(self):
        """fly method"""
        print("The bird is flying")

    def habitat(self):
        """bird habitat method"""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Flyingfish class"""
    def fly(self):
        """flyingfish fly method"""
        print("The flying fish is soaring!")

    def swim(self):
        """flyingfish swim method"""
        print("The flying fish is swimming!")

    def habitat(self):
        """flyingfish habitat method"""
        print("The flying fish lives both in water and the sky!")

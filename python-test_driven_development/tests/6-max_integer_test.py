#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for max integer"""
    def test_max_integer(self):
        """max int is 4"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_int_beginning(self):
        """max int found in beginning"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_int_middle(self):
        """max int found in middle"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_max_int_negative(self):
        """max int found in middle"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_int_one_negative(self):
        """max int found in middle"""
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

    def test_max_int_one_element(self):
        """one element"""
        self.assertEqual(max_integer([3]), 3)


    def test_empty(self):
        """empty"""
        self.assertEqual(max_integer([]), None)

    if __name__ == '__main__':
        unittest.main()

#!/bin/python3.7

import unittest

class Cell():
    def CheckAlive(self):
        return True

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        cell = Cell()
        self.assertTrue(cell.CheckAlive(), True)

if __name__ == '__main__':
    unittest.main()

#!/bin/python3.7

import unittest

class Cell():
    x = 0

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        cell = Cell()
        cell.isAlive = True
        self.assertTrue(cell.CheckAlive(), True)

if __name__ == '__main__':
    unittest.main()

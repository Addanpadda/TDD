#!/bin/python3.7

import unittest

class Cell():
    isAlive = 0

    def CheckAlive(self):
        return True

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        cell = Cell()
        cell.isAlive = True
        self.assertTrue(cell.CheckAlive(), True)

if __name__ == '__main__':
    unittest.main()

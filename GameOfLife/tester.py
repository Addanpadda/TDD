#!/bin/python3.7

import unittest

class Cell():
    def CheckAlive(self):
        return True

class TestStringMethods(unittest.TestCase):
    def test_CheckAlive_True(self):
        cell = Cell()
        self.assertTrue(cell.CheckAlive())

    def test_CheckAlive_False(self):
        cell = Cell()
        self.assertFalse(cell.CheckAlive())

if __name__ == '__main__':
    unittest.main()

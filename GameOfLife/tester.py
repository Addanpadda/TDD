#!/bin/python3.7

import unittest

class TestStringMethods(unittest.TestCase):
    
    cell = Cell()
    cell.isAlive = True

    def test_upper(self):
        self.assertTrue(cell.CheckAlive(), True)

if __name__ == '__main__':
    unittest.main()

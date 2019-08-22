#!/bin/python3.7
import unittest
from game import *

class Tests(unittest.TestCase):
    def test_Universe_Cell_Should_Be_Alive_rule_1(self):
        universe = Universe(3, 3)

        universe.space[1][1].Alive(True)
        self.assertFalse(universe.CellShouldBeAlive(1, 1))

    def test_Universe_Cell_Should_Be_Alive_rule_2(self):
        universe = Universe(3, 3)
        
        universe.space[0][1].Alive(True)
        universe.space[2][1].Alive(True)
        self.assertFalse(universe.CellShouldBeAlive(1, 1))
        
        universe.space[1][1].Alive(True)
        self.assertTrue(universe.CellShouldBeAlive(1, 1))

    def test_Universe_Cell_Should_Be_Alive_rule_3(self):
        universe = Universe(3, 3)

        universe.space[1][0].Alive(True)
        universe.space[0][1].Alive(True)
        universe.space[2][1].Alive(True)
        universe.space[1][2].Alive(True)
        universe.space[1][1].Alive(True)
        self.assertFalse(universe.CellShouldBeAlive(1, 1))

    def test_Universe_Cell_Should_Be_Alive_rule_4(self):
        universe = Universe(3, 3)

        universe.space[1][0].Alive(True)
        universe.space[0][1].Alive(True)
        universe.space[2][1].Alive(True)
        self.assertTrue(universe.CellShouldBeAlive(1, 1))

    
    def test_Cell_CheckAlive_True(self):
        cell = Cell()
        cell.Alive(True)
        self.assertTrue(cell.CheckAlive())

    def test_Cell_CheckAlive_False(self):
        cell = Cell()
        cell.Alive(False)
        self.assertFalse(cell.CheckAlive())
    
    def test_Universe_CreateUniverse(self):
        universe = Universe(3, 3)
        self.assertEqual(sum(len(x) for x in universe.space), 9)

    def test_Universe_Neighbours_diagonal(self):
        universe = Universe(3, 3)

        universe.space[0][0].Alive(True)
        self.assertEqual(universe.Neighbours(1, 1), 1)
        universe.space[0][2].Alive(True)
        self.assertEqual(universe.Neighbours(1, 1), 2)
        universe.space[2][0].Alive(True)
        self.assertEqual(universe.Neighbours(1, 1), 3)
        universe.space[2][2].Alive(True)
        self.assertEqual(universe.Neighbours(1, 1), 4)

    def test_Universe_Neighbours_diagonal_edge_of_space(self):
        universe = Universe(3, 3)

        universe.space[1][1].Alive(True)
        self.assertEqual(universe.Neighbours(0, 0), 1)
    
    def test_Universe_Neighbours_linear(self):
        universe = Universe(3, 3)

        universe.space[0][1].Alive(True)
        self.assertEqual(universe.Neighbours(1, 1), 1)
        universe.space[1][0].Alive(True)
        self.assertEqual(universe.Neighbours(1, 1), 2)
        universe.space[1][2].Alive(True)
        self.assertEqual(universe.Neighbours(1, 1), 3)
        universe.space[2][1].Alive(True)
        self.assertEqual(universe.Neighbours(1, 1), 4)

    def test_Universe_Neighbours_linear_edge_of_space(self):
        universe = Universe(3, 3)

        universe.space[0][1].Alive(True)
        self.assertEqual(universe.Neighbours(0, 0), 1)
        universe.space[1][0].Alive(True)
        self.assertEqual(universe.Neighbours(0, 0), 2)

    def test_Universe_Import(self):
        universe = Universe(3, 4)
        world = [
            [1, 0, 0],
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]
        universe.Import(world)

        for x in range(3):
            for y in range(3):
                self.assertEqual(universe.space[x][y].CheckAlive(), world[x][y]) 


if __name__ == '__main__':
    unittest.main()

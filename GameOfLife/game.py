#!/bin/python3.7
import os
import time

class Cell():
    _isAlive = 0
    
    def Alive(self, isAlive):
        self._isAlive = isAlive

    def CheckAlive(self):
        return self._isAlive

class Universe():
    _dimentions = [0, 0]
    space = list()

    def __init__(self, dimention_x, dimention_y):
        self._dimentions = [dimention_x, dimention_y]
        self.space = self.CreateUniverse(dimention_x, dimention_y)

    def CellShouldBeAlive(self, x, y):
        neighbours = self.Neighbours(x, y)
        alive = self.space[x][y].CheckAlive()
        
        if alive:
            if neighbours is 2 or neighbours is 3:  # Rule 2
                return True
        else:
            if neighbours is 3:  # Rule 4
                return True

        return False   # Rule 1 & 3 and other situations

    def CreateUniverse(self, x_dimention, y_dimention):
        cells = []
        
        for y in range(y_dimention):
            cells.append([])
            for x in range(x_dimention):
                cells[y].append(Cell())
        
        return cells

    def Neighbours(self, x, y):
        neighbours = 0
        neighbourTest = [x+1, y+1]

        while True:
            for x in range(2):
                if int(neighbourTest[0]) >= 0 and int(neighbourTest[1]) >= 0:
                    neighbours += self.space[neighbourTest[0]][neighbourTest[1]].CheckAlive()
                neighbourTest[0] -= 1
            
            for x in range(2):
                if neighbourTest[0] >= 0 and neighbourTest[1] >= 0:
                    neighbours += self.space[neighbourTest[0]][neighbourTest[1]].CheckAlive()
                neighbourTest[1] -= 1

            for x in range(2):                                                           
                if neighbourTest[0] >= 0 and neighbourTest[1] >= 0:
                    neighbours += self.space[neighbourTest[0]][neighbourTest[1]].CheckAlive()
                neighbourTest[0] += 1

            for x in range(2):
                if neighbourTest[0] >= 0 and neighbourTest[1] >= 0:
                    neighbours += self.space[neighbourTest[0]][neighbourTest[1]].CheckAlive()
                neighbourTest[1] += 1
            
            return neighbours
    
    def Cycle(self):
        space_update = list()

        for x in range(len(world)-1):
            space_update.append([])
            for y in range(len(world[0])-1):
                space_update[x].append(self.CellShouldBeAlive(x, y))
                #print('NEw x:', x,',y', y,': :', self.CellShouldBeAlive(x, y))
        self.Import(space_update)

    def Import(self, world):
        for x in range(len(world)):
            for y in range(len(world[0])):
                self.space[x][y].Alive(bool(world[x][y]))

    def Print(self):
        for x in range(len(world)):
            print()
            for y in range(len(world[0])):
                if self.space[x][y].CheckAlive():
                    print(' * ', end='')
                else:
                    print('   ', end='')


if __name__ == '__main__':
    universe = Universe(20, 20)
    world = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    universe.Import(world)
   
    while True:
        os.system('clear')
        universe.Print()
        universe.Cycle()
        time.sleep(1)

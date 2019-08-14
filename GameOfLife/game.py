#!/bin/python3.7

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

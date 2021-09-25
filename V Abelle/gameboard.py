import random
from cell import Cell

class GameBoard():

    """Function __init__"""
    def __init__(self):
        self.width = 40
        self.high = 23
        self.cells = []
        self.nonreachables =[]
        self.createGameboard()
        self.randomWorld()

    """Function createGameboard, creates the gameboard"""
    def createGameboard(self):
        for columna in range (0, self.high):
            list = []
            for fila in range (0, self.width):
                list.append(Cell())
            self.cells.append(list)

    """Function randomBiome, generates random biomes"""
    def randomBiome(self):
        biome = numbertobiomes[random.randrange(1,4)]
        return biome

    """Function randomWorld, creates the world randomly and filters it"""
    def randomWorld(self):
        for Y in range(23):
            for X in range(40):
                ran = str(self.randomBiome())
                self.cells[Y][X].setBiome(ran)

        for Y in range(23):
            for X in range(40):
                #edges
                if X == 0 or Y == 0 or X == 39 or Y == 22:
                    self.cells[Y][X].setBiome("barrier")
                    continue
                
                #rivers
                if self.cells[Y + 1][X].biome == "water" and self.cells[Y - 1][X].biome == "water" or self.cells[Y + 1][X].biome == "water" and self.cells[Y][X - 1].biome == "water":
                    lake = random.randrange(1,6)
                    if lake == 1:
                        self.cells[Y][X].setBiome("water")
                        self.cells[Y][X].setCellCoordinates(Y,X)
                
                #ground
                if self.cells[Y + 1 ][X].biome == "dirt" and self.cells[Y][X + 1].biome == "dirt" and self.cells[Y][X - 1].biome == "dirt":
                    self.cells[Y][X].setBiome("dirt")
                    #mountains
                    mountain = random.randrange(1,11)
                    if mountain == 1:
                        self.cells[Y][X].setBiome("mountain")
                        self.cells[Y][X].setCellCoordinates(Y,X)
                        continue
                
                #plants
                if self.cells[Y][X].biome == "dirt":
                    plant = self.randomPlants()
                    self.cells[Y][X].setPlants(plant)
                    continue
    
    """Function getTiles, returns the biome from a cell"""
    def getTiles(self,y,x):
        self.cells[y][x].setCellCoordinates(x,y)
        biome = self.cells[y][x].biome
        return biome

    """Function cleanGameboard, deletes the biomes from a cell"""
    def cleanGameboard(self):
        for x in range (self.high):
            for y in range (self.width):
                self.cells[y][x].setBiome("")

    """Function randomPlants, generates plants randomly"""
    def randomPlants(self):
        plants = numbertoplants[random.randrange(1,3)]
        return plants

    """Function checkFreeSpace, checks if a cell is free"""
    def checkFreeSpace(self,coord):
        if coord in self.nonreachables:
            return False
        else:
            return True

numbertobiomes = {
    1 : "water",
    2 : "dirt",
    3 : "dirt" 
    }
    
numbertoplants = {
    1 : "grass",
    2 : "tree",
    3 : "flower"
    }
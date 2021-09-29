import random
from cell import Cell

class GameBoard():

    """Function __init__"""
    def __init__(self):
        self.cells = []

    """Function addCellAndBiome, adds a Cell object to the correspondent list and establishes a biome"""
    def addCellAndBiome(self,x,y,biome):
        self.cells[x].append(Cell())
        self.cells[x][y].setBiome(biome)

    """Function assignSize, assigns the size from the map"""
    def assignSize(self,width):
        for x in range(width):
            self.cells.append([])

    """Fucntion checkBiome, checks wath biome has the cell"""
    def checkBiome(self, posX, posY):
        return self.cells[posX][posY].readBiome()
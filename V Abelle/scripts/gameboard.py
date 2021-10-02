import random
from cell import Cell

class GameBoard():

    """Function __init__"""
    def __init__(self):
        self.cells = []
        self.width = 40
        self.height = 23
        self.nonreachables =[]
        self.createBoard()

    """Function createBoard, creates a game board from 40x23"""
    def createBoard(self):
        for column in range (0, self.height):
            list = []
            for row in range (0, self.width):
                list.append(Cell())
            self.cells.append(list)

    """Function biomeRandom, generates biomes randomly"""
    def biomeRandom(self):
        biome = number_to_biomes[random.randrange(1,4)]
        return biome

    """Function randomWorld, create the world randomly and filters it"""
    def randomWorld(self):
        for Y in range(self.height):
            for x in range(self.width):
                ran = str(self.biomeRandom())
                self.cells[Y][x].setBiome(ran)

        for Y in range(self.height):
            for x in range(self.width):
                #bordes
                if x == 0 or Y == 0 or x == (self.width-1) or Y == (self.height-1):
                    self.cells[Y][x].setBiome("Barrier")
                    continue
                
                #rios
                if self.cells[Y + 1][x].biome == "Water" and self.cells[Y - 1][x].biome == "Water" or self.cells[Y + 1][x].biome == "Water" and self.cells[Y][x - 1].biome == "Water":
                    lake = random.randrange(1,6)
                    if lake == 1:
                        self.cells[Y][x].setBiome("Water")
                        self.cells[Y][x].setCoordinates(Y, x)
                
                #tierra firme
                if self.cells[Y + 1 ][x].biome == "Dirt" and self.cells[Y][x + 1].biome == "Dirt" and self.cells[Y][x - 1].biome == "Dirt":
                    self.cells[Y][x].setBiome("Dirt")
                    #montañas
                    mountain = random.randrange(1,11)
                    if mountain == 1:
                        self.cells[Y][x].setBiome("Mountain")
                        self.cells[Y][x].setCoordinates(Y, x)
                        continue
                
                #plantas
                if self.cells[Y][x].biome == "Dirt":
                    plant = self.plantsRandom()
                    self.cells[Y][x].setPlants(plant)
                    continue

    """Function backgroundWorld, create the world randomly and filters it"""
    def backgroundWorld(self):
        for Y in range(23):
            for x in range(40):
                ran = str(self.biomeRandom())
                self.cells[Y][x].setBiome(ran)

        for Y in range(23):
            for x in range(40):
                #bordes
                if x == 0 or Y == 0 or x == 39 or Y == 22:
                    continue

                #rios
                if self.cells[Y + 1][x].biome == "Water" and self.cells[Y - 1][x].biome == "Water" or self.cells[Y + 1][x].biome == "Water" and self.cells[Y][x - 1].biome == "Water":
                    lake = random.randrange(1,6)
                    if lake == 1:
                        self.cells[Y][x].setBiome("Water")
                        self.cells[Y][x].setCoordinates(Y, x)
                
                #tierra firme
                if self.cells[Y + 1 ][x].biome == "Dirt" and self.cells[Y][x + 1].biome == "Dirt" and self.cells[Y][x - 1].biome == "Dirt":
                    self.cells[Y][x].setBiome("Dirt")
                    #montañas
                    mountain = random.randrange(1,11)
                    if mountain == 1:
                        self.cells[Y][x].setBiome("Mountain")
                        self.cells[Y][x].setCoordinates(Y, x)
                        continue
                
                #plantas
                if self.cells[Y][x].biome == "Dirt":
                    plant = self.plantsRandom()
                    self.cells[Y][x].setPlants(plant)
                    continue

    """Function getTiles, returns the biome from a cell"""
    def getTiles(self, y, x):
        self.cells[y][x].setCoordinates(x, y)
        biome = self.cells[y][x].biome
        return biome
    
    """Function eraseBoard, deletes the biome from a cell"""
    def eraseBoard(self):
        for x in range (self.height):
            for y in range (self.width):
                self.cells[y][x].setBiome("")

    """Function plantsRandom, generates plants randomly"""
    def plantsRandom(self):
        plants = number_to_plants[random.randrange(1,3)]
        return plants

    """Function checkSpace, checks if the cell is free"""
    def checkSpace(self, coord):
        if coord in self.nonreachables:
            return False
        else:
            return True

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
    
    """Function hideAllCells, sets the visibility from all the cells on 'False'"""
    def hideAllCells(self):
        for x in range(len(self.cells)):
            for y in range(len(self.cells[0])):
                self.cells[x][y].hideCell()
    
    """Function revealCell, changes the visibility from an especific cell to 'True'"""
    def revealCell(self, posX, posY):
        self.cells[posX][posY].showCell()
    
    """Function getVisibility, asks to the cell if it's visible or not"""
    def getVisibility(self,posX,posY):
        return self.cells[posX][posY].getVisibility()

number_to_biomes = {
    1 : "Water",
    2 : "Dirt",
    3 : "Dirt" 
    }
    
number_to_plants = {
    1 : "Grass",
    2 : "Tree",
    3 : "Flower"
    }
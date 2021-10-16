import random
from cell import Cell

class GameBoard():

    def __init__(self,width,height):
        """Function __init__"""
        self.cells = []
        self.width = 40
        self.height = 33
        self.nonreachables =[]
        self.createBoard()

    def createBoard(self):
        """Function createBoard, creates a game board from 40x23"""
        for column in range (0, self.height):
            list = []
            for row in range (0, self.width):
                list.append(Cell())
            self.cells.append(list)

    def biomeRandom(self):
        """Function biomeRandom, generates biomes randomly"""
        biome = number_to_biomes[random.randrange(1,4)]
        return biome

    def randomWorld(self):
        """Function randomWorld, create the world randomly and filters it"""
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

    def backgroundWorld(self):
        """Function backgroundWorld, create the world randomly and filters it"""
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

    def getTiles(self, y, x):
        """Function getTiles, returns the biome from a cell"""
        self.cells[y][x].setCoordinates(x, y)
        biome = self.cells[y][x].biome
        return biome
    
    def eraseBoard(self):
        """Function eraseBoard, deletes the biome from a cell"""
        for x in range (self.height):
            for y in range (self.width):
                self.cells[y][x].setBiome("")

    def plantsRandom(self):
        """Function plantsRandom, generates plants randomly"""
        plants = number_to_plants[random.randrange(1,3)]
        return plants

    def checkSpace(self, coord):
        """Function checkSpace, checks if the cell is free"""
        if coord in self.nonreachables:
            return False
        else:
            return True

    def setBiome(self,x,y,biome):
        """Function setBiome, adds a Cell object to the list and establishes the biome"""
        self.cells[x][y].setBiome(biome)

    def getBiome(self,x,y):
        """Function getBiome, """
        biome = self.cells[x][y].getBiome()
        return biome

    def addCellAndBiome(self,x,y,biome):
        """Function addCellAndBiome, adds a Cell object to the correspondent list and establishes a biome"""
        self.cells[x].append(Cell())
        self.cells[x][y].setBiome(biome)

    def assignSize(self,width):
        """Function assignSize, assigns the size from the map"""
        self.cells = []
        for x in range(width):
            self.cells.append([])

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
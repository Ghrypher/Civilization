import random, pygame

class Cell:


    def __init__(self):
        """ constructor de la clase """
        self.biome = ""
        self.revealed = False
        self.active = False
        self.x = None
        self.y = None
        self.neighbors = []
        self.barrier = False
    
    def __str__(self):
        return self.biome

    def __lt__(self, other):
	    return False

    def setCoordinates(self, x, y):
        """Sets the row and collum of the cell"""
        self.x = x
        self.y = y
    
    def getPosition(self):
        """Gets the position of the cell"""
        return self.x, self.y

    def getNeighbors(self):
        return self.neighbors

    def isBarrier(self):
        self.barrier = True

    def isNotBarrier(self):
        self.barrier = False

    def getBarrier(self):
        return self.barrier

    def getBiome(self):
        """Gets the biome of the cell"""
        return self.biome

    def addNeighbors(self, neighbor):
	    self.neighbors.append(neighbor)

    def resetCell(self):
        self.open = False
        self.closed = False
        self.start = False
        self.end = False

    def revealCell(self):
        """Reveals the cell"""
        self.revealed = True
        self.active = True
    
    def getVisibility(self):
        """Obtains if the cell is being seen or if it was seen"""
        return self.revealed, self.active
    
    def hideCell(self):
        """Hide the cell"""
        self.active = False

class Dirt(Cell):

    def __init__(self):
        super().__init__() 
        self.biome = "D"
        self.unit = None

    def getUnit(self):
        return self.unit

    def setUnit(self, unit):
        self.unit = unit
    
    def eraseUnit(self):
        self.unit = None

class Mountain(Cell):

    def __init__(self):
        super().__init__() 
        self.biome = "M"

class Water(Cell):
    
    def __init__(self):
        super().__init__() 
        self.biome = "W"

class Iron(Cell):

    def __init__(self):
        super().__init__() 
        self.biome = "I"

class Gold(Cell):

    def __init__(self):
        super().__init__() 
        self.biome = "G"

class Forest(Cell):

    def __init__(self):
        super().__init__() 
        self.biome = "F"
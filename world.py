import random, os
from cell import *
from units import *

class World():
    def __init__(self):
        """ constructor de la clase """
        self.ancho = None
        self.alto = None
        self.unit = []
        self.cells = []
        self.map_to_text = {"Barrier" : "B",
                            "Dirt" : "D",
                            "Water" : "W",
                            "Mountain" :"M",
                            "Iron" : "I",
                            "Gold" : "G",
                            "Revealed" :"R",
                            "Forest" : "F",
                            "Hidden" : "H"}
        self.textToClass = {
            "D" : Dirt,
            "M" : Mountain,
            "W" : Water,
            "I" : Iron,
            "G" : Gold,
            "F" : Forest
        }
        self.textToUnit = {
            "WR" : Warrior,
            "WK" : Worker,
            "FD" : Founder
        }
        self.number_to_biomes = {1 : Water,
                                2 : Dirt,
                                3 : Dirt, 
                                4: Dirt}
        self.number_to_plants = {1 : "Grass",
                                2 : "Tree",
                                3 : "Flower"}

    def setWorldSize(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto                 

    def random_world(self):
        """ crea el mundo aleatoriamente y lo filtra """
        for columna in range (0, self.alto):
            lista = []
            self.cells.append(lista)

        for Y in range(self.alto):
            for x in range(self.ancho):
                self.cells[Y].append(self.number_to_biomes[random.randrange(1, 5)]())

        for Y in range(self.alto):
            for x in range(self.ancho):
                #bordes
                if x == 0 or Y == 0 or x == (self.ancho-1) or Y == (self.alto-1):
                    self.cells[Y].pop(x)
                    self.cells[Y].insert(x, Dirt())
                    continue
                
                #tierra firme
                if (str(self.cells[Y + 1 ][x]) == "D" or str(self.cells[Y + 1 ][x]) == "F" or str(self.cells[Y + 1 ][x]) == "M") and (str(self.cells[Y][x + 1]) == "D" or str(self.cells[Y][x + 1]) == "F" or str(self.cells[Y][x + 1]) == "M") and (str(self.cells[Y][x - 1]) == "D" or str(self.cells[Y][x - 1]) == "F" or str(self.cells[Y][x - 1]) == "M"):
                    self.cells[Y].pop(x)
                    self.cells[Y].insert(x, Dirt())
                    #montañas
                    mountain = random.randrange(1,16)
                    if mountain == 1:
                        mineral = random.randrange(1,11)
                        if mineral <= 5:
                            self.cells[Y].pop(x)
                            self.cells[Y].insert(x, Iron())
                        if mineral > 5 and mineral <= 7 :
                            self.cells[Y].pop(x)
                            self.cells[Y].insert(x, Gold())
                        if mineral > 7 and mineral <= 10 :
                            self.cells[Y].pop(x)
                            self.cells[Y].insert(x, Mountain())
                    continue
                
                #rios
                if str(self.cells[Y + 1][x]) == "W" and str(self.cells[Y - 1][x]) == "W" and str(self.cells[Y][x - 1]) == "W":
                    lake = random.randrange(1,6)
                    if lake == 1:
                        self.cells[Y].pop(x)
                        self.cells[Y].insert(x, Water())
                    else:
                        self.cells[Y].pop(x)
                        self.cells[Y].insert(x, Dirt())
                
                #forests
                if str(self.cells[Y][x]) == "D" :
                    forest = random.randrange(1,6)
                    if forest == 1:
                        self.cells[Y].pop(x)
                        self.cells[Y].insert(x, Forest())
                    if self.cells[Y + 1 ][x] == "F" and self.cells[Y][x + 1] == "F" and self.cells[Y][x - 1] == "F":
                        self.cells[Y].pop(x)
                        self.cells[Y].insert(x, Forest())
                    continue

        self.document_txt("Maps/random_world.txt")
        f = open("Maps/random_world.txt", "a+")
        for y in range(self.alto):
            f.write("\n")
            for x in range(self.ancho):
                tile = str(self.cells[y][x])
                f.write(tile)

    def save_game(self, map):
        print("game saved")
        self.document_txt("Maps/save.txt")
        f = open("maps/save.txt", "a+")
        for y in range(len(map[0])):
            f.write("\n")
            for x in range(len(map)):
                f.write(self.getBiome(x, y))
    
    def limpiar_tablero(self):
        """Elimina todo el tablero para poder crear uno nuevo"""
        self.cells = []
    
    def plants_random(self):
        """ genera plantas aleatoriamente """
        plants = self.number_to_plants[random.randrange(1,3)]
        return plants
    
    def set_biome(self, x, y, biome):
        """Añade un objeto Cell a la lista correspondiente y le establece el bioma"""
        self.cells[x][y].set_biome(biome)

    def getBiome(self, x, y):
        """  """
        biome = self.cells[x][y].getBiome()
        return biome
    
    def getCellData(self, x, y):
        """Gets the biome and the units or estructures on the cell"""
        if str(self.cells[x][y]) == "D":
            return self.cells[x][y].getBiome(), self.cells[x][y].getUnit()
        else:
            return self.cells[x][y].getBiome(), None
    
    def addCellAndBiome(self, x, biome):
        """Añade un objeto Cell a la lista correspondiente y le establece el bioma"""
        self.cells[x].append(self.textToClass[biome]())
    
    def assignSize(self, width):
        """Asigna el tamaño del tablero segun el tamaño del mapa"""
        self.cells = [] 
        for _ in range(width):
            self.cells.append([])
    
    def document_txt(self,path):
        f = open(path, "w")
        f.write(";Map made by Santella Agustin")
        f.write("\n")
        f.write(";element index")
        f.write("\n")
        f.write(";  D : Diert")
        f.write("\n")
        f.write(";  M : Mountain")
        f.write("\n")
        f.write(";  W : Water")
        f.write("\n")
        f.write("\n")
        f.write("; starting the level:")

    def checkUnit(self, posX, posY):
        """  """
        for x in range(len(self.Unit)):
            pos = self.Unit[x].getPosition()
            if pos == (posX, posY):
                index = self.Unit[x].getIndex()
                return index
        
    def addUnit(self, posX, posY, index, type, team):
        self.Unit.append(Unit(type, team))
        self.Unit[index].setPosition(posX, posY)

    def erase_Units(self):
        self.Unit = []
    
    def getWidthHeight(self):
        """Gets the width and the height of the actual map"""
        return len(self.cells), len(self.cells[0])
    
    def assignNewUnit(self, posX, posY, type):
        unit = self.textToUnit[type]()
        unit.setPosition(posX, posY)
        self.cells[posX][posY].setUnit(unit)
        self.unit.append(unit)
    
    def reassignUnit(self, posX, posY, newPosX, newPosY):
        unit = self.cells[posX][posY].getUnit()
        self.cells[posX][posY].eraseUnit()
        unit.setPosition(newPosX, newPosY)
        self.cells[newPosX][newPosY].setUnit(unit)

    def getUnit(self, x, y):
        return self.cells[x][y].getUnit()

    def revealMap(self):
        for unit in self.unit:
            unit.revealMap(self.cells)
    
    def getCellVisibility(self, x, y):
        return self.cells[x][y].getVisibility()

    def hideAllCells(self):
        """Hide all the cells in the map"""
        for x in range(0, len(self.cells)):
            for y in range(0, len(self.cells[0])):
                self.cells[x][y].hideCell()

    def clearWorld(self):
        self.cells = []

    def restartAllUnitMovement(self):
        """Restarts the movement of all the units"""
        for unit in self.unit:
            unit.restartMovement()


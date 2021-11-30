from os import fsdecode
import random
from queue import PriorityQueue
from cell import *
from units import *
from structures import *

class World:
    def __init__(self):
        """ constructor de la clase """
        self.ancho = None
        self.alto = None
        self.unit = []
        self.structures = []
        self.cells = []
        self.mapToText = {"Barrier" : "B",
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
            "FD" : Founder,
            "AR" : Archer,
            "CP" : Catapult,
            "EX" : Explorer,
        }
        self.textToStructure = {
            "CT" : City,
            "PT" : Port,
            "SM" : Sawmill,
            "IM" : IronMine,
            "GM" : GoldMine
        }
        self.number_to_biomes = {1 : Water,
                                2 : Dirt,
                                3 : Dirt, 
                                4: Dirt}
        self.number_to_plants = {1 : "Grass",
                                2 : "Tree",
                                3 : "Flower"}

    def setWorldSize(self, ancho, alto):
        """Sets the width and height of the world"""
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

        self.document_txt("maps/random_world.txt")
        f = open("maps/random_world.txt", "a+")
        for y in range(self.alto):
            f.write("\n")
            for x in range(self.ancho):
                tile = str(self.cells[y][x])
                f.write(tile)
    
    def getBiome(self, x, y):
        """Gets the biome of the cell"""
        biome = self.cells[x][y].getBiome()
        return biome
    
    def getCellData(self, x, y):
        """Gets the biome and the units or estructures on the cell"""
        return self.cells[x][y].getBiome(), self.cells[x][y].getUnit()
    
    def addCellAndBiome(self, x, y, biome):
        """Añade un objeto Cell a la lista correspondiente y le establece el bioma"""
        biomeSet = self.textToClass[biome]()
        biomeSet.setCoordinates(x, y)

        if str(biomeSet) != "D":
            biomeSet.isBarrier()
            
        self.cells[x].append(biomeSet)
    
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
    
    def getWidthHeight(self):
        """Gets the width and the height of the actual map"""
        return len(self.cells), len(self.cells[0])
    
    def assignNewUnit(self, posX, posY, type, resource):
        """Creates a new unit and assigns it to a cell"""
        unit = self.textToUnit[type]()
        unit.setResources(resource) #Sets the resources to consume food
        unit.setPosition(posX, posY) #Sets the position
        self.cells[posX][posY].isBarrier() #Tells that the cell is a barrier
        self.updateCellNeighbors(posX, posY)
        self.cells[posX][posY].setUnit(unit) #Assign the unit to the cell
        self.unit.append(unit)
    
    def assignNewStructure(self, posX, posY, type, resources):
        """Creates a new structure and assigns it to a cell"""
        structure = self.textToStructure[type]()
        structure.setPosition(posX, posY) #Sets the position
        structure.setResources(resources) 
        self.cells[posX][posY].setUnit(structure) #Assign the structure to the cell
        self.structures.append(structure)
    
    def reassignUnit(self, posX, posY, newPosX, newPosY):
        """Removes a unit from one cell and assigns it to a new cell"""
        unit = self.cells[posX][posY].getUnit() #Gets the unit
        self.cells[posX][posY].isNotBarrier()
        self.updateCellNeighbors(posX, posY)
        self.cells[posX][posY].eraseUnit() #Remove the unit from the cell where it was
        unit.setPosition(newPosX, newPosY)
        self.cells[newPosX][newPosY].setUnit(unit) #Assigns it to the new cell
        self.cells[newPosX][newPosY].isBarrier()
        self.updateCellNeighbors(newPosX, newPosY)

    def getUnit(self, x, y):
        """Gets the unit of a cell"""
        return self.cells[x][y].getUnit()

    def revealMap(self):
        """For each unit reveal the map"""
        for unit in self.unit:
            unit.revealMap(self.cells)
        for structure in self.structures:
            structure.revealMap(self.cells)
    
    def getCellVisibility(self, x, y):
        """Gets the visibility of the cell"""
        return self.cells[x][y].getVisibility()

    def hideAllCells(self):
        """Hide all the cells in the map"""
        for x in range(0, len(self.cells)):
            for y in range(0, len(self.cells[0])):
                self.cells[x][y].hideCell()

    def clearWorld(self):
        """Clears the world"""
        self.cells = []

    def restartAllUnitActions(self):
        """Restarts the movement of all the units"""
        for unit in self.unit:
            unit.restartActions()

    def updateAllNeighbors(self):
        """Update the neighbors of all the cells"""
        for x in range(len(self.cells)):
            for y in range(len(self.cells[0])):
                self.cells[x][y].updateNeighbor(self.cells)
    
    def updateCellNeighbors(self, x, y):
        """Update the neighbor of the neighbor cell"""        
        if x < len(self.cells) - 1: #RIGHT
            self.cells[x + 1][y].updateNeighbor(self.cells)
        if x > 0: #LEFT
            self.cells[x - 1][y].updateNeighbor(self.cells)
        if y < len(self.cells[0]) - 1: #DOWN
            self.cells[x][y + 1].updateNeighbor(self.cells)
        if y > 0: #UP
            self.cells[x][y - 1].updateNeighbor(self.cells)

    def h(self, p1, p2):
        """Gets the distance between one cell and other"""
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def AStar(self, start, end):
        """Executes a path finding algorithm to find the best path from one point to other"""
        count = 0
        openSet = PriorityQueue()
        openSet.put((0, count, start))
        cameFrom = {}
        gScore = {node: float("inf") for x in self.cells for node in x}
        gScore[start] = 0
        fScore = {node: float("inf") for x in self.cells for node in x}
        fScore[start] = self.h(start.getPosition(), end.getPosition())

        openSetHash = {start}

        while not openSet.empty():

            current = openSet.get()[2]
            openSetHash.remove(current)

            if current == end:
                coordinates = []
                while current in cameFrom:
                    coordinates.append(current.getPosition())
                    current = cameFrom[current]
                return coordinates

            for neighbor in current.getNeighbors():
                tempGScore = gScore[current] + 1
                if tempGScore < gScore[neighbor]:
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tempGScore
                    hola = neighbor.getPosition()
                    adios = end.getPosition()
                    fScore[neighbor] = tempGScore + self.h(hola, adios)
                    if neighbor not in openSetHash:
                        count += 1
                        openSet.put((fScore[neighbor], count, neighbor))
                        openSetHash.add(neighbor)
        
        return []

    def getAllUnits(self):
        """Return the list of units in the game"""
        return self.unit

    def checkDeaths(self):
        """Checks if the units or structures died to erase them"""
        index = 0
        for x in range(len(self.unit)):
            unit = self.unit[index]
            life, maxLife = unit.getHealthData()
            if life <= 0:
                posX, posY = unit.getPosition()
                self.cells[posX][posY].eraseUnit()
                self.unit.remove(unit)
            else:
                index += 1

        index = 0
        for y in range(len(self.structures)):
            structure = self.structures[index]
            life, maxLife = structure.getHealthData()
            if life <= 0:
                posX, posY = structure.getPosition()
                self.cells[posX][posY].eraseUnit()
                self.structures.remove(structure)
            else:
                index += 1
    
    def healUnits(self):
        """Heals an unit if resting"""
        for unit in self.unit:
            unit.healUnit()

    def removeUnit(self, unit):
        """Removes a unit from the list"""
        self.unit.remove(unit)

    def getAllUnitsInformation(self):
        """Gets the units and the cost of each one"""
        unitsDict = {}
        for unit in self.textToUnit.values():
            unit = unit()
            unitsDict[str(unit)] = unit.getCreationData()
        
        return unitsDict

    def checkProductionFinished(self):
        """Checks if the production of a unit has finished"""
        for city in self.structures:
            if str(city) == "CT":
                city.reduceTime() #Reduce the time production by 1
                posX, posY = city.getPosition() #Gets the position of the city
                unitX, unitY = None, None

                #Checks if there is space arround the city to spawn an unit
                for x in range(posX - 2, posX + 3):
                    for y in range(posY - 2, posY + 3):
                        if x >= 0 and x < len(self.cells) and y >= 0 and y < len(self.cells[0]):
                            biome, unit = self.getCellData(x, y)
                            if biome == "D" and unit == None:
                                if unitX == None:
                                    unitX, unitY = x, y

                #If there is space then checks if an unit finished producing
                if unitX != None:
                    unit = city.productionFinished()
                    if unit != None:
                        city.assignNewUnit()
                        self.assignNewUnit(unitX, unitY, unit, city.getResources())
                        self.revealMap()

    def modifyResources(self):
        """Adds resources from the structures and reduce them from the units"""
        for structure in self.structures:
            structure.addResources() #Adds resources generated by the structure

        for unit in self.unit:
            unit.consumeFood() #Unit consumes food to live
        
    def killAllUnits(self):
        """Kills all the units"""
        for x in range(len(self.unit)):
            posX, posY = self.unit[0].getPosition()
            self.cells[posX][posY].eraseUnit()
            self.unit.remove(self.unit[0])

    def getStructureCost(self, type):
        """Gets the costo of construction of the structure and returns it"""
        structure = self.textToStructure[type]()
        return structure.getConstructionCost()

    def setAllUnitsRoute(self):
        """Sets all the units route"""
        for unit in self.unit:
            if unit.getPositionToMove() != (None, None):
                if unit.getPosition() != unit.getPositionToMove():
                    posX, posY = unit.getPosition()
                    posToMoveX, posToMoveY = unit.getPositionToMove()
                    unit.setRoute(self.AStar(self.cells[posX][posY], self.cells[posToMoveX][posToMoveY]))
            else:
                unit.setRoute([])
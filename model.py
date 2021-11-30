import random, math,os
from world import World
from resources import Resources

class Model():

    def __init__(self):
        """Loads the variables and execute the methods when the class is created"""
        self.world = World()

        self.mapWidth = None
        self.mapHeight = None

        self.mapNeedsRedraw = False

        self.actualUnit = None
        self.unitMenu = None

        self.actualCity = None
        self.cityMenu = None

        self.attack = None #Saves is a unit is going to attack
        self.construct = None #Saces if a worker is going to construct

        self.resources = Resources()

        self.biomeToStructure = {
            "W" : "PT",
            "F" : "SM",
            "G" : "GM",
            "I" : "IM"
        }

    def setAttack(self, value):
        """Sets the attack event"""
        self.attack = value

    def setConstruct(self, value):
        """change the value if the worker is constructing or not"""
        self.construct = value

    def randomMap(self, width, height):
        """Generates a txt with a random map"""
        self.world.setWorldSize(width, height)
        self.world.random_world()

    def readMap (self, file):
        """Reads a txt file with the map"""
        assert os.path.exists(file), 'Cannot find the level file: %s' % (file)
        M_File = open(file, "r")
        content = M_File.readlines() + ["\r\n"]
        M_File.close()

        M_TextLines = []
        M_Obj = []

        for lineNum in range(len(content)):
            line = content[lineNum].rstrip('\r\n')

            # Si encuentra un ";" en la linea actual devuelve ""
            if ";" in line:
                line = line[:line.find(";")]

            # Si tiene algo lo añade a la lista con las lineas de texto del mapa
            if line != "":
                M_TextLines.append(line)

            elif line == "" and len(M_TextLines) > 0:
                maxWidth = -1

                # Busca la fila mas larga de todas
                for i in range(len(M_TextLines)):
                    if len(M_TextLines[i]) > maxWidth:
                        maxWidth = len(M_TextLines[i])

                # Las empareja llenando con espacios si es que hace falta
                for i in range (len(M_TextLines)):
                    M_TextLines[i] += " " * (maxWidth - len(M_TextLines[i]))

                # Añade una lista por cada linea de mapa
                for x in range (len(M_TextLines[0])):
                    M_Obj.append([])

                # Invierte el mapa para que quede al derecho en la matriz
                for y in range (len(M_TextLines)):
                    for x in range (maxWidth):
                        M_Obj[x].append(M_TextLines[y][x])
                
        self.createBoard(M_Obj)

    def createBoard(self, M_Obj):
        """Crea el tablero de la clase board y le asigna el bioma a cada celda"""

        self.world.assignSize(len(M_Obj))

        for x in range(len(M_Obj)):
            for y in range(len(M_Obj[0])):
                self.world.addCellAndBiome(x, y, M_Obj[x][y])
        
        self.world.updateAllNeighbors()

    def getWidthHeight(self):
        """Gets the width and height of the actual map"""
        self.mapWidth, self.mapHeight = self.world.getWidthHeight()
        return self.mapWidth, self.mapHeight

    def getCellBiome(self, x, y):
        """Gets the biome of the cell"""
        biome = self.world.getBiome(x,y)
        return biome

    def getCellData(self, x, y):
        """Gets the biome and the unit of the cell"""
        return self.world.getCellData(x, y)

    def assignNewUnitCell(self, x, y, type):
        """Assigns a new unit to a cell"""
        self.world.assignNewUnit(x, y, type, self.resources)
        self.getAndAssignUnit(x, y)
        self.actualUnit.restartActions()
        self.setUnitMenu(str(self.actualUnit))

    def assignNewCityCell(self, x, y, type):
        """Assigns a new city to a cell"""
        self.world.assignNewStructure(x, y, type, self.resources)
        self.getAndAssignUnit(x, y)
        self.setCityMenu(str(self.actualCity))

    def reassignUnitCell(self, posX, posY, newPosX, newPosY):
        """reassign a unit from one cell to other"""
        self.world.reassignUnit(posX, posY, newPosX, newPosY)

    def moveUnit(self, x, y):
        """Checks if a unit can move and if so it does"""
        if self.actualUnit != None:
            posX, posY = self.actualUnit.getPosition()
            if self.actualUnit.getMovement() > 0:
                if self.movementPossible(posX + x, posY + y):
                    self.actualUnit.reduceMovement()
                    self.actualUnit.setRest(False)
                    self.reassignUnitCell(posX, posY, posX + x, posY + y)
                    self.hideMap()
                    self.revealMap()
                    self.mapNeedsRedraw = True

    def getAndAssignUnit(self, x, y):
        """Gets the unit of a cell and assign it as the active unit"""
        unit = self.world.getUnit(x, y)
        if unit != None:
            try:
                unit.getRoute()
                self.actualUnit = unit
                self.setUnitMenu(str(self.actualUnit))
            except:
                self.actualCity = unit
                self.setCityMenu(str(self.actualCity))

    def startUnitGeneration(self):
        """Selects a random position on the map"""
        while True:
            posX = random.randrange(0, self.mapWidth)
            posY = random.randrange(0, self.mapHeight)
            posX1 = None
            posY1 = None
            posX2 = None
            posY2 = None
            if self.movementPossible(posX, posY):
                for x in range(posX - 1, posX + 2):
                    for y in range(posY - 1, posY + 2):
                        if self.movementPossible(x, y):
                            if (posX, posY) != (x, y):
                                if posX1 == None:
                                    posX1, posY1 = x, y
                                elif posX2 == None:
                                    posX2, posY2 = x, y
                                    break
                    if posX1 != None and posX2 != None:
                        break
                if posX1 != None and posX2 != None:
                    break


        self.assignNewUnitCell(posX, posY, "FD")
        self.assignNewUnitCell(posX1, posY1, "EX")
        self.assignNewUnitCell(posX2, posY2, "WR")

    def movementPossible(self, x, y):
        """Checks if it is possible to move to the cell"""
        try:
            biome, unit = self.getCellData(x, y)
            if biome == "D" and unit == None and x >= 0 and y >= 0:
                return True
            else:
                return False
        except:
            return False

    def getMapRedraw(self):
        """Return if the map needs to redraw or not"""
        if self.mapNeedsRedraw:
            self.mapNeedsRedraw = False
            return True
        else:
            return False

    def hideMap(self):
        """Hide the map"""
        self.world.hideAllCells()

    def revealMap(self):
        """Reveal the part of the map seen by all the units"""
        self.world.revealMap()

    def getCellVisibility(self, x, y):
        """Gets if a cell was revealed and if it is actually being seen"""
        return self.world.getCellVisibility(x, y)

    def getPositionUnit(self):
        return self.actualUnit.getPosition()

    def restartAllUnitActions(self):
        """Restarts the movement of all the units"""
        self.world.restartAllUnitActions()   

    def setUnitMovement(self, posX, posY):
        """Sets the position to move of the unit selected"""
        self.actualUnit.setPostionToMove(posX, posY)

    def moveUnits(self):
        """Gets the position and routes of units and moves them"""
        actualUnit = self.actualUnit
        units = self.world.getAllUnits()

        for unit in units:   

            self.actualUnit = unit
            routes = unit.getRoute()
            routesReverted = []

            #Reverts the list
            for x in range(1, len(routes) + 1):
                routesReverted.append(routes[-x])
            routes = routesReverted

            if routes != None:
                for route in routes:
                    posX, posY = unit.getPosition()
                    if self.actualUnit.getMovement() > 0:                        
                        posToMoveX, posToMoveY = route
                        self.moveUnit(posToMoveX - posX, posToMoveY - posY)
                        if route == self.actualUnit.getPositionToMove(): # Checks if the actual route is the final position
                            self.setPositionToMoveUnit(None, None)
                    else:
                        break
        self.actualUnit = actualUnit

    def setPositionToMoveUnit(self, posX, posY):
        """Sets the position to move of the unit"""
        if self.actualUnit != None:            
            self.actualUnit.setPostionToMove(posX, posY)

    def getUnitMenu(self):
        """Gets the string of the actual unit"""
        return self.unitMenu

    def getCityMenu(self):
        """Gets the string of the actual unit"""
        return self.cityMenu

    def setUnitMenu(self, value):
        """Sets the value of the unitMenu"""
        self.unitMenu = value

    def setCityMenu(self, value):
        """Sets the value of the cityMenu"""
        self.cityMenu = value

    def getUnitHealth(self, unit):
        """Gets the health of the unit"""
        return unit.getHealthData()

    def attackUnit(self, x, y):
        """Attacks if the cell selected has an enemy unit"""
        biome, unit = self.getCellData(x, y)
        if self.actualUnit != None:
            if unit != None:
                if unit != self.actualUnit:
                    if self.actualUnit.getActionPosible():
                        x1, y1 = self.actualUnit.getPosition()
                        x2, y2 = unit.getPosition()

                        #Checks if the attack is a distance or melee attack
                        if abs(x1 - x2) > 1 and abs(x1 - x2) <= self.actualUnit.getAttackRange() and abs(y1 - y2) > 1 and abs(y1 - y2) <= self.actualUnit.getAttackRange(): 
                            self.actualUnit.setRest(False)
                            self.actualUnit.rangeAttack(unit)
                            life, maxLife = self.actualUnit.getHealthData()

                            if life <= 0: #Checks if the unit attacking died
                                self.actualUnit = None
                        
                            self.world.checkDeaths()

                        elif abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
                            self.actualUnit.setRest(False)
                            self.actualUnit.meleeAttack(unit)
                            life, maxLife = self.actualUnit.getHealthData()

                            if life <= 0: #Checks if the actual unit died
                                self.actualUnit = None
                            
                            self.world.checkDeaths()
            
            self.attack = False

    def constructOrRepair(self, x, y):
        """Constructs or repair a building from a cell"""
        if self.actualUnit.getActionPosible():
            biome, unit = self.getCellData(x, y)
            x1, y1 = self.actualUnit.getPosition()
            if abs(x - x1) <= 1 and abs(y - y1) <= 1:
                if unit != None:
                    try:
                        unit.getRepaired() #If it is a structure, it will repair it 
                        self.actualUnit.setActionPosible(False)                   
                    except:
                        pass
                elif str(biome) != "D" and str(biome) != "M":
                    gold, wood = self.world.getStructureCost(self.biomeToStructure[str(biome)])
                    if self.resources.getGold() >= gold and self.resources.getWood() >= wood:
                        self.resources.modifyGold(-gold)
                        self.resources.modifyWood(-wood)
                        self.assignNewCityCell(x, y, self.biomeToStructure[str(biome)])
                        self.actualUnit.setActionPosible(False)
                        self.hideMap()
                        self.revealMap()

    def cellSelected(self, x, y):
        """Executes a method depending if an event is active or not"""
        if self.attack:
            self.attackUnit(x, y)
            self.attack = False
            self.mapNeedsRedraw = True
        elif self.construct:
            self.constructOrRepair(x, y)
            self.construct = False
            self.mapNeedsRedraw = True
        else:
            self.getAndAssignUnit(x, y)

    def unitRest(self):
        """Sets that the unit is resting"""
        if self.actualUnit != None:
            if self.actualUnit.getActionPosible():
                self.actualUnit.unitResting() 

    def foundCity(self):
        """Erase the founder unit and creates a city"""
        self.world.removeUnit(self.actualUnit)
        posX, posY = self.actualUnit.getPosition()
        self.actualUnit = None
        self.assignNewCityCell(posX, posY, "CT")
        self.world.revealMap()
        self.mapNeedsRedraw = True

    def getAllUnitsAndCosts(self):
        """Get all posible units to create in the game and returns them with its respective cost of creation"""
        return self.world.getAllUnitsInformation()

    def assignUnitCreation(self, unit, time, gold, silver):
        """Tells the city to create an unit"""
        if self.resources.getGold() >= gold:
            if self.resources.getSilver() >= silver:
                self.resources.modifyGold(-gold)
                self.resources.modifySilver(-silver)
                self.actualCity.addUnitProduction(unit, time)
                self.actualCity.assignNewUnit()

    def passTurn(self):
        """All that happens when the turn passes is here"""
        self.world.checkProductionFinished()
        self.world.modifyResources()
        if self.resources.getFood() == 0:
            if self.resources.getHunger() == 5:
                self.actualUnit = None
                self.world.killAllUnits()
                self.resources.removeCounters()
                self.hideMap()
                self.revealMap()
            self.resources.addCounter()
        else:
            self.resources.removeCounters()
        self.world.setAllUnitsRoute()
        self.moveUnits()
        self.world.healUnits()
        self.restartAllUnitActions()
        self.mapNeedsRedraw = True

    def getResources(self):
        """Gets all the resources"""
        return self.resources.getGold(), self.resources.getSilver(), self.resources.getWood(), self.resources.getFood()
from cell import Cell
from character import Character

class Board():

    def __init__(self):
        """El inicio de la clase, se crean las variables que pertenecen
           a la misma"""
        self.cells = []
        self.units = []

    def addCellAndBiome(self, x, y, biome):
        """Añade un objeto Cell a la lista correspondiente y le establece el bioma"""
        self.cells[x].append(Cell())
        self.cells[x][y].setBiome(biome)
    
    def assignSize(self, width):
        """Asigna el tamaño del tablero segun el tamaño del mapa"""
        for x in range(width):
            self.cells.append([])

    def checkBiome(self, posX, posY):
        """Consulta y devuelve el bioma de la celda a consultar"""
        return self.cells[posX][posY].readBiome()

    def hideAllCells(self):
        """Hace que la visibilidad de todas las cells sea falsa"""
        for x in range(len(self.cells)):
            for y in range(len(self.cells[0])):
                self.cells[x][y].hideCell()
    
    def revealCell(self, posX, posY):
        """Cambia la visibilidad de la celda especificada a True"""
        self.cells[posX][posY].showCell()
    
    def getVisibility(self, posX, posY):
        """Consulta a la celda si esta visible o no"""
        return self.cells[posX][posY].getVisibility()

    def getUnit(self, posX, posY):
        return self.cells[posX][posY].getUnit()

    def createUnit(self, posX, posY):
        unit = Character()
        self.cells[posX][posY].setUnit(unit)
        unit.setPosition(posX, posY)
        self.units.append(unit)

    def getListUnits(self):
        return self.units

    def assignUnitCell(self, posX, posY, unit):
        self.cells[posX][posY].setUnit(unit)

    def removeUnitCell(self, posX, posY):
        self.cells[posX][posY].removeUnit()


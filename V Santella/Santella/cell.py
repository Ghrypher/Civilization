import random, pygame

class Cell:
    """ clase Celda almacena barcos o no """

    def __init__(self):
        """ constructor de la clase """
        self.biome = ""
        self.busy = False
        self.occupant = None
        self.revealed = False
        self.visible = False
        self.unit = None
        self.tile = None

    def set_biome(self, biome):
        """ establece el bioma de la celda """
        self.biome = str(biome)

    def get_biome(self):
        return self.biome

    def erase_biome(self):
        """ borra el bioma actual de la celda """
        if self.biome != "":
            self.biome = ""

    def getUnit(self):
        return self.unit

    def setUnit(self, unit):
        self.unit = unit
    
    def setUnitPosition(self,posX, posY):
        self.unit.setPosition(posX, posY)
    
    def getVisibility(self):
        return self.visible, self.revealed
    
    def showCell(self):
        self.visible = True
        self.revealed = True
    
    def cellOff(self):
        self.visible = False
import random, pygame

class Cell:
    """ clase Celda almacena barcos o no """

    def __init__(self):
        """ constructor de la clase """
        self.biome = ""
        self.busy = False
        self.occupant = None
        self.revealed = False
        self.active = False
        self.plants = ""
        self.unit = None
        self.tile = None

    def set_biome(self, biome):
        """ establece el bioma de la celda """
        self.biome = str(biome)

    def getBiome(self):
        return self.biome

    def erase_biome(self):
        """ borra el bioma actual de la celda """
        if self.biome != "":
            self.biome = ""

    def set_plants(self, plants):
        """ establece uan planta en la celda """
        self.plants = str(plants)

    def erase_plants(self):
        """ borra el bioma actual de la celda """
        if self.plants != "":
            self.plants = ""
    
    def free_cell(self):
        """ revisa si hay una algo/alguien en la celda """
        if self.plants == "" and self.busy == False:
            return True
        else:
            return False

    def reveal(self):
        """ revela la celda """
        img = pygame.image.load('asets/floor/' + str(self.biome) + '.png').convert()
        self.tile = img
        self.tile.set_colorkey((0, 0, 0))
        return img
    
    def hide(self):
        """ esconde la celda """
        self.tile = []
        self.tile.set_colorkey((0, 0, 0))

    def set_coordinates(self, x, y):
        """ establece las coordenadas de la celda """

    def get_coordinates(self):
        """ devuelve las coordenadas de la celda """
        coordenates = str(self.position_x) + " " + str(self.position_y)
        return coordenates

    def getUnit(self):
        return self.unit

    def setUnit(self, unit):
        self.unit = unit
    
    def setUnitPosition(self,posX, posY):
        self.unit.setPosition(posX, posY)
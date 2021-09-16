import random

class Cell:
    """ clase Celda almacena barcos o no """

    def __init__(self):
        """ constructor de la clase """
        self.biome = ""
        self.busy = False
        self.occupant = None
        self.revealed = False
        self.plants = ""
        self.tile = []

    def set_biome(self, biome):
        self.biome = str(biome)

    def erase_biome(self):
        if self.biome != "":
            self.biome = ""

    def set_plants(self, plants):
        self.plants = str(plants)

    def erase_plants(self):
        if self.plants != "":
            self.plants = ""
    
    def free_cell(self):
        """ revisa si hay una barco en la celda """
        if self.plants == "" and self.busy == False:
            return True
        else:
            return False

    def reveal(self):
        self.tile = pygame.image.load('asets/floor/' + str(self.biome) + '.png').convert()
        self.tile.set_colorkey((0, 0, 0))
    
    def hide(self):
        self.tile = []
        self.tile.set_colorkey((0, 0, 0))


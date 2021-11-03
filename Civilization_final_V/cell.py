import pygame
import random

class Cell():

    def __init__(self):
        """Function __init__"""
        self.biome = ""
        self.space = True
        self.occupant = None
        self.revealed = False
        self.visible = False
        self.plants = ""
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
    
    def free_cell(self):
        """ revisa si hay una algo/alguien en la celda """
        if self.plants == "" and self.busy == False:
            return True
        else:
            return False

    def reveal(self):
        """ revela la celda """
        img = pygame.image.load('assets/floor/' + str(self.biome) + '.png').convert()
        self.tile = img
        self.tile.set_colorkey((0, 0, 0))
        return img
    
    def hide(self):
        """ esconde la celda """
        self.tile = []
        self.tile.set_colorkey((0, 0, 0))
    
    def getVisibility(self):
        return self.visible, self.revealed
    
    def showCell(self):
        self.visible = True
        self.revealed = True
    
    def cellOff(self):
        self.visible = False

    def checkSpace(self):
        """  """
        return self.space
    
    def useSpace(self):
        """  """
        self.sapce = False
    
    def freeSpace(self):
        """  """
        self.sapce = True

import pygame
import random

class Cell():

    def __init__(self):
        """Function __init__"""
        self.biome = ""
        self.busy = False
        self.occupant = False
        self.revealed = False
        self.visible = False
        self.plants = ""
        self.tile = None

    def setBiome(self, biome):
        """ establece el bioma de la celda """
        self.biome = str(biome)

    def getBiome(self):
        return self.biome

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
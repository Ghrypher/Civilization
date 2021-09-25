import pygame
import random

class Cell():

    """Function __init__"""
    def __init__(self):
        self.biome = ""
        self.busy = False
        self.occupant = None
        self.revealed = False
        self.plants = ""
        self.tile = None
        self.positionx = int
        self.positiony = int

    """Function setBiome, establishes the biome from the cell"""
    def setBiome(self,biome):
        self.biome = str(biome)

    """Function eraseBiome, deletes the biome from the cell"""
    def eraseBiome(self):
        if self.biome != "":
            self.biome = ""
    
    """Function setPlants, adds a plant to the cell"""
    def setPlants(self,plants):
        self.plants = str(plants)

    """Function erasePlants, deletes a plant from the cell"""
    def erasePlants(self):
        if self.plants != "":
            self.plants = ""

    """Function freeCell, control if the cell is empty"""
    def freeCell(self):
        if self.plants == "" and self.busy == False:
            return True
        else:
            return False
    
    """Function revealCell, reveales the cell"""
    def revealCell(self):
        img = pygame.image.load('resources/icons/map/floor/' + str(self.biome) + '.png').convert()
        self.tile = img
        self.tile.set_colorkey((0, 0, 0))
        return img

    """Function hidesCell, hides the cell"""
    def hideCell(self):
        self.tile = []
        self.tile.set_colorkey((0, 0, 0))
    
    """Function setCellCoordinates, says his position to the cell"""
    def setCellCoordinates(self,x,y):
        self.positionx = x
        self.positiony = y
    
    """Function getCellCoordinates, returns the position of the cell"""
    def getCellCoordinates(self):
        coordenates = str(self.positionx) + " " + str(self.positiony)
        return coordenates
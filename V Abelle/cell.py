import pygame
import random

class Cell():

    """Function __init__"""
    def __init__(self):
        self.occupant = None
        self.visible = False
        self.biome = None
        self.busy = False
        self.revealed = False
        self.active = False
        self.plants = ""
        self.tile = None
        self.position_x = int
        self.position_y = int

    """Function setBiome, establishes the biome from the cell"""
    def setBiome(self,biome):
        self.biome = str(biome)

    """Function eraseBiome, deletes the actual biome from the cell"""
    def eraseBiome(self):
        if self.biome != "":
            self.biome = ""

    """Function readBiome, returns what biome contains the cell"""
    def getBiome(self):
        return self.biome

    """Function setPlants, puts a plant on the cell"""
    def setPlants(self,plants):
        self.plants = str(plants)

    """Function erasePlants, deletes the plant from the cell"""
    def erasePlants(self):
        if self.plants != "":
            self.plants = ""

    """Function freeCell, checks if the cell is empty"""
    def freeCell(self):
        if self.plants == "" and self.busy == False:
            return True
        else:
            return False
    
    """Function revealCell, reveals the cell"""
    def revealCell(self):
        img = pygame.image.load('asets/floor/' + str(self.biome) + '.png').convert()
        self.tile = img
        self.tile.set_colorkey((0, 0, 0))
        return img

    """Function hideCell, hides the cell"""
    def hideCell(self):
        self.tile = []
        self.tile.set_colorkey((0, 0, 0))

    """Function setCoordinates, establishes the cell coordinates"""
    def setCoordinates(self,x,y):
        self.position_x = x
        self.position_y = y

    """Function getCoordinates, returns the cell coordinates"""
    def getCoordinates(self):
        coordenates = str(self.position_x) + " " + str(self.position_y)
        return coordenates
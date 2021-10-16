import pygame
import random

class Cell():

    def __init__(self):
        """Function __init__"""
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

    def setBiome(self,biome):
        """Function setBiome, establishes the biome from the cell"""
        self.biome = str(biome)

    def eraseBiome(self):
        """Function eraseBiome, deletes the actual biome from the cell"""
        if self.biome != "":
            self.biome = ""

    def getBiome(self):
        """Function readBiome, returns what biome contains the cell"""
        return self.biome

    def setPlants(self,plants):
        """Function setPlants, puts a plant on the cell"""
        self.plants = str(plants)

    def erasePlants(self):
        """Function erasePlants, deletes the plant from the cell"""
        if self.plants != "":
            self.plants = ""

    def freeCell(self):
        """Function freeCell, checks if the cell is empty"""
        if self.plants == "" and self.busy == False:
            return True
        else:
            return False
    
    def revealCell(self):
        """Function revealCell, reveals the cell"""
        img = pygame.image.load('asets/floor/' + str(self.biome) + '.png').convert()
        self.tile = img
        self.tile.set_colorkey((0, 0, 0))
        return img

    def hideCell(self):
        """Function hideCell, hides the cell"""
        self.tile = []
        self.tile.set_colorkey((0, 0, 0))

    def setCoordinates(self,x,y):
        """Function setCoordinates, establishes the cell coordinates"""
        self.position_x = x
        self.position_y = y

    def getCoordinates(self):
        """Function getCoordinates, returns the cell coordinates"""
        coordenates = str(self.position_x) + " " + str(self.position_y)
        return coordenates
import pygame
import random

class Cell():

    """Function __init__"""
    def __init__(self):
        self.troop = None
        self.biome = None

    """Function setBiome, establishes the biome from the cell"""
    def setBiome(self,biome):
        self.biome = str(biome)

    """Function readBiome, returns what biome contains the cell"""
    def readBiome(self):
        return self.biome
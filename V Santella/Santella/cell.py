import pygame


import pygame
import random

class Cell:
    """ clase Celda almacena barcos o no """

    def __init__(self):
        """ constructor de la clase """
        self.biome = ""
        self.busy = False
        self.occupant = None
        self.active = False
        self.plants = ""
        self.tile = None
        self.position_x = int
        self.position_y = int

    def set_biome(self, biome):
        """ establece el bioma de la celda """
        self.biome = str(biome)

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
        """ le indica sus coordenadas a la celda """
        self.position_x = x
        self.position_y = y

    def get_coordinates(self):
        """ devuelve las coordenadas de la celda """
        coordenates = str(self.position_x) + " " + str(self.position_y)
        return coordenates

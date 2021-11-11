import pygame, sys
from pygame.locals import *
"""-----------------------------------------------------------------------------"""
import random, math,os
from world import World
"""-----------------------------------------------------------------------------"""
import pygame
from pygame.locals import *

class Controller():

    def __init__(self):
        """Loads the variables and execute the methods when the class is created"""
        self.view = View()
        self.model = Model()
        self.view.setModel(self.model)
        self.model.Read_Map("Maps/map2.txt")
        self.view.setMapSize()
        self.loopGame()
    
    def loopGame(self):
        """Loop of the game which gets the inputs of the user"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #If the user presses the X at the top right
                    self.terminate()
                
            self.view.updateScreen()

    def terminate(self):
        """End the program"""
        pygame.quit()
        sys.exit()
    

class View():

    def __init__(self):
        """Loads the variables and execute the methods when the class is created"""
        self.model = None

        self.screenWidth = 1280
        self.screenHeight = 704
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))

        self.mapWidth = None 
        self.mapHeight = None

    def setModel(self, model):
        """Sets the same model that uses the controller"""
        self.model = model
    
    def setMapSize(self):
        """Sets the map width and height"""
        self.mapWidth, self.mapHeight = self.model.getWidthHeight()

    def updateScreen(self):        
        pygame.display.update()

class Model():

    def __init__(self):
        """Loads the variables and execute the methods when the class is created"""
        self.world = World()

    def Read_Map (self, file):
        """Reads a txt file with the map"""
        assert os.path.exists(file), 'Cannot find the level file: %s' % (file)
        M_File = open(file, "r")
        content = M_File.readlines() + ["\r\n"]
        M_File.close()

        M_TextLines = []
        M_Obj = []

        for lineNum in range(len(content)):
            line = content[lineNum].rstrip('\r\n')

            # Si encuentra un ";" en la linea actual devuelve ""
            if ";" in line:
                line = line[:line.find(";")]

            # Si tiene algo lo añade a la lista con las lineas de texto del mapa
            if line != "":
                M_TextLines.append(line)

            elif line == "" and len(M_TextLines) > 0:
                maxWidth = -1

                # Busca la fila mas larga de todas
                for i in range(len(M_TextLines)):
                    if len(M_TextLines[i]) > maxWidth:
                        maxWidth = len(M_TextLines[i])

                # Las empareja llenando con espacios si es que hace falta
                for i in range (len(M_TextLines)):
                    M_TextLines[i] += " " * (maxWidth - len(M_TextLines[i]))

                # Añade una lista por cada linea de mapa
                for x in range (len(M_TextLines[0])):
                    M_Obj.append([])

                # Invierte el mapa para que quede al derecho en la matriz
                for y in range (len(M_TextLines)):
                    for x in range (maxWidth):
                        M_Obj[x].append(M_TextLines[y][x])
                
        self.createBoard(M_Obj)

    def createBoard(self, M_Obj):
        """Crea el tablero de la clase board y le asigna el bioma a cada celda"""

        self.world.assignSize(len(M_Obj))

        for x in range(len(M_Obj)):
            for y in range(len(M_Obj[0])):
                self.world.addCellAndBiome(x, y, M_Obj[x][y])

    def getWidthHeight(self):
        """Gets the width and height of the actual map"""
        return self.world.getWidthHeight()


if __name__ == "__main__":
    game = Controller()
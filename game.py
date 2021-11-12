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
        self.model.readMap("Maps/map1.txt")
        self.view.setMapSize()
        self.view.drawMap()
        self.loopGame()
    
    def loopGame(self):
        """Loop of the game which gets the inputs of the user"""
        camUp = False
        camDown = False
        camRight = False
        camLeft = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #If the user presses the X at the top right
                    self.terminate()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        camUp = True
                    if event.key == K_DOWN:
                        camDown = True
                    if event.key == K_RIGHT:
                        camRight = True
                    if event.key == K_LEFT:
                        camLeft = True
                if event.type == KEYUP:
                    if event.key == K_UP:
                        camUp = False
                    if event.key == K_DOWN:
                        camDown = False
                    if event.key == K_RIGHT:
                        camRight = False
                    if event.key == K_LEFT:
                        camLeft = False
            if camUp:
                self.view.moveCamera("U")
            if camDown:
                self.view.moveCamera("D")
            if camRight:
                self.view.moveCamera("R")
            if camLeft:
                self.view.moveCamera("L")
                
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
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight)) #Creates the screen where the game will display

        #Store the width and height fo the map
        self.mapWidth = None 
        self.mapHeight = None

        #Store the width and height of the cells
        self.tileWidth = 32
        self.tileHeight = 32

        self.mapSurf = None

        self.textToMap = {"B" : pygame.image.load("asets/floor/Barrier.png"),
                            "D" : pygame.image.load("asets/floor/Dirt.png"),
                            "F" : pygame.image.load("asets/floor/Forest.png"),
                            "W" :pygame.image.load("asets/floor/Water.png"),
                            "M" : pygame.image.load("asets/floor/Mountain.png"),
                            "I" : pygame.image.load("asets/floor/Iron_Mountain.png"),
                            "G" : pygame.image.load("asets/floor/Gold_Mountain.png"),
                            "R" : "Revealed",
                            "H" : "Hidden",
                            "0" : False,
                            "1" : True}

        #Sets the limit for the camera to move
        self.maxCamMoveX = None
        self.maxCamMoveY = None

        #Stores how much the camera move fron the center
        self.cameraMoveX = 0
        self.cameraMoveY = 0    

        self.cameraVelocity = 5 #Sets the velocity of the camera movement    

    def setModel(self, model):
        """Sets the same model that uses the controller"""
        self.model = model
    
    def setMapSize(self):
        """Sets the map width, height and all the variables which need this information"""
        self.mapWidth, self.mapHeight = self.model.getWidthHeight()
        
        self.mapSurf = pygame.Surface((self.mapWidth * self.tileWidth, self.mapHeight * self.tileHeight)) #Creates a surface for the map
        
        self.maxCamMoveX = abs(self.screenWidth / 2 - self.mapWidth * self.tileWidth / 2)
        self.maxCamMoveY = abs(self.screenHeight / 2 - self.mapHeight * self.tileHeight / 2)

    def drawMap(self):
        """Draws the map on a surface"""
        for x in range(self.mapWidth):
            for y in range(self.mapHeight):
                #Gets the biome of the cell and draw it on the surface
                baseTile = self.textToMap[self.model.getCellBiome(x, y)]
                tileRect = pygame.Rect(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight)
                self.mapSurf.blit(baseTile, tileRect)

    def moveCamera(self, cameraDirection):
        """Moves the camera and checks if it can move also"""
        if cameraDirection == "U" and self.cameraMoveY < self.maxCamMoveY:
            self.cameraMoveY += self.cameraVelocity
        if cameraDirection == "D" and self.cameraMoveY > -self.maxCamMoveY:
            self.cameraMoveY -= self.cameraVelocity
        if cameraDirection == "L" and self.cameraMoveX < self.maxCamMoveX:
            self.cameraMoveX += self.cameraVelocity
        if cameraDirection == "R" and self.cameraMoveX > -self.maxCamMoveX:
            self.cameraMoveX -= self.cameraVelocity

    def updateScreen(self):
        self.screen.fill((0,0,0))
        mapSurfRect = self.mapSurf.get_rect(center = (self.screenWidth/2 + self.cameraMoveX, self.screenHeight/2 + self.cameraMoveY))  
        self.screen.blit(self.mapSurf, mapSurfRect)      
        pygame.display.update()

class Model():

    def __init__(self):
        """Loads the variables and execute the methods when the class is created"""
        self.world = World()

    def readMap (self, file):
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

    def getCellBiome(self, x, y):
        """Gets the biome of the cell"""
        biome = self.world.getBiome(x,y)
        return biome

if __name__ == "__main__":
    game = Controller()
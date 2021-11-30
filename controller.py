import pygame, sys
from pygame.locals import *
from view import View
from model import Model

class Controller():

    def __init__(self):
        """Starts the class and executes what is inside"""
        self.view = View()
        self.model = Model()
        self.view.setModel(self.model)
        self.loopMenu()

    def loopMenu(self):
        """Loops the menu and gets all the events of the user"""
        while True:
            mousePressed = False
            for event in pygame.event.get():
                if event.type == QUIT: # If the X pressed then finish the program
                    self.terminate()
                if event.type == MOUSEBUTTONDOWN: # Checks if the mouse was pressed
                    mousePressed = True
                if event.type == KEYDOWN: # Records the keys pressed
                    if event.key == K_ESCAPE:
                        self.view.goBack()                        

            mousePos = pygame.mouse.get_pos() #Gets the position in pixels of the mouse    
            map = self.view.checkCollition(mousePos, mousePressed)
            if map != None:
                break
            self.view.updateScreen(mousePos)
        self.loopGame(map)
    
    def loopGame(self, map):
        """Loop of the game which gets the inputs of the user"""
        if map == "maps/random_world.txt":
            self.model.randomMap(100, 80)
        self.model.readMap(map)
        self.view.setMapSize()
        self.model.startUnitGeneration()
        self.model.revealMap()
        self.view.drawMap()
        self.view.centerLoadCamera()
        camUp = False
        camDown = False
        camRight = False
        camLeft = False
        mousePos = (0, 0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #If the user presses the X at the top right
                    self.terminate()

                mousePos = pygame.mouse.get_pos()

                if event.type == KEYDOWN:
                    #When the arrows are pressed
                    if event.key == K_UP:
                        camUp = True
                    if event.key == K_DOWN:
                        camDown = True
                    if event.key == K_RIGHT:
                        camRight = True
                    if event.key == K_LEFT:
                        camLeft = True

                    #When the enter is pressed 
                    if event.key == K_RETURN:
                        self.model.passTurn()
                        self.view.mapNeedsRedraw()

                    #When the leters w,a,s,d are pressed
                    if event.key == K_w:
                        self.model.moveUnit(0, -1)
                        self.model.setPositionToMoveUnit(None, None)
                        self.view.mapNeedsRedraw()
                    if event.key == K_s:
                        self.model.moveUnit(0, 1)
                        self.model.setPositionToMoveUnit(None, None)
                        self.view.mapNeedsRedraw()
                    if event.key == K_a:
                        self.model.moveUnit(-1, 0)
                        self.model.setPositionToMoveUnit(None, None)
                        self.view.mapNeedsRedraw()
                    if event.key == K_d:
                        self.model.moveUnit(1, 0)
                        self.model.setPositionToMoveUnit(None, None)
                        self.view.mapNeedsRedraw()

                #When the arrows stopped being pressed
                if event.type == KEYUP:
                    if event.key == K_UP:
                        camUp = False
                    if event.key == K_DOWN:
                        camDown = False
                    if event.key == K_RIGHT:
                        camRight = False
                    if event.key == K_LEFT:
                        camLeft = False

                #When the mouse is clicked
                if event.type == MOUSEBUTTONDOWN:
                    posX, posY = self.view.getMouseMapPos(mousePos)
                    if pygame.mouse.get_pressed()[0]: # Left click
                        if not self.view.drawUnitActions(mousePos, True):
                            self.model.cellSelected(posX, posY)
                        self.view.mapNeedsRedraw()
                    if pygame.mouse.get_pressed()[2]: # Right click
                        self.model.setPositionToMoveUnit(posX, posY)
                        

            if camUp:
                self.view.moveCamera("U")
            if camDown:
                self.view.moveCamera("D")
            if camRight:
                self.view.moveCamera("R")
            if camLeft:
                self.view.moveCamera("L")
                
            self.view.updateGame(mousePos)

    def terminate(self):
        """End the program"""
        pygame.quit()
        sys.exit()     

if __name__ == "__main__":
    game = Controller()
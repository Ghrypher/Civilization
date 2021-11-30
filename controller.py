import pygame
from pygame.locals import *
from view import View

class Controller():

    def __init__(self):
        self.view = View()
        self.loopMenu()

    def loopMenu(self):
        """Loops the menu and gets all the events of the user"""
        while True:
            mousePressed = False
            for event in pygame.event.get():
                if event.type == QUIT: # If the X pressed then finish the program
                    self.view.terminate()
                if event.type == MOUSEBUTTONDOWN: # Checks if the mouse was pressed
                    mousePressed = True
                if event.type == KEYDOWN: # Records the keys pressed
                    if event.key == K_ESCAPE:
                        self.view.goBack()                        

            mousePos = pygame.mouse.get_pos() #Gets the position in pixels of the mouse    
            self.view.checkCollition(mousePos, mousePressed)
            self.view.updateScreen(mousePos)  

if __name__ == "__main__":
    game = Controller()
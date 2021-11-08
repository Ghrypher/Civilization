import pygame, sys
from pygame.locals import *

class Menu():

    def __init__(self):
        """The variables of the class are created and all the function in are executed when the class is created"""
        self.screen = pygame.display.set_mode((800,600)) # Creates a screen of 800 x 600
        self.font = "resources/fonts/Enchanted_Land.otf" # Saves de direction of the file with de font

        self.loadIconAndCaption()
        self.loadMenuStart()
        self.loopMenu()
        
    def loadIconAndCaption(self):
        """Loads and set de title of the window and the icon at the top left of the window"""
        pygame.display.set_caption("T-H-E")
        icon = pygame.image.load("resources/assets/menu/windowicon.png")
        pygame.display.set_icon(icon)
    
    def loopMenu(self):
        """Loops the menu and gets all the events of the user"""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT: # If the X pressed then finish the program
                    self.terminate()

            pygame.display.update()

    def loadMenuStart(self):
        """Load the elements of the menu"""
        background = pygame.image.load("resources/assets/menu/defaultback.jpg")
        self.screen.blit(background, (0,0))

    def loadMouseIcon(self):
        """"""

    def terminate(self):
        """Finish the program"""
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    menu = Menu()
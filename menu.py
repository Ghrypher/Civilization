import pygame, sys
from pygame.locals import *

class Menu():

    def __init__(self):
        """The variables of the class are created and all the function in are executed when the class is created"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1280,704)) # Creates a screen of 1280 x 704
        self.menuSUrf = pygame.Surface((1280,704))
        self.font = "resources/fonts/Enchanted_Land.otf" # Saves the location of the file with the font

        pygame.mouse.set_visible(False)
        
        self.buttonRect1 = None
        self.buttonRect2 = None
        self.buttonRect3 = None

        self.loadIconAndCaption()
        self.loadMenuStart()
        self.loopMenu()
        
    def loadIconAndCaption(self):
        """Loads and set the title of the window and the icon at the top left of the window"""
        pygame.display.set_caption("T-H-E")
        icon = pygame.image.load("resources/assets/menu/windowicon.png")
        pygame.display.set_icon(icon)
    
    def loopMenu(self):
        """Loops the menu and gets all the events of the user"""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT: # If the X pressed then finish the program
                    self.terminate()

            mousePos = pygame.mouse.get_pos() #Gets the position in pixels of the mouse
            self.menuRect = self.menuSUrf.get_rect()
            
            self.screen.blit(self.menuSUrf, self.menuRect)
            self.loadMouseIcon(mousePos)

            pygame.display.update()

    def loadMenuStart(self):
        """Creates and load the elements of the start of the menu"""

        buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")
        buttonRect = buttonBackground.get_rect()

        # Loads and draws background
        background = pygame.image.load("resources/assets/menu/defaultback.jpg")
        self.menuSUrf.blit(background, (0,0))
    
        button1Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button1Rect = button1Surf.get_rect(center = (900,168))

        button1Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font, 100).render("Play", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect1 = button1Rect

        # Draws the text on the button and then draws the surface
        button1Surf.blit(buttonText, buttonTextRect)
        self.menuSUrf.blit(button1Surf, button1Rect)

        button2Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button2Rect = button2Surf.get_rect(center = (900,336))

        button2Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font, 100).render("Instructions", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect2 = button2Rect

        # Draws the text on the button and then draws the surface
        button2Surf.blit(buttonText, buttonTextRect)
        self.menuSUrf.blit(button2Surf, button2Rect)

        button3Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button3Rect = button3Surf.get_rect(center = (900,504))

        button3Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font, 100).render("Credits", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect3 = button3Rect

        # Draws the text on the button and then draws the surface
        button3Surf.blit(buttonText, buttonTextRect)
        self.menuSUrf.blit(button3Surf, button3Rect)


    def loadMouseIcon(self, mousePos):
        """Loads the mouse image constantly"""

        mouse = pygame.image.load("resources/assets/menu/defaultcursor.png")
        self.screen.blit(mouse, mousePos)

    def terminate(self):
        """Finish the program"""
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    menu = Menu()
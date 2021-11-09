import pygame, sys
from pygame.locals import *

class Menu():

    def __init__(self):
        """The variables of the class are created and all the function in are executed when the class is created"""
        pygame.init()

        self.screenWidth = 1280
        self.screenHeight = 704
        self.screen = pygame.display.set_mode((self.screenWidth,self.screenHeight)) # Creates a screen of 1280 x 704
        self.menuSurf = pygame.Surface((self.screenWidth,self.screenHeight))
        self.font = "resources/fonts/Enchanted_Land.otf" # Saves the location of the file with the font
        self.collition = False

        # Hides the cursor
        pygame.mouse.set_visible(False)
        
        # Saves the position and size of the buttons shown
        self.buttonRect1 = None
        self.buttonRect2 = None
        self.buttonRect3 = None

        # Dictionary which tells which is the menu that is actualy active
        self.actualMenuDict = {
            1 : self.loadMenuStart,
            2 : self.loadGameSelector,
            3 : self.loadCredits,
            4 : self.loadInstructions
        }
        self.actualMenu = 1

        self.loadMenuStart((0,0), False)
        self.loadIconAndCaption()
        self.loopMenu()
        
    def loadIconAndCaption(self):
        """Loads and set the title of the window and the icon at the top left of the window"""
        pygame.display.set_caption("T-H-E")
        icon = pygame.image.load("resources/assets/menu/windowicon.png")
        pygame.display.set_icon(icon)
    
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
                        self.goBack()                        

            mousePos = pygame.mouse.get_pos() #Gets the position in pixels of the mouse    
            self.checkCollition(mousePos, mousePressed)
            self.updateScreen(mousePos)        

    def loadMenuStart(self, mousePos, click):
        """Creates and load the elements of the start of the menu"""
        buttonPressed = False #Represents if one of the buttons was pressed or not

        buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")
        buttonRect = buttonBackground.get_rect()

        # Loads and draws background
        background = pygame.image.load("resources/assets/menu/defaultback.jpg")
        self.menuSurf.blit(background, (0,0))

        # Loads the logo of the game
        logo = pygame.image.load("resources/assets/menu/gamelogo.png")
        self.menuSurf.blit(logo, (30,90))

        button1Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button1Rect = button1Surf.get_rect(center = (900,168))

        if button1Rect.collidepoint(mousePos):
            buttonBackground = pygame.image.load("resources/assets/menu/buttonselector.png")
            if click == True:
                self.actualMenu = 2
                buttonPressed = True
        else:
            buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")

        button1Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font, 100).render("Play", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect1 = button1Rect

        # Draws the text on the button and then draws the surface
        button1Surf.blit(buttonText, buttonTextRect)
        self.menuSurf.blit(button1Surf, button1Rect)

        button2Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button2Rect = button2Surf.get_rect(center = (900,336))

        if button2Rect.collidepoint(mousePos):
            buttonBackground = pygame.image.load("resources/assets/menu/buttonselector.png")
            if click == True:
                self.actualMenu = 4
                buttonPressed = True
        else:
            buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")

        button2Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font, 100).render("Instructions", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect2 = button2Rect

        # Draws the text on the button and then draws the surface
        button2Surf.blit(buttonText, buttonTextRect)
        self.menuSurf.blit(button2Surf, button2Rect)

        button3Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button3Rect = button3Surf.get_rect(center = (900,504))

        if button3Rect.collidepoint(mousePos):
            buttonBackground = pygame.image.load("resources/assets/menu/buttonselector.png")
            if click == True:
                self.actualMenu = 3
                buttonPressed = True
        else:
            buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")

        button3Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font, 100).render("Credits", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect3 = button3Rect

        # Draws the text on the button and then draws the surface
        button3Surf.blit(buttonText, buttonTextRect)
        self.menuSurf.blit(button3Surf, button3Rect)
        if buttonPressed:
            self.collition = False
            self.loadActualMenu((0,0), False)

    def loadGameSelector(self, mousePos, click):
        """Creates and load the elements of the start of the menu"""

        buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")
        buttonRect = buttonBackground.get_rect()

        # Loads and draws background
        background = pygame.image.load("resources/assets/menu/defaultback.jpg")
        self.menuSurf.blit(background, (0,0))

        button1Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button1Rect = button1Surf.get_rect(center = (640,504))

        if button1Rect.collidepoint(mousePos):
            buttonBackground = pygame.image.load("resources/assets/menu/buttonselector.png")
        else:
            buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")

        button1Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font, 100).render("Pre-created Map", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect1 = button1Rect

        # Draws the text on the button and then draws the surface
        button1Surf.blit(buttonText, buttonTextRect)
        self.menuSurf.blit(button1Surf, button1Rect)

        button2Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button2Rect = button2Surf.get_rect(center = (640,200))

        if button2Rect.collidepoint(mousePos):
            buttonBackground = pygame.image.load("resources/assets/menu/buttonselector.png")
        else:
            buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")

        button2Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font, 100).render("Random Map", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect2 = button2Rect

        self.buttonRect3 = pygame.Rect(0,0,0,0)

        # Draws the text on the button and then draws the surface
        button2Surf.blit(buttonText, buttonTextRect)
        self.menuSurf.blit(button2Surf, button2Rect)
    
    def loadCredits(self, mousePos, click):
        """Creates and loads the screen of credits"""

        self.buttonRect1 = pygame.Rect(0,0,0,0)
        self.buttonRect2 = pygame.Rect(0,0,0,0)
        self.buttonRect3 = pygame.Rect(0,0,0,0)

        # Loads and draws background
        background = pygame.image.load("resources/assets/menu/defaultback.jpg")
        self.menuSurf.blit(background, (0,0))

        # Writes text on the screen
        text = pygame.font.Font(self.font, 100).render("Creditos", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (640, 100))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font, 60).render("Hecho por: Sangiago Abelle, Santella Agustin, Sanna Ian", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (640, 220))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font, 60).render("Desarrollador del menu: Santiago Abelle", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (640, 320))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font, 60).render("Desarrollador de la generacion del mapa: Sanna Ian", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (640, 420))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font, 60).render("Diseñador grafico: Santella Agustin", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (640, 520))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font, 70).render("Esperamos que hayas disfrutado de The Huergo Empires", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (640, 650))

        self.menuSurf.blit(text, textRect)

    def loadInstructions(self, mousePos, click):
        """Creates and loads the screen of Instructions"""

        self.buttonRect1 = pygame.Rect(0,0,0,0)
        self.buttonRect2 = pygame.Rect(0,0,0,0)
        self.buttonRect3 = pygame.Rect(0,0,0,0)

        # Loads and draws background
        background = pygame.image.load("resources/assets/menu/defaultback.jpg")
        self.menuSurf.blit(background, (0,0))

        # Writes text on the screen
        text = pygame.font.Font(self.font, 100).render("Instrucciones", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (640, 100))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font, 48).render("""1- Para ganar se debe vencer a todos los enemigos o completar una de las investigaciones en su totalidad""", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(midleft = (0, 220))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font, 48).render("2- Se pasa de turno utilizando la tecla enter", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(midleft = (0, 320))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font, 48).render("3- Solo se pueden mover las unidades e interactuar con las ciudades cierta cantidad de veces por turno", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(midleft = (0, 420))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font, 48).render("4- Las unidades necesitan comida y para construir se requiren materiales", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(midleft = (0, 520))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font, 48).render("5- Divertirse jugando", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(midleft = (0, 620))

        self.menuSurf.blit(text, textRect)

    def loadMouseIcon(self, mousePos):
        """Loads the mouse image"""

        mouse = pygame.image.load("resources/assets/menu/defaultcursor.png")
        self.screen.blit(mouse, mousePos)

    def terminate(self):
        """Finish the program"""
        pygame.quit()
        sys.exit()

    def updateScreen(self, mousePos):
        """Loads the menu with the cursor and updates the screen"""

        self.menuRect = self.menuSurf.get_rect()            
        self.screen.blit(self.menuSurf, self.menuRect)
        self.loadMouseIcon(mousePos)

        pygame.display.update()

    def checkCollition(self, mousePos, click):
        """Checks if the cursor is on any of the buttons of the actual menu"""
        if self.buttonRect1.collidepoint(mousePos) == True or self.buttonRect2.collidepoint(mousePos) == True or self.buttonRect3.collidepoint(mousePos) == True:
            if self.collition == False or click == True:
                self.collition = True
                self.loadActualMenu(mousePos, click)                    
        else:
            if self.collition == True:
                self.collition = False  
                self.loadActualMenu(mousePos, click)
                
    def loadActualMenu(self, mousePos, click):
        self.actualMenuDict[self.actualMenu](mousePos, click)

    def goBack(self):
        """Redirects to the menu before the actual one"""

        goBackDict = {
            2 : 1,
            3 : 1,
            4 : 1
        }
        try:
            self.actualMenu = goBackDict[self.actualMenu]
            self.collition = False
            self.loadActualMenu((0,0), False)
        except:
            """do nothing"""

if __name__ == "__main__":
    menu = Menu()
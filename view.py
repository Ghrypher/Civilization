import pygame, sys
from pygame.locals import *
import math

from pygame.transform import scale

class View():

    def __init__(self):
        """The variables of the class are created and all the function in are executed when the class is created"""
        pygame.init()

        self.screenWidth = 1280
        self.screenHeight = 704
        self.screen = pygame.display.set_mode((self.screenWidth,self.screenHeight),pygame.RESIZABLE) # Creates a screen of 1280 x 704
        self.menuSurf = pygame.Surface((self.screenWidth,self.screenHeight))
        self.font = "resources/fonts/Enchanted_Land.otf" # Saves the location of the file with the font
        self.collition = False
        self.resized = False
        self.scale = None

        # Hides the cursor
        pygame.mouse.set_visible(False)
        
        # Saves the position and size of the buttons shown
        self.buttonRect1 = None
        self.buttonRect2 = None
        self.buttonRect3 = None

        # Dictionary which tells which is the menu that is actualy active
        self.actualMenuDict = {
            0 : self.loadLogOut,
            1 : self.loadMenuStart,
            2 : self.loadGameSelector,
            3 : self.loadCredits,
            4 : self.loadInstructions
        }
        self.actualMenu = 1

        self.loadMenuStart((0,0), False)
        self.loadIconAndCaption()

        self.model = None

        #Store the width and height fo the map
        self.mapWidth = None 
        self.mapHeight = None

        #Store the width and height of the cells
        self.tileWidth = 32
        self.tileHeight = 32

        self.mapSurf = None
        self.mapRect = None

        #Gets the image of the cell from the string
        self.textToMap = {"B" : pygame.image.load("asets/floor/barrier.png"),
                            "D" : pygame.image.load("asets/floor/dirt.png"),
                            " D": pygame.image.load("asets/floor/dirt_inactive.png"),
                            "F" : pygame.image.load("asets/floor/forest.png"),
                            " F" : pygame.image.load("asets/floor/forest_inactive.png"),
                            "W" :pygame.image.load("asets/floor/water.png"),
                            " W" :pygame.image.load("asets/floor/water_inactive.png"),
                            "M" : pygame.image.load("asets/floor/mountain.png"),
                            " M" : pygame.image.load("asets/floor/mountain_inactive.png"),
                            "I" : pygame.image.load("asets/floor/iron_mountain.png"),
                            " I" : pygame.image.load("asets/floor/iron_mountain_inactive.png"),
                            "G" : pygame.image.load("asets/floor/gold_mountain.png"),
                            " G" : pygame.image.load("asets/floor/gold_mountain_inactive.png"),
                            "": pygame.image.load("asets/floor/off_world.png"),
                            "R" : "Revealed",
                            "H" : "Hidden",
                            "0" : False,
                            "1" : True}
        
        #Gets the image of the unit from the string
        self.textToUnit = {
            "WR" : pygame.image.load("asets/characters/red_warrior.png"),
            "FD" : pygame.image.load("asets/characters/red_founder.png"),
            "WK" : pygame.image.load("asets/characters/red_worker.png"),
            "AR" : pygame.image.load("asets/characters/red_archer.png"),
            "CP" : pygame.image.load("asets/characters/red_catapult.png"),
            "EX" : pygame.image.load("asets/characters/red_explorer.png"),
            "CT" : pygame.image.load("asets/buildings/red_capital.png"),
            "PT" : pygame.image.load("asets/floor/mountain.png"),
            "SM" : pygame.image.load("asets/floor/mountain.png"),
            "GM" : pygame.image.load("asets/floor/mountain.png"),
            "IM" : pygame.image.load("asets/floor/mountain.png")
        }

        #Dictionary with the menu of actions of each unit
        self.unitMenu = {
            "FD" : self.founderActions,
            "WR" : self.commonActions,
            "WK" : self.workerActions,
            "AR" : self.commonActions,
            "CP" : self.commonActions,
            "EX" : self.commonActions,
            "CT" : self.cityOptions,
            "PT" : self.structuresOptions,
            "SM" : self.structuresOptions,
            "GM" : self.structuresOptions,
            "IM" : self.structuresOptions
        }

        self.unit = None
        self.city = None

        #Sets the limit for the camera to move
        self.maxCamMoveX = None
        self.maxCamMoveY = None

        #Stores how much the camera move fron the center
        self.cameraMoveX = 0
        self.cameraMoveY = 0    

        self.cameraVelocity = 5 #Sets the velocity of the camera movement    
        
    def loadIconAndCaption(self):
        """Loads and set the title of the window and the icon at the top left of the window"""
        pygame.display.set_caption("T-H-E")
        icon = pygame.image.load("resources/assets/menu/windowicon.png")
        pygame.display.set_icon(icon)      

    def loadMenuStart(self, mousePos, click):
        """Creates and load the elements of the start of the menu"""
        buttonPressed = False #Represents if one of the buttons was pressed or not

        buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")
        buttonBackground = pygame.transform.scale(buttonBackground,(self.screenWidth * 0.46,self.screenHeight * 0.14))
        buttonRect = buttonBackground.get_rect()

        # Loads and draws background
        background = pygame.image.load("resources/assets/menu/defaultback.jpg")
        background = pygame.transform.scale(background,(self.screenWidth,self.screenHeight))
        self.menuSurf.blit(background, (0,0))

        # Loads the logo of the game
        logo = pygame.image.load("resources/assets/menu/gamelogo.png")
        logo = pygame.transform.scale(logo,(self.screenWidth * 0.4,self.screenHeight * 0.72))
        self.menuSurf.blit(logo,((0.25 * self.screenWidth) / 4,(0.75 * self.screenHeight) / 4))

        button1Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button1Rect = button1Surf.get_rect(center = ((3.5 * self.screenWidth) / 5,self.screenHeight / 3.75))

        if button1Rect.collidepoint(mousePos):
            buttonBackground = pygame.image.load("resources/assets/menu/buttonselector.png")
            buttonBackground = pygame.transform.scale(buttonBackground,(self.screenWidth * 0.46,self.screenHeight * 0.14))
            if click == True:
                self.actualMenu = 2
                buttonPressed = True
        else:
            buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")
            buttonBackground = pygame.transform.scale(buttonBackground,(self.screenWidth * 0.46,self.screenHeight * 0.14))

        button1Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font,int(self.screenWidth * 0.08)).render("Play", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect1 = button1Rect

        # Draws the text on the button and then draws the surface
        button1Surf.blit(buttonText, buttonTextRect)
        self.menuSurf.blit(button1Surf, button1Rect)
        
        button2Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button2Rect = button2Surf.get_rect(center = ((3.5 * self.screenWidth) / 5,self.screenHeight / 2))

        if button2Rect.collidepoint(mousePos):
            buttonBackground = pygame.image.load("resources/assets/menu/buttonselector.png")
            buttonBackground = pygame.transform.scale(buttonBackground,(self.screenWidth * 0.46,self.screenHeight * 0.14))
            if click == True:
                self.actualMenu = 4
                buttonPressed = True
        else:
            buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")
            buttonBackground = pygame.transform.scale(buttonBackground,(self.screenWidth * 0.46,self.screenHeight * 0.14))

        button2Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font, 100).render("Instructions", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect2 = button2Rect

        # Draws the text on the button and then draws the surface
        button2Surf.blit(buttonText, buttonTextRect)
        self.menuSurf.blit(button2Surf, button2Rect)

        button3Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button3Rect = button3Surf.get_rect(center = ((3.5 * self.screenWidth) / 5,(3.5 * self.screenHeight) / 5))

        if button3Rect.collidepoint(mousePos):
            buttonBackground = pygame.image.load("resources/assets/menu/buttonselector.png")
            buttonBackground = pygame.transform.scale(buttonBackground,(self.screenWidth * 0.46,self.screenHeight * 0.14))
            if click == True:
                self.actualMenu = 3
                buttonPressed = True
        else:
            buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")
            buttonBackground = pygame.transform.scale(buttonBackground,(self.screenWidth * 0.46,self.screenHeight * 0.14))

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
        buttonBackground = pygame.transform.scale(buttonBackground,(self.screenWidth * 0.46,self.screenHeight * 0.14))
        buttonRect = buttonBackground.get_rect()

        # Loads and draws background
        background = pygame.image.load("resources/assets/menu/defaultback.jpg")
        background = pygame.transform.scale(background,(self.screenWidth,self.screenHeight))
        self.menuSurf.blit(background, (0,0))

        button1Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button1Rect = button1Surf.get_rect(center = (self.screenWidth / 2,self.screenHeight / 4))

        if button1Rect.collidepoint(mousePos):
            buttonBackground = pygame.image.load("resources/assets/menu/buttonselector.png")
            buttonBackground = pygame.transform.scale(buttonBackground,(self.screenWidth * 0.46,self.screenHeight * 0.14))
            if click:
                return "maps/map1.txt"
        else:
            buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")
            buttonBackground = pygame.transform.scale(buttonBackground,(self.screenWidth * 0.46,self.screenHeight * 0.14))

        button1Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font,int(self.screenWidth * 0.08)).render("Pre-created Map", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect1 = button1Rect

        # Draws the text on the button and then draws the surface
        button1Surf.blit(buttonText, buttonTextRect)
        self.menuSurf.blit(button1Surf, button1Rect)

        button2Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button2Rect = button2Surf.get_rect(center = (self.screenWidth / 2,(3 * self.screenHeight) / 4))

        if button2Rect.collidepoint(mousePos):
            buttonBackground = pygame.image.load("resources/assets/menu/buttonselector.png")
            buttonBackground = pygame.transform.scale(buttonBackground,(self.screenWidth * 0.46,self.screenHeight * 0.14))
            if click:
                return "maps/random_world.txt"
        else:
            buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")
            buttonBackground = pygame.transform.scale(buttonBackground,(self.screenWidth * 0.46,self.screenHeight * 0.14))

        button2Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font,int(self.screenWidth * 0.08)).render("Random Map", True, (0,0,0)) # Creates text with a Font 
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
        background = pygame.transform.scale(background,(self.screenWidth,self.screenHeight))
        self.menuSurf.blit(background, (0,0))

        # Writes text on the screen
        text = pygame.font.Font(self.font,int(self.screenWidth * 0.078)).render("Creditos", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (self.screenWidth * 0.5,self.screenHeight * 0.14))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font,int(self.screenWidth * 0.046)).render("Hecho por: Sangiago Abelle, Santella Agustin, Sanna Ian", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (self.screenWidth * 0.5,self.screenHeight * 0.31))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font,int(self.screenWidth * 0.046)).render("Desarrollador del menu: Santiago Abelle", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (self.screenWidth * 0.5,self.screenHeight * 0.45))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font,int(self.screenWidth * 0.046)).render("Desarrollador de la generacion del mapa: Sanna Ian", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (self.screenWidth * 0.5,self.screenHeight * 0.59))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font,int(self.screenWidth * 0.046)).render("Diseñador grafico: Santella Agustin", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (self.screenWidth * 0.5,self.screenHeight * 0.73))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font,int(self.screenWidth * 0.054)).render("Esperamos que hayas disfrutado de The Huergo Empires", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (self.screenWidth * 0.5,self.screenHeight * 0.92))

        self.menuSurf.blit(text, textRect)

    def loadInstructions(self, mousePos, click):
        """Creates and loads the screen of Instructions"""

        self.buttonRect1 = pygame.Rect(0,0,0,0)
        self.buttonRect2 = pygame.Rect(0,0,0,0)
        self.buttonRect3 = pygame.Rect(0,0,0,0)

        # Loads and draws background
        background = pygame.image.load("resources/assets/menu/defaultback.jpg")
        background = pygame.transform.scale(background,(self.screenWidth,self.screenHeight))
        self.menuSurf.blit(background, (0,0))

        # Writes text on the screen
        text = pygame.font.Font(self.font,int(self.screenWidth * 0.08)).render("Instrucciones", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (self.screenWidth * 0.5,self.screenHeight * 0.14))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font,int(self.screenWidth * 0.0375)).render("""1- Para ganar se debe vencer a todos los enemigos o completar una de las investigaciones en su totalidad""", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(midleft = (10,self.screenHeight * 0.31))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font,int(self.screenWidth * 0.0375)).render("2- Se pasa de turno utilizando la tecla enter", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(midleft = (10,self.screenHeight * 0.45))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font,int(self.screenWidth * 0.0375)).render("3- Solo se pueden mover las unidades e interactuar con las ciudades cierta cantidad de veces por turno", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(midleft = (10,self.screenHeight * 0.59))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font,int(self.screenWidth * 0.0375)).render("4- Las unidades necesitan comida y para construir se requiren materiales", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(midleft = (10,self.screenHeight * 0.73))

        self.menuSurf.blit(text, textRect)

        text = pygame.font.Font(self.font,int(self.screenWidth * 0.0375)).render("5- Divertirse jugando", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(midleft = (10,self.screenHeight * 0.88))

        self.menuSurf.blit(text, textRect)

    def loadLogOut(self, mousePos, click):
        """Creates and loads the elements for the Log out screen"""

        buttonPressed = False

        self.buttonRect1 = pygame.Rect(0,0,0,0)
        self.buttonRect2 = pygame.Rect(0,0,0,0)
        self.buttonRect3 = pygame.Rect(0,0,0,0)

        self.menuSurf.fill((0,0,0))

        # Loads and draws background
        background = pygame.image.load("resources/assets/menu/defaultback.jpg")

        backgroundSurf = pygame.Surface((self.screenWidth, self.screenHeight), pygame.SRCALPHA)
        backgroundSurf.blit(background, (0,0))
        backgroundSurf.set_alpha(100)
        self.menuSurf.blit(backgroundSurf, (0,0))

        # Writes text on the screen
        text = pygame.font.Font(self.font,int(self.screenWidth * 0.08)).render("¿Queres cerrar el juego?", True, (255,255,255)) # Creates text with a Font 
        textRect = text.get_rect(center = (640, 100))

        self.menuSurf.blit(text, textRect)
        
        buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")
        buttonRect = buttonBackground.get_rect()

        button1Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button1Rect = button1Surf.get_rect(center = (640, 281))

        if button1Rect.collidepoint(mousePos):
            buttonBackground = pygame.image.load("resources/assets/menu/buttonselector.png")
            if click == True:
                self.terminate()
        else:
            buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")

        button1Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font,int(self.screenWidth * 0.08)).render("Si", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect1 = button1Rect

        # Draws the text on the button and then draws the surface
        button1Surf.blit(buttonText, buttonTextRect)
        self.menuSurf.blit(button1Surf, button1Rect)

        button2Surf = pygame.Surface((buttonRect[2], buttonRect[3])) #Creates a surface for the button
        button2Rect = button2Surf.get_rect(center = (640,469))

        if button2Rect.collidepoint(mousePos):
            buttonBackground = pygame.image.load("resources/assets/menu/buttonselector.png")
            if click == True:
                self.actualMenu = 1
                buttonPressed = True
        else:
            buttonBackground = pygame.image.load("resources/assets/menu/menubuttontexture.jpg")

        button2Surf.blit(buttonBackground, (0,0)) # Draws the background for the button

        buttonText = pygame.font.Font(self.font,int(self.screenWidth * 0.08)).render("No", True, (0,0,0)) # Creates text with a Font 
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2]/2, buttonRect[3]/2))

        self.buttonRect2 = button2Rect

        # Draws the text on the button and then draws the surface
        button2Surf.blit(buttonText, buttonTextRect)
        self.menuSurf.blit(button2Surf, button2Rect)
        
        self.buttonRect3 = pygame.Rect(0,0,0,0)

        if buttonPressed:
            self.collition = False
            self.loadActualMenu((0,0), False)

    def loadMouseIcon(self, mousePos):
        """Loads the mouse image"""
        mouse = pygame.image.load("resources/assets/menu/defaultcursor.png")
        mouse = pygame.transform.scale(mouse,(self.screenWidth * 0.025,self.screenHeight * 0.055))
        self.screen.blit(mouse, mousePos)

    def terminate(self):
        """Finish the program"""
        pygame.quit()
        sys.exit()

    def setRescaling(self,scale):
        self.resized = True
        self.scale = scale
        self.screenWidth = self.scale[0]
        self.screenHeight = self.scale[1]
        self.screen = pygame.display.set_mode((self.screenWidth,self.screenHeight),pygame.RESIZABLE)
        self.menuSurf = pygame.transform.scale(self.menuSurf,self.scale)

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
                return self.loadActualMenu(mousePos, click)                    
        else:
            if self.collition == True:
                self.collition = False  
                self.loadActualMenu(mousePos, click)
                
    def loadActualMenu(self, mousePos, click):
        return self.actualMenuDict[self.actualMenu](mousePos, click)

    def goBack(self):
        """Redirects to the menu before the actual one"""

        goBackDict = {
            1 : 0,
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
                visibility = self.model.getCellVisibility(x, y)
                biome, unit = self.model.getCellData(x, y)
                if visibility == (True, True):
                    baseTile = self.textToMap[biome]
                    baseTile = pygame.transform.scale(baseTile,((self.tileWidth,self.tileHeight)))
                    tileRect = pygame.Rect(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight)
                    self.mapSurf.blit(baseTile, tileRect)
                    if unit != None:
                        unitImage = self.textToUnit[str(unit)]
                        unitImage = pygame.transform.scale(unitImage,((self.tileWidth,self.tileHeight)))
                        self.mapSurf.blit(unitImage, tileRect) #Draws the unit on the cell
                        health, maxHealth = self.model.getUnitHealth(unit)
                        relationHealthBar = health/maxHealth

                        heightBar = self.tileHeight / 5.33
                        healthBar = pygame.Surface((self.tileWidth, heightBar))
                        healthBarRect = pygame.Rect(tileRect[0], tileRect[1] + self.tileHeight - heightBar, self.tileWidth, heightBar)

                        colorHealthBar = pygame.Surface(((self.tileWidth - 2) * relationHealthBar, heightBar - 2))
                        colorHealthBar.fill((255, 0, 0))
                        colorHealthBarRect = colorHealthBar.get_rect(topleft = (healthBarRect[0] + 1, healthBarRect[1] + 1))

                        self.mapSurf.blit(healthBar, healthBarRect)
                        self.mapSurf.blit(colorHealthBar, colorHealthBarRect)



                if visibility == (True, False):
                    baseTile = self.textToMap[" " + biome]
                    tileRect = pygame.Rect((x * self.tileWidth, y * self.tileHeight),(self.tileWidth,self.tileHeight))
                    print(self.tileWidth,self.tileHeight)
                    self.mapSurf.blit(baseTile, tileRect)
                if visibility == (False, False):
                    baseTile = self.textToMap[""]
                    tileRect = pygame.Rect((x * self.tileWidth, y * self.tileHeight),(self.tileWidth,self.tileHeight))
                    print(self.tileWidth,self.tileHeight)
                    self.mapSurf.blit(baseTile, tileRect)

    def mapNeedsRedraw(self):
        if self.model.getMapRedraw():
            self.drawMap()

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

    def centerLoadCamera(self):
        posX, posY = self.model.getPositionUnit()
        if posX < self.mapWidth/2:
            self.cameraMoveX += abs(posX - self.mapWidth/2) * self.tileWidth
        else:
            self.cameraMoveX -= abs(posX - self.mapWidth/2) * self.tileWidth
        if posY < self.mapHeight/2:
            self.cameraMoveY += abs(posY - self.mapHeight/2) * self.tileHeight
        else:
            self.cameraMoveY -= abs(posY - self.mapHeight/2) * self.tileHeight
        if self.cameraMoveY > self.maxCamMoveY:
            self.cameraMoveY = self.maxCamMoveY
        elif self.cameraMoveY < -self.maxCamMoveY:
            self.cameraMoveY = -self.maxCamMoveY 
        if self.cameraMoveX > self.maxCamMoveX:
            self.cameraMoveX = self.maxCamMoveX 
        elif self.cameraMoveX < -self.maxCamMoveX:
            self.cameraMoveX = -self.maxCamMoveX

    def getMouseMapPos(self, mousePos):
        """Gets the mouse position in relation of the map Surface"""
        rectX, rectY = self.mapRect.topleft        
        mousePos = tuple(sum(x) for x in zip(mousePos, (abs(rectX), abs(rectY))))
        posX, posY = mousePos
        return math.floor(posX/self.tileWidth), math.floor(posY/self.tileHeight)

    def updateGame(self, mousePos):
        if self.resized:
            self.mapSurf = self.mapSurf = pygame.transform.scale(self.mapSurf,(self.screenWidth,self.screenHeight))
        self.screen.fill((0,0,0))
        self.mapRect = self.mapSurf.get_rect(center = (self.screenWidth/2 + self.cameraMoveX, self.screenHeight/2 + self.cameraMoveY))  
        self.screen.blit(self.mapSurf, self.mapRect)
        self.drawUnitActions((0, 0), False)
        self.drawActualResources()
        self.drawCursor(mousePos)
        pygame.display.update()

    def drawCursor(self, mousePos):
        """Draws a custom cursor and marks the selected cell"""
        cursor = pygame.image.load("asets/handcursor.png")
        cursor = pygame.transform.scale(cursor,(self.screenWidth * 0.025,self.screenHeight * 0.055))
        self.screen.blit(cursor, mousePos)

    def founderActions(self, mousePos, click):
        """Draws the button with the possible action of the founder unit"""
        defendIcon = pygame.image.load("asets/buttons/rest_button.png")
        defendIcon = pygame.transform.scale(defendIcon,(self.screenWidth * 0.025,self.screenHeight * 0.04))
        iconRect = pygame.Rect(self.screenWidth - self.tileWidth*2, self.screenHeight - self.tileHeight, self.tileWidth, self.tileHeight)
        self.screen.blit(defendIcon, iconRect)
        if iconRect.collidepoint(mousePos) and click == True:
            self.unit = None
            self.model.unitRest()
            self.model.setUnitMenu(None)
            return True

        attackIcon = pygame.image.load("asets/buttons/battle_button.png")
        attackIcon = pygame.transform.scale(attackIcon,(self.screenWidth * 0.025,self.screenHeight * 0.04))
        iconRect = pygame.Rect(self.screenWidth - self.tileWidth*4, self.screenHeight - self.tileHeight, self.tileWidth, self.tileHeight)
        self.screen.blit(attackIcon, iconRect)
        if iconRect.collidepoint(mousePos) and click == True:
            self.unit = None
            self.model.setUnitMenu(None)
            self.model.setAttack(True)
            return True

        foundIcon = pygame.image.load("asets/buttons/found_button.png")
        foundIcon = pygame.transform.scale(foundIcon,(self.screenWidth * 0.025,self.screenHeight * 0.04))
        iconRect = pygame.Rect(self.screenWidth - self.tileWidth*6, self.screenHeight - self.tileHeight, self.tileWidth, self.tileHeight)
        self.screen.blit(foundIcon, iconRect)
        if iconRect.collidepoint(mousePos) and click == True:
            self.unit = None
            self.model.foundCity()
            self.model.setUnitMenu(None)
            return True

    def commonActions(self, mousePos, click):
        """Draws the buttons with the possible action of the warrior unit"""

        defendIcon = pygame.image.load("asets/buttons/rest_button.png")
        defendIcon = pygame.transform.scale(defendIcon,(self.screenWidth * 0.025,self.screenHeight * 0.04))
        iconRect = pygame.Rect(self.screenWidth - self.tileWidth*2, self.screenHeight - self.tileHeight, self.tileWidth, self.tileHeight)
        self.screen.blit(defendIcon, iconRect)
        if iconRect.collidepoint(mousePos) and click == True:
            self.unit = None
            self.model.unitRest()
            self.model.setUnitMenu(None)
            return True

        attackIcon = pygame.image.load("asets/buttons/battle_button.png")
        attackIcon = pygame.transform.scale(attackIcon,(self.screenWidth * 0.025,self.screenHeight * 0.04))
        iconRect = pygame.Rect(self.screenWidth - self.tileWidth*4, self.screenHeight - self.tileHeight, self.tileWidth, self.tileHeight)
        self.screen.blit(attackIcon, iconRect)
        if iconRect.collidepoint(mousePos) and click == True:
            self.unit = None
            self.model.setUnitMenu(None)
            self.model.setAttack(True)
            return True

    def workerActions(self, mousePos, click):
        """Draws the buttons of the workers actions"""

        defendIcon = pygame.image.load("asets/buttons/rest_button.png")
        defendIcon = pygame.transform.scale(defendIcon,(self.screenWidth * 0.025,self.screenHeight * 0.04)) #32*32
        iconRect = pygame.Rect(self.screenWidth - self.tileWidth*2, self.screenHeight - self.tileHeight, self.tileWidth, self.tileHeight)
        self.screen.blit(defendIcon, iconRect)
        if iconRect.collidepoint(mousePos) and click == True:
            self.unit = None
            self.model.unitRest()
            self.model.setUnitMenu(None)
            return True
        
        buildIcon = pygame.image.load("asets/buttons/build_button.png")
        buildIcon = pygame.transform.scale(buildIcon,(self.screenWidth * 0.025,self.screenHeight * 0.04))
        iconRect = pygame.Rect(self.screenWidth - self.tileWidth*4, self.screenHeight - self.tileHeight, self.tileWidth, self.tileHeight)
        self.screen.blit(buildIcon, iconRect)
        if iconRect.collidepoint(mousePos) and click == True:
            self.unit = None
            self.model.setConstruct(True)
            self.model.setUnitMenu(None)
            return True

    def cityOptions(self, mousePos, click):
        """Shows the options of the city"""

        #Draws backgroung of the city menu
        background = pygame.image.load("asets/woodBackground.jpg")
        background = pygame.transform.scale(background,(self.screenWidth * 0.31,self.screenHeight * 1))
        backgroundRect = background.get_rect()
        backgroundSurf = pygame.Surface((backgroundRect[2], backgroundRect[3]))
        backgroundSurf.blit(background, (0,0))
        backgroundRect[0] += self.screenWidth - backgroundRect[2]

        unitsDict = self.model.getAllUnitsAndCosts()

        itemMenu = pygame.image.load("asets/woodOptions.jpg")
        itemMenu = pygame.transform.scale(itemMenu,(self.screenWidth * 0.24,self.screenHeight * 0.09))
        itemMenuRect = itemMenu.get_rect()
        itemMenuRect[1] += 20 #Leaves a margin at the top
        itemMenuRect.centerx = backgroundRect[2] / 2 # Centers the options

        posX, posY = mousePos
        posX -= backgroundRect[0]
        mousePos = (posX, posY)

        #For each posible unit, it creates an item
        for key in unitsDict.keys():
            #Creates a Surface and draws a background for a new item
            itemMenuSurf = pygame.Surface((itemMenuRect[2], itemMenuRect[3]))
            itemMenuSurf.blit(itemMenu, (0,0))

            unitImage = self.textToUnit[key] #Gets the image of the unit
            unitImageRect = unitImage.get_rect()

            #Sets the position and draws the image of the unit
            unitImageRect.topleft = ((itemMenuRect[3] - unitImageRect[3]) / 2, (itemMenuRect[3] - unitImageRect[3]) / 2)
            itemMenuSurf.blit(unitImage, unitImageRect)

            unitData = unitsDict[key]
            gold, silver, turns, food = unitData

            if itemMenuRect.collidepoint(mousePos):
                self.model.assignUnitCreation(key, turns, gold, silver)

            #Draws the resources needed of each one to create the unit
            #GOLD
            goldText = pygame.font.Font(self.font,self.screenWidth * 0.0195).render("gold: " + str(gold), True, (255,255,255))
            goldTextRect = goldText.get_rect(center = (itemMenuRect[2] / 3, itemMenuRect[3] / 3))
            itemMenuSurf.blit(goldText, goldTextRect)

            #SILVER
            silverText = pygame.font.Font(self.font,self.screenWidth * 0.0195).render("silver: " + str(silver), True, (255,255,255))
            silverTextRect = silverText.get_rect(center = (itemMenuRect[2] / 3, itemMenuRect[3] / 3 * 2))
            itemMenuSurf.blit(silverText, silverTextRect)

            #TURNS
            turnsText = pygame.font.Font(self.font, self.screenWidth * 0.0195).render("turns: " + str(turns), True, (255,255,255))
            turnsTextRect = turnsText.get_rect(center = (itemMenuRect[2] / 3 * 2, itemMenuRect[3] / 3))
            itemMenuSurf.blit(turnsText, turnsTextRect)

            #FOOD
            foodText = pygame.font.Font(self.font,self.screenWidth * 0.0195).render("food: " + str(food) + " p/t", True, (255,255,255))
            foodTextRect = foodText.get_rect(center = (itemMenuRect[2] / 3 * 2, itemMenuRect[3] / 3 * 2))
            itemMenuSurf.blit(foodText, foodTextRect)

            backgroundSurf.blit(itemMenuSurf, itemMenuRect)
            itemMenuRect[1] += 100

        #Creates a surface and draws a button
        buttonImg = pygame.image.load("asets/cancel_button.jpg")
        buttonImg = pygame.transform.scale(buttonImg,(self.screenWidth * 0.19,self.screenHeight * 0.09))

        buttonRect = buttonImg.get_rect()
        buttonRect.topleft = ((backgroundRect[2] - buttonRect[2]) / 2, itemMenuRect[1])

        #Checks if the cancel button is pressed
        if buttonRect.collidepoint(mousePos) == True and click == True:
            self.model.setCityMenu(None)
            return True

        buttonSurf = pygame.Surface((buttonRect[2], buttonRect[3]))
        buttonSurf.blit(buttonImg, (0,0))

        #Drawss the text that goes on the button
        buttonText = pygame.font.Font(self.font,self.screenWidth * 0.03125).render("Cancel", True, (255,255,255))
        buttonTextRect = buttonText.get_rect(center = (buttonRect[2] / 2, buttonRect[3] / 2))
        buttonSurf.blit(buttonText, buttonTextRect)

        backgroundSurf.blit(buttonSurf, buttonRect)

        self.screen.blit(backgroundSurf, backgroundRect)

    def structuresOptions(self, mousePos, click):
        """It literaly do nothing, used for other structures apart from the city which not display anithing"""
        self.model.setCityMenu(None)

    def drawUnitActions(self, mousePos, click):
        self.unit = self.model.getUnitMenu()
        self.city = self.model.getCityMenu()
        if self.city != None:
            return self.unitMenu[self.city](mousePos, click)
        if self.unit != None:
            return self.unitMenu[self.unit](mousePos, click)
        
    def drawActualResources(self):
        """Draws at the top left of the screen the remain resources"""
        gold, silver, wood, food = self.model.getResources()

        resources = {
            "Gold: " : gold,
            "Silver: " : silver,
            "Wood: " : wood,
            "Food: " : food
        }

        screenX = 0

        for key in resources.keys():
            text = pygame.font.Font(self.font,int(self.screenWidth * 0.013)).render(key + str(resources[key]), True, (255,255,255))
            textRect = text.get_rect()
            self.screen.blit(text, (screenX, 0))
            screenX += textRect[2] + (self.screenWidth * 0.007)


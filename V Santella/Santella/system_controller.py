import pygame

pygame.init()

class SystemController():
    def __init__(self):
        """Function __init__"""
        self.buttexture = None
        self.screenlogo = None
        self.event = None

    def systemLoads(self):
        """ """
        windowiconload = pygame.image.load('assets/menus/icon.png') #Loads the window icon
        windowicon = pygame.display.set_icon(windowiconload) #Sets the window icon
        windowname = pygame.display.set_caption('civ_POO') #Sets the title of the window
        self.buttexture = pygame.image.load('assets/Menus/Menu_button_Play.png') #Loads the texture from the game buttons
        buttselector = pygame.image.load('assets/Menus/Menu_button_Play_pressed.png')
        return windowicon,windowname,self.buttexture,buttselector

    def menuesLoads(self,num):
        """Function menuesLoads, loads all the menues resources, renders the texts and creates the collisions"""
        if num == 1: #Background image
            defback = pygame.image.load('asets/menus/background.jpg') #Loads the 'background' image
            defaultcursor = pygame.image.load('asets/menus/Mouse.png').convert_alpha() #Loads the default cursor image
            return defback,defaultcursor

        elif num == 2: #Map selector
            mapselbtn = self.buttexture #Adds the wood button texture to this button
            mapselbtncoll = mapselbtn.get_rect(midleft = (640,238)) #Creates the collision from the previous button
            return mapselbtn,mapselbtncoll

        elif num == 3: #Random mode
            btnrandom = self.buttexture #Adds the wood button texture to this button
            btnrandomcoll = btnrandom.get_rect(midleft = (335,275)) #Creates the collision from the previous button
            return btnrandom,btnrandomcoll

        elif num == 4: #Created mode
            btncreated = self.buttexture #Adds the wood button texture to this button
            btncreatedcoll = btncreated.get_rect(midleft = (335,425)) #Creates the collision from the previous button
            return btncreated,btncreatedcoll
    
    def screenLogo(self):
        """ """
        screenlogo = pygame.transform.scale2x(pygame.image.load('asets/menus/logo.png')).convert #Loads the logo from the main menu
        screenlogocoll = screenlogo.get_rect(center = (350, 360)) #Creates the collision from the previous logo
        return screenlogo,screenlogocoll

    def controlMouseMovement(self):
        """Function controlMouseMovement, gets the mouse position and sets the cursor on non visible"""
        self.mousepos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        return self.mousepos

    def controlInputsEvents(self,mode):
        """Function controlInputsEvents, controls the keyboard or mouse inputs"""
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                return 'exit'
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                return 'mouseon'
            """Only for WorkInProgress, Credits, Instructions, MapSelector"""
            if  mode == 'map':
                if self.event.type == pygame.KEYDOWN:
                    """Escape"""
                    if self.event.key == pygame.K_ESCAPE:
                        return 'nonexit'






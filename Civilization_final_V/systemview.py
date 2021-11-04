import pygame
from pygame.locals import *

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

class GameView():
    """ """
    def __init__(self):
        """Function __init__"""
        self.screensX = 1280 #Is the width from the window
        self.screensY = 704 #Is the height from the window
        self.screenSize = (self.screensX,self.screensY) #Is the size from the window
        self.screen = pygame.display.set_mode(self.screenSize, pygame.RESIZABLE)
        self.windowIcon,self.windowName,self.menufont,self.menufontlittle,self.menufontlittle2,self.buttonwoodtexture,self.buttonselector = self.systemLoads() #Uses the systemLoads function from systemcontroller
        self.clock = pygame.time.Clock() #Creates the clock function from the game
        self.mousepos = (0,0) #Records the position from the mouse
        self.screenlogo = pygame.image.load('resources/assets/gamelogo.png') #Loads the logo from the main menu
        self.screenlogocoll = self.screenlogo.get_rect(center = (350,360)) #Creates the collision from the previous logo
        self.loadingtext,self.loadingtextcoll,self.loadingbar,self.loadingbarcoll = self.menuesLoads(9)

        self.event = ''
        self.mouseclicked = False
        self.defaultbackground = None
        self.menumusic = None
        self.defaultcursor = None
        self.handcursor = None
        self.workinprogressmessage = None
        self.underconstruction = None
        self.exitbackground = None
        self.exitbackgroundpos = None
        self.exittext = None
        self.exittextpos = None
        self.exitbuttonyes = None
        self.exitbuttonyescoll = None
        self.exitbuttonyestext = None
        self.exitbuttonyestextcoll = None
        self.exitbuttonno = None
        self.exitbuttonnocoll = None
        self.exitbuttonnotext = None
        self.exitbuttonnotextcoll = None
        self.mapselectorbutton = None
        self.mapselectorbuttoncoll = None
        self.mapselectorbuttontext = None
        self.mapselectorbuttontextcoll = None
        self.menubuttoncredits = None
        self.menubuttoncreditstext = None
        self.menubuttoncreditscoll = None
        self.menubuttoncreditstextcoll = None
        self.menubuttoninstructions = None
        self.menubuttoninstructionstext = None
        self.menubuttoninstructionscoll = None
        self.menubuttoninstructionstextcoll = None
        self.randomplaybutton = None
        self.randomplaybuttoncoll = None
        self.randomplaybuttontext = None
        self.randomplaybuttontextcoll = None
        self.createdplaybutton = None
        self.createdplaybuttoncoll = None
        self.createdplaybuttontext = None
        self.createdplaybuttontextcoll = None
        self.swordcursor = None
        self.foundersprite = None
        self.founderspriteposx = None
        self.founderspriteposy = None
        self.founderspritecoll = None
        self.biometiles = None
        self.hidden = None
        self.gamemusic1 = None
        self.gamemusic2 = None
        self.mouseoldpos = None
    
    def loadBarView(self,mode):
        """Function loadBarView, is the loop from the load bar"""
        loading = True
        loadingstep = 0
        loadingprogressvalue = 0
        while loading:
            loadingstep += 1

            """Background"""
            self.screen.fill([0,0,0])
            """Text"""
            self.screen.blit(self.loadingtext,self.loadingtextcoll)
            """Loading Bar"""
            self.screen.blit(self.loadingbar,self.loadingbarcoll)
            """Loading Bar Content Complete"""
            pygame.draw.rect(self.screen,[116,125,131],(250,542,loadingprogressvalue,20)) #97 == 8% progress
    
    def menuFirstDraw(self):
        """Function menuFirstDraw, draws in the menu the basic draw"""
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Game Logo"""
        self.screen.blit(self.screenlogo,self.screenlogocoll)
        """Buttons"""
        """Play"""
        self.screen.blit(self.mapselectorbutton,self.mapselectorbuttoncoll)
        self.screen.blit(self.mapselectorbuttontext,self.mapselectorbuttontextcoll)
        """Credits"""
        self.screen.blit(self.menubuttoncredits,self.menubuttoncreditscoll)
        self.screen.blit(self.menubuttoncreditstext,self.menubuttoncreditstextcoll)
        """Instructions"""
        self.screen.blit(self.menubuttoninstructions,self.menubuttoninstructionscoll)
        self.screen.blit(self.menubuttoninstructionstext,self.menubuttoninstructionstextcoll)
        self.menumusic.play(loops = -1)
        self.menumusic.set_volume(0.50)

    def menuView(self,mousepos,keyevent):
        """Function menuView, is the menu loop"""
        returnedvalue = ' '

        self.mouseclicked = False

        """Mouse Movement"""
        self.mousepos = mousepos
            
        """Events Manager"""
        self.event = keyevent
        if self.event == 'exit':
            returnedvalue = 'exit'
        elif self.event == 'mouseon':
            self.mouseclicked = True

        """Draw Calls"""
        try:
            if self.mouseoldpos != self.mousepos:
                """Background"""
                self.screen.blit(self.defaultbackground,(0,0))
                """Game Logo"""
                self.screen.blit(self.screenlogo,self.screenlogocoll)
                """Buttons"""
                """Play"""
                self.screen.blit(self.mapselectorbutton,self.mapselectorbuttoncoll)
                self.screen.blit(self.mapselectorbuttontext,self.mapselectorbuttontextcoll)
                """Credits"""
                self.screen.blit(self.menubuttoncredits,self.menubuttoncreditscoll)
                self.screen.blit(self.menubuttoncreditstext,self.menubuttoncreditstextcoll)
                """Instructions"""
                self.screen.blit(self.menubuttoninstructions,self.menubuttoninstructionscoll)
                self.screen.blit(self.menubuttoninstructionstext,self.menubuttoninstructionstextcoll)
        except:
            pass

        """Mouses"""
        if self.mapselectorbuttoncoll.collidepoint(self.mousepos) == True or self.menubuttoncreditscoll.collidepoint(self.mousepos) == True or self.menubuttoninstructionscoll.collidepoint(self.mousepos) == True:
            self.screen.blit(self.handcursor,self.mousepos)
        else:
            self.screen.blit(self.defaultcursor,self.mousepos)

        """Control"""
        """Mouse Passes Over the Buttons"""
        """Map Select"""
        if self.mapselectorbuttoncoll.collidepoint(self.mousepos) == True:
            self.screen.blit(self.buttonselector,self.mapselectorbuttoncoll)
            self.screen.blit(self.handcursor,self.mousepos)
            if self.mouseclicked == True:
                self.mouseclicked = False
                self.menumusic.stop()
                returnedvalue = 'map'
        """Credits"""
        if self.menubuttoncreditscoll.collidepoint(self.mousepos) == True:
            self.screen.blit(self.buttonselector,self.menubuttoncreditscoll)
            self.screen.blit(self.handcursor,self.mousepos)
            if self.mouseclicked == True:
                self.mouseclicked = False
                returnedvalue = 'crets'
        """Instructions"""
        if self.menubuttoninstructionscoll.collidepoint(self.mousepos) == True:
            self.screen.blit(self.buttonselector,self.menubuttoninstructionscoll)
            self.screen.blit(self.handcursor,self.mousepos)
            if self.mouseclicked == True:
                self.mouseclicked = False
                returnedvalue = 'insts'

        """System"""
        self.mouseoldpos = self.mousepos
        try:
            self.screenUpdate(self.clock,30)
        except:
            pass

        return returnedvalue

    def workInProgressFirstDraw(self):
        """Function workInProgressFirstDraw, draws in the screen the basic work in progress menu"""
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Under Construction"""
        self.screen.blit(self.workinprogressmessage,(275,300))
        self.screen.blit(self.underconstruction,(425,75))
    
    def workInProgressView(self,mousepos,keyevent):
        """Function workInProgressView, is the work in progress menu loop"""
        
        returnedvalue = ' '

        self.mouseclicked = False

        """Mouse Movement"""
        self.mousepos = mousepos
            
        """Events Manager"""
        self.event = keyevent
        if self.event == 'exit':
            returnedvalue = 'exit'
        elif self.event == 'nonexit':
            returnedvalue = 'nonexit'

        """Draw Calls"""
        try:
            if self.mouseoldpos != self.mousepos:
                """Background"""
                self.screen.blit(self.defaultbackground,(0,0))
                """Under Construction"""
                self.screen.blit(self.workinprogressmessage,(275,300))
                self.screen.blit(self.underconstruction,(425,75))
                self.screen.blit(self.defaultcursor,self.mousepos)
        except:
            pass

        """System"""
        self.mouseoldpos = self.mousepos
        try:
            self.screenUpdate(self.clock,30)
        except:
            pass

        return returnedvalue
    
    def exitUIFirstDraw(self):
        """Function exitUIFirstDraw, draws in the screen the basic exit UI menu"""
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.exitbackground,self.exitbackgroundpos)
        """Question"""
        self.screen.blit(self.exittext,self.exittextpos)
        """Buttons"""
        """Yes"""
        self.screen.blit(self.exitbuttonyes,self.exitbuttonyescoll)
        self.screen.blit(self.exitbuttonyestext,self.exitbuttonyestextcoll)
        """No"""
        self.screen.blit(self.exitbuttonno,self.exitbuttonnocoll)
        self.screen.blit(self.exitbuttonnotext,self.exitbuttonnotextcoll)
        oldmousepos = (0,0)
    
    def exitUIView(self,mousepos,keyevent):
        """Function exitUIView, is the exit UI menu loop"""
        
        returnedvalue = ' '

        self.mouseclicked = False

        """Mouse Movement"""
        self.mousepos = mousepos
            
        """Events Manager"""
        self.event = keyevent
        if self.event == 'mouseon':
            self.mouseclicked = True
        elif self.event == 'mouseoff':
            self.mouseclicked = False

        """Draw Calls"""
        try:
            if self.mouseoldpos != self.mousepos:
                """Draw Calls"""
                """Background"""
                self.screen.blit(self.exitbackground,self.exitbackgroundpos)
                """Question"""
                self.screen.blit(self.exittext,self.exittextpos)
                """Buttons"""
                """Yes"""
                self.screen.blit(self.exitbuttonyes,self.exitbuttonyescoll)
                self.screen.blit(self.exitbuttonyestext,self.exitbuttonyestextcoll)
                """No"""
                self.screen.blit(self.exitbuttonno,self.exitbuttonnocoll)
                self.screen.blit(self.exitbuttonnotext,self.exitbuttonnotextcoll)
                """Mouse"""
                self.screen.blit(self.defaultcursor,self.mousepos)

                """Control"""
                """Mouse Passes Over the Buttons"""
                """Yes"""
                if self.exitbuttonyescoll.collidepoint(self.mousepos) == True:
                    self.screen.blit(self.buttonselector,self.exitbuttonyescoll)
                    self.screen.blit(self.handcursor,self.mousepos)
                    if self.mouseclicked == True:
                        self.mouseclicked = False
                        pygame.quit()
                        exit()
                """No"""
                if self.exitbuttonnocoll.collidepoint(self.mousepos) == True:
                    self.screen.blit(self.buttonselector,self.exitbuttonnocoll)
                    self.screen.blit(self.handcursor,self.mousepos)
                    if self.mouseclicked == True:
                        self.mouseclicked = False
                        returnedvalue = 'nonexit'
        except:
            pass

        """System"""
        self.mouseoldpos = self.mousepos
        try:
            self.screenUpdate(self.clock,30)
        except:
            pass
    
    def creditsFirstDraw(self):
        """Function creditsFirstDraw, draws in the screen the basic credits menu"""
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Under Construction"""
        self.screen.blit(self.workinprogressmessage,(275,300))
        self.screen.blit(self.underconstruction,(425,75))
    
    def creditsView(self,mousepos,keyevent):
        """Function creditsView, is the credits menu loop"""
        
        returnedvalue = ' '

        self.mouseclicked = False

        """Mouse Movement"""
        self.mousepos = mousepos
            
        """Events Manager"""
        self.event = keyevent
        if self.event == 'exit':
            returnedvalue = 'credits'
        elif self.event == 'nonexit':
            returnedvalue = 'nonexit'

        """Draw Calls"""
        try:
            if self.mouseoldpos != self.mousepos:
                """Background"""
                self.screen.blit(self.defaultbackground,(0,0))
                """Under Construction"""
                self.screen.blit(self.workinprogressmessage,(275,300))
                self.screen.blit(self.underconstruction,(425,75))
                self.screen.blit(self.defaultcursor,self.mousepos)
        except:
            pass

        """System"""
        self.mouseoldpos = self.mousepos
        try:
            self.screenUpdate(self.clock,30)
        except:
            pass

        return returnedvalue

    def instructionsFirstDraw(self):
        """Function instructionsFirstDraw, draws in the screen the basic instructions menu"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Under Construction"""
        self.screen.blit(self.workinprogressmessage,(275,300))
        self.screen.blit(self.underconstruction,(425,75))
    
    def instructionsView(self,mousepos,keyevent):
        """Function instructionsView, is the instructions menu loop"""
        
        returnedvalue = ' '

        self.mouseclicked = False

        """Mouse Movement"""
        self.mousepos = mousepos
            
        """Events Manager"""
        self.event = keyevent
        if self.event == 'exit':
            returnedvalue = 'credits'
        elif self.event == 'nonexit':
            returnedvalue = 'nonexit'

        """Draw Calls"""
        try:
            if self.mouseoldpos != self.mousepos:
                """Background"""
                self.screen.blit(self.defaultbackground,(0,0))
                """Under Construction"""
                self.screen.blit(self.workinprogressmessage,(275,300))
                self.screen.blit(self.underconstruction,(425,75))
                self.screen.blit(self.defaultcursor,self.mousepos)
        except:
            pass

        """System"""
        self.mouseoldpos = self.mousepos
        try:
            self.screenUpdate(self.clock,30)
        except:
            pass

        return returnedvalue
    
    def mapSelectorFirstDraw(self):
        """Function mapSelectorFirstDraw, draws in the screen the basic map selector menu"""
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Buttons"""
        """Play Random"""
        self.screen.blit(self.randomplaybutton,self.randomplaybuttoncoll)
        self.screen.blit(self.randomplaybuttontext,self.randomplaybuttontextcoll)
        """Play Pre-Created"""
        self.screen.blit(self.createdplaybutton,self.createdplaybuttoncoll)
        self.screen.blit(self.createdplaybuttontext,self.createdplaybuttontextcoll)

    def mapSeclectorView(self,mousepos,keyevent):
        """Function mapSeclectorView, is the map selector menu loop"""
        
        returnedvalue = ' '

        self.mouseclicked = False

        """Mouse Movement"""
        self.mousepos = mousepos
            
        """Events Manager"""
        self.event = keyevent
        if self.event == 'exit':
            returnedvalue = 'exit'
        elif self.event == 'nonexit':
            returnedvalue = 'nonexit'
        elif self.event == 'mouseon':
            self.mouseclicked = True

        """Draw Calls"""
        try:
            if self.mouseoldpos != self.mousepos:
                """Draw Calls"""
                """Background"""
                self.screen.blit(self.defaultbackground,(0,0))
                """Buttons"""
                """Play Random"""
                self.screen.blit(self.randomplaybutton,self.randomplaybuttoncoll)
                self.screen.blit(self.randomplaybuttontext,self.randomplaybuttontextcoll)
                """Play Pre-Created"""
                self.screen.blit(self.createdplaybutton,self.createdplaybuttoncoll)
                self.screen.blit(self.createdplaybuttontext,self.createdplaybuttontextcoll)
                """Mouses"""
                if self.createdplaybuttoncoll.collidepoint(self.mousepos) == True or self.randomplaybuttoncoll.collidepoint(self.mousepos) == True:
                    self.screen.blit(self.handcursor,self.mousepos)
                else:
                    self.screen.blit(self.defaultcursor,self.mousepos)
        except:
            pass

        """Control"""
        """Mouse Passes Over the Buttons"""
        """Random Map"""
        if self.randomplaybuttoncoll.collidepoint(self.mousepos) == True:
            self.screen.blit(self.buttonselector,self.randomplaybuttoncoll)
            self.screen.blit(self.handcursor,self.mousepos)
            if self.mouseclicked == True:
                self.mouseclicked = False
                self.menumusic.stop()
                returnedvalue = 'random'
        """Pre-Created Map"""
        if self.createdplaybuttoncoll.collidepoint(self.mousepos) == True:
            self.screen.blit(self.buttonselector,self.createdplaybuttoncoll)
            self.screen.blit(self.handcursor,self.mousepos)
            if self.mouseclicked == True:
                self.mouseclicked = False
                self.menumusic.stop()
                returnedvalue = 'pre'

        """System"""
        self.mouseoldpos = self.mousepos
        try:
            self.screenUpdate(self.clock,30)
        except:
            pass

        return returnedvalue

    def gameLoopView(self,M_surf,mapRect,mousepos,cursor):
        self.screen.fill((0,0,0))

        # Dibuja el mapa en la pantalla del display
        self.screen.blit(M_surf, mapRect)
        self.screen.blit(cursor,mousepos)
        
        try:
            self.screenUpdate(self.clock,60)
        except:
            pass
    
    def loadMap(self):
        """ """
        M_width = len(self.map) * self.tile_size
        M_height = len(self.map[0]) * self.tile_size
        M_surf = pygame.Surface((M_width, M_height))

        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                self.world.cellOff(x, y)
        
        for unit in range(len(self.world.Unit)):            
            positionX, positionY = self.world.Unit[unit].getPosition() # Obtiene la posicion del personaje
            for x in range(len(self.map)):
                for y in range(len(self.map[x])):

                    if ((x - positionX)**2 + (y - positionY)**2)**(1/2) <= 5:
                        self.world.revealCell(x, y) 

        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if ((x - positionX)**2 + (y - positionY)**2)**(1/2) <= 5:
                    self.world.revealCell(x, y) 

                if ((x - positionX)**2 + (y - positionY)**2)**(1/2) <= 5:
                    self.world.revealCell(x, y) 
                                
                if self.world.getVisibility(x, y) == (True, True):                
                    spaceRect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                    baseTile = self.biometiles[self.map[x][y]]

                 # Dibuja el la casilla con el bioma en la superficie
                    M_surf.blit(baseTile, spaceRect)
                else:
                    if self.world.getVisibility(x, y) == (False, True):
                        spaceRect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                        baseTile = self.biometiles[" " + self.map[x][y]]

                        # Dibuja el la casilla con el bioma en la superficie
                        M_surf.blit(baseTile, spaceRect)
                    else:
                        spaceRect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                        baseTile = self.biometiles[" "]

                        # Dibuja el la casilla con el bioma en la superficie
                        M_surf.blit(baseTile, spaceRect) 

        for x in range(self.units):
            positionX, positionY = self.world.Unit[x].getPosition()
            self.foundersprite = self.gameview.updateSprite((str(self.world.Unit[x].getSprite())))
            spaceRect = pygame.Rect(positionX * self.tile_size, positionY * self.tile_size, self.tile_size, self.tile_size)
            M_surf.blit(self.foundersprite, spaceRect)        
        return M_surf
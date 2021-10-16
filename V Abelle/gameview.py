import pygame
import gameresources as gameres
from systemcontroller import SystemController

pygame.init()

class GameView():
    def __init__(self):
        self.syscon = SystemController()
        self.screensx = 1280 #Is the width from the window
        self.screensy = 704 #Is the height from the window
        self.screensize = (self.screensx,self.screensy) #Is the size from the window
        self.screen = self.syscon.createScreen(self.screensize)
        self.windowicon,self.windowname,self.menufont,self.menufontlittle,self.menufontlittle2,self.buttonwoodtexture = gameres.systemLoads() #Uses the systemLoads function from gameresources
        self.clock = self.syscon.createClock() #Creates the clock function from the game
        self.mousepos = (0,0) #Records the position from the mouse
        self.screenlogo,self.screenlogocoll = gameres.screenLogo() #Uses the self.screenLogo function from gameresources
        self.loadingtext,self.loadingtextcoll,self.loadingbar,self.loadingbarcoll = gameres.menuesLoads(9)

        self.gamecontroll = SystemController()
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

    def loadBarView(self,mode):
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

            """Loads"""
            """Menues Loads"""
            if mode == 1:
                if loadingstep == 1:
                    loadingprogressvalue += 130
                if loadingstep == 10:
                    """Menues All"""
                    self.defaultbackground,self.menumusic,self.defaultcursor,self.handcursor = gameres.menuesLoads(1) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 130
                elif loadingstep == 15:
                    """Work In Progress"""
                    self.workinprogressmessage,self.underconstruction = gameres.menuesLoads(2) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 130
                elif loadingstep == 20:
                    """Exit"""
                    self.exitbackground,self.exitbackgroundpos,self.exittext,self.exittextpos,self.exitbuttonyes,self.exitbuttonyescoll,self.exitbuttonyestext,self.exitbuttonyestextcoll,self.exitbuttonno,self.exitbuttonnocoll,self.exitbuttonnotext,self.exitbuttonnotextcoll = gameres.menuesLoads(3) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 130
                elif loadingstep == 25:
                    """Map Selector"""
                    self.mapselectorbutton,self.mapselectorbuttoncoll,self.mapselectorbuttontext,self.mapselectorbuttontextcoll= gameres.menuesLoads(4) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 130
                elif loadingstep == 30:
                    """Credits"""
                    self.menubuttoncredits,self.menubuttoncreditstext,self.menubuttoncreditscoll,self.menubuttoncreditstextcoll = gameres.menuesLoads(5) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 130
                elif loadingstep == 35:
                    """Instructions"""
                    self.menubuttoninstructions,self.menubuttoninstructionstext,self.menubuttoninstructionscoll,self.menubuttoninstructionstextcoll = gameres.menuesLoads(6) #Uses the menuLoads function from gameresources
                    loading = False
            """Game Loads"""
            if mode == 2:
                if loadingstep == 1:
                    loadingprogressvalue += 195
                if loadingstep == 10:
                    """Play Random"""
                    self.randomplaybutton,self.randomplaybuttoncoll,self.randomplaybuttontext,self.randomplaybuttontextcoll = gameres.menuesLoads(7) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 195
                elif loadingstep == 15:
                    """Play Pre-Created"""
                    self.createdplaybutton,self.createdplaybuttoncoll,self.createdplaybuttontext,self.createdplaybuttontextcoll = gameres.menuesLoads(8) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 195
                elif loadingstep == 30:
                    """Game"""
                    self.swordcursor,self.foundersprite,self.founderspriteposx,self.founderspriteposy,self.founderspritecoll,self.biometiles,self.hidden = gameres.gameLoads(1) #Uses the gameLoads function from gameresources
                    loadingprogressvalue += 195
                elif loadingstep == 35:
                    self.gamemusic1,self.gamemusic2 = gameres.gameLoads(2) #Uses the gameLoads function from gameresources
                    loading = False

            self.clock.tick(30)
            pygame.display.update()

    def menuFirstDraw(self):
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

    def menuView(self):
        playing = True
        self.mouseclicked = False

        while playing == True:
            """Mouse Movement"""
            self.mousepos = self.gamecontroll.controlMouseMovement()

            """Events Manager"""
            self.event = self.gamecontroll.controlInputsEvents('menu')
            if self.event == 'exit':
                returnedvalue = 'exit'
                playing = False
            elif self.event == 'mouseon':
                self.mouseclicked = True

            """Draw Calls"""
            try:
                if mouseoldpos != self.mousepos:
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
                pygame.draw.rect(self.screen,[0,0,255],(self.mapselectorbuttoncoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.menumusic.stop()
                    returnedvalue = 'map'
                    playing = False
            """Credits"""
            if self.menubuttoncreditscoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttoncreditscoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    returnedvalue = 'crets'
                    playing = False
            """Instructions"""
            if self.menubuttoninstructionscoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttoninstructionscoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    returnedvalue = 'insts'
                    playing = False

            """System"""
            mouseoldpos = self.mousepos
            self.syscon.screenUpdate(self.clock,30)
    
        return returnedvalue

    def workInProgressFirstDraw(self):
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Under Construction"""
        self.screen.blit(self.workinprogressmessage,(275,300))
        self.screen.blit(self.underconstruction,(425,75))
    
    def workInProgressView(self):
        returnedvalue = ''
        playing = False
        
        while playing == True:
            """Mouse Movement"""
            self.mousepos = self.gamecontroll.controlMouseMovement()

            """Events Manager"""
            self.event = self.gamecontroll.controlInputsEvents('work')
            if self.event == 'exit':
                returnedvalue = 'exit'
                playing = False
            elif self.event == 'nonexit':
                returnedvalue = 'nonexit'
                playing = False
            
            """Draw Calls"""
            try:
                if oldmousepos != self.mousepos:
                    """Background"""
                    self.screen.blit(self.defaultbackground,(0,0))
                    """Under Construction"""
                    self.screen.blit(self.workinprogressmessage,(275,300))
                    self.screen.blit(self.underconstruction,(425,75))
                    self.screen.blit(self.defaultcursor,self.mousepos)
            except:
                pass            

            """System"""
            self.syscon.screenUpdate(self.clock,30)
            oldmousepos = self.mousepos

        return returnedvalue

    def exitUIFirstDraw(self):
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

    def exitUIView(self,gamemode):
        oldmousepos = None
        looping = True

        while looping == True:
            """Mouse Movement"""
            self.mousepos = self.gamecontroll.controlMouseMovement()

            """Events Manager"""
            self.event = self.gamecontroll.controlInputsEvents('exit')
            if self.event == 'mouseon':
                self.mouseclicked = True
            elif self.event == 'mouseoff':
                self.mouseclicked = False
            
            if oldmousepos != self.mousepos:
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
                    pygame.draw.rect(self.screen,[0,0,255],(self.exitbuttonyescoll))
                    self.screen.blit(self.handcursor,self.mousepos)
                    if self.mouseclicked == True:
                        self.mouseclicked = False
                        pygame.quit()
                        exit()
                """No"""
                if self.exitbuttonnocoll.collidepoint(self.mousepos) == True:
                    pygame.draw.rect(self.screen,[0,0,255],(self.exitbuttonnocoll))
                    self.screen.blit(self.handcursor,self.mousepos)
                    if self.mouseclicked == True:
                        self.mouseclicked = False
                        looping = False
            
            """System"""
            self.syscon.screenUpdate(self.clock,30)
            oldmousepos = self.mousepos

        if gamemode == 'random':
            return 'random'
        elif gamemode == 'created':
            return 'created'
        elif gamemode == 'menu':
            return 'menu'
        elif gamemode == 'credits':
            return 'credits'
        elif gamemode == 'instructions':
            return 'instructions'
        elif gamemode == 'mode':
            return 'mode'

    def creditsFirstDraw(self):
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Under Construction"""
        self.screen.blit(self.workinprogressmessage,(275,300))
        self.screen.blit(self.underconstruction,(425,75))

    def creditsView(self):
        playing = True
        returnedvalue = ' '

        while playing == True:
            """Mouse Movement"""
            self.mousepos = self.gamecontroll.controlMouseMovement()

            """Events Manager"""
            self.event = self.gamecontroll.controlInputsEvents('credits')
            if self.event == 'exit':
                returnedvalue = 'credits'
                playing = False
            elif self.event == 'nonexit':
                playing = False
            
            """Draw Calls"""
            """Background"""
            self.screen.blit(self.defaultbackground,(0,0))
            """Under Construction"""
            self.screen.blit(self.workinprogressmessage,(275,300))
            self.screen.blit(self.underconstruction,(425,75))
            self.screen.blit(self.defaultcursor,self.mousepos)

            """System"""
            self.syscon.screenUpdate(self.clock,30)
        
        return returnedvalue

    def instructionsFirstDraw(self):
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Under Construction"""
        self.screen.blit(self.workinprogressmessage,(275,300))
        self.screen.blit(self.underconstruction,(425,75))

    def instructionsView(self):
        playing = True
        returnedvalue = ' '

        while playing == True:
            """Mouse Movement"""
            self.mousepos = self.gamecontroll.controlMouseMovement()

            """Events Manager"""
            self.event = self.gamecontroll.controlInputsEvents('insts')
            if self.event == 'exit':
                returnedvalue = 'exit'
                playing = False
            elif self.event == 'nonexit':
                playing = False
            
            """Background"""
            self.screen.blit(self.defaultbackground,(0,0))
            """Under Construction"""
            self.screen.blit(self.workinprogressmessage,(275,300))
            self.screen.blit(self.underconstruction,(425,75))
            self.screen.blit(self.defaultcursor,self.mousepos)

            """System"""
            self.syscon.screenUpdate(self.clock,30)
    
        return returnedvalue

    def mapSelectorFirstDraw(self):
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

    def mapSeclectorView(self):
        playing = True
        returnedvalue = ''

        while playing == True:
            """Mouse Movement"""
            self.mousepos = self.gamecontroll.controlMouseMovement()

            """Events Manager"""
            self.event = self.gamecontroll.controlInputsEvents('map')
            if self.event == 'exit':
                returnedvalue = 'exit'
                playing = False
            elif self.event == 'nonexit':
                playing = False
            elif self.event == 'mouseon':
                self.mouseclicked = True

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

            """Control"""
            """Mouse Passes Over the Buttons"""
            """Random Map"""
            if self.randomplaybuttoncoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.randomplaybuttoncoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.menumusic.stop()
                    returnedvalue = 'random'
                    playing = False
            """Pre-Created Map"""
            if self.createdplaybuttoncoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.createdplaybuttoncoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.menumusic.stop()
                    returnedvalue = 'pre'
                    playing = False

            """System"""
            self.syscon.screenUpdate(self.clock,30)
        
        return returnedvalue



import pygame
from system_controller import SystemController

pygame.init()

class GameView():
    """  """
    def __init__(self):
        """Function __init__"""
        self.syscon = SystemController()
        
        #screen
        self.screenlogo,self.screenlogocoll = self.syscon.screenLogo()
        self.defaultbackground = None
        
        self.windowicon, self.windowname, self.buttontexture,self.buttonselector = self.syscon.systemLoads()

        #map selector button
        self.mapselectorbutton = None
        self.mapselectorbuttoncoll = None
        self.mapselectorbuttontext = None
        self.mapselectorbuttontextcoll = None

        self.event = None
        self.mouseclicked = None


    def loads(self):
        """  """
        self.defaultbackground,self.defaultcursor = self.syscon.menuesLoads(1)
        self.mapselectorbutton,self.mapselectorbuttoncoll,self.mapselectorbuttontext,self.mapselectorbuttontextcoll= self.syscon.menuesLoads(2)


    def menuFirstDraw(self):
        """Function menuFirstDraw, draws in the menu the basic draw"""
        #  Background
        self.screen.blit(self.defaultbackground,(0,0))
        #  Game Logo
        self.screen.blit(self.screenlogo,self.screenlogocoll)

        #  Play
        self.screen.blit(self.mapselectorbutton,self.mapselectorbuttoncoll)
    
    def menuView(self):
        """Function menuView, is the menu loop"""
        playing = True
        self.mouseclicked = False

        while playing == True:
            """Mouse Movement"""
            self.mousepos = self.syscon.controlMouseMovement()

            """Events Manager"""
            self.event = self.syscon.controlInputsEvents('menu')
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
                self.screen.blit(self.buttonselector,self.mapselectorbuttoncoll)
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.menumusic.stop()
                    returnedvalue = 'map'
                    playing = False
            """Credits"""
            if self.menubuttoncreditscoll.collidepoint(self.mousepos) == True:
                self.screen.blit(self.buttonselector,self.menubuttoncreditscoll)
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    returnedvalue = 'crets'
                    playing = False
            """Instructions"""
            if self.menubuttoninstructionscoll.collidepoint(self.mousepos) == True:
                self.screen.blit(self.buttonselector,self.menubuttoninstructionscoll)
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    returnedvalue = 'insts'
                    playing = False

            """System"""
            mouseoldpos = self.mousepos
            self.syscon.screenUpdate(self.clock,30)
    
        return returnedvalue
        
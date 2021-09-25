"""Libraries"""
import pygame
import sys
from pygame.constants import QUIT, SRCALPHA
from gameboard import GameBoard

"""Pygame Init"""
pygame.init()

class GameMain():

    """Function __init__"""
    def __init__(self):
        self.screensx = 1280
        self.screensy = 704
        self.mousepos = (0,0)
        self.playing = True
        self.mousedown = False
        self.keyup = False
        self.keydown = False
        self.keyleft = False
        self.keyright = False
        self.cameraup = False
        self.cameradown = False
        self.cameraleft = False
        self.cameraright = False
        self.mouseclicked = False
        self.screensize = (self.screensx,self.screensy)
        self.screen = pygame.display.set_mode(self.screensize)
        self.clock = pygame.time.Clock()
        self.menufont = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',100)
        self.menufontlittle = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',70)
        self.windowname = pygame.display.set_caption('T-H-E')
        self.windowiconload = pygame.image.load('resources/icons/windowicon.png')
        self.windowicon = pygame.display.set_icon(self.windowiconload)
        self.screenlogo = pygame.image.load('resources/icons/gamelogo.png')
        self.screenlogocoll = self.screenlogo.get_rect(center = (350,360))
        self.defaultbackground = pygame.image.load('resources/icons/menuback.jpg')
        """Buttons"""
        self.buttonwoodtexture = pygame.image.load('resources/icons/menubuttontexture.jpg')
        self.underconstruction = pygame.image.load('resources/icons/underconstruction.png').convert_alpha()
        """Exit"""
        self.exitbackground = pygame.image.load('resources/icons/exitback.png')
        self.exitbackground.set_alpha(5)
        self.exitbackgroundpos = (0,0)
        self.exittext = self.menufont.render('DO YOU WANT TO EXIT?',True,[255,255,255])
        self.exittextpos = (215,50)
        self.exitbuttonyes = self.buttonwoodtexture
        self.exitbuttonyescoll = self.exitbuttonyes.get_rect(center = (640,275))
        self.exitbuttonyestext = self.menufont.render('YES',True,[0,0,0])
        self.exitbuttonyestextcoll = self.exitbuttonyestext.get_rect(midleft = (585,275))
        self.exitbuttonno = self.buttonwoodtexture
        self.exitbuttonnocoll = self.exitbuttonno.get_rect(center = (640,425))
        self.exitbuttonnotext = self.menufont.render('NO',True,[0,0,0])
        self.exitbuttonnotextcoll = self.exitbuttonnotext.get_rect(midleft = (585,425))
        """Map Selector"""
        self.mapselectorbutton = self.buttonwoodtexture
        self.mapselectorbuttoncoll = self.mapselectorbutton.get_rect(midleft = (640,238))
        self.mapselectorbuttontext = self.menufontlittle.render('MAP SELECTION',True,[0,0,0])
        self.mapselectorbuttontextcoll = self.mapselectorbuttontext.get_rect(center = (952,230))
        """Credits"""
        self.menubuttoncredits = self.buttonwoodtexture
        self.menubuttoncreditstext = self.menufont.render('CREDITS',True,[0,0,0])
        self.menubuttoncreditscoll = self.menubuttoncredits.get_rect(midleft = (640,368))
        self.menubuttoncreditstextcoll = self.menubuttoncreditstext.get_rect(center = (952,368))
        self.creditstemporaly = self.menufont.render('WORK IN PROGRESS',True,[0,0,0])
        """Instructions"""
        self.menubuttoninstructions = self.buttonwoodtexture
        self.menubuttoninstructionstext = self.menufont.render('INSTRUCTIONS',True,[0,0,0])
        self.menubuttoninstructionscoll = self.menubuttoninstructions.get_rect(midleft = (640,498))
        self.menubuttoninstructionstextcoll = self.menubuttoninstructionstext.get_rect(center = (940,498))
        self.instructionstemporaly = self.menufont.render('WORK IN PROGRESS',True,[0,0,0])
        """Play Random"""
        self.randomplaybutton = self.buttonwoodtexture
        self.randomplaybuttoncoll = self.randomplaybutton.get_rect(midleft = (335,275))
        self.randomplaybuttontext = self.menufontlittle.render('PLAY RANDOM',True,[0,0,0])
        self.randomplaybuttontextcoll = self.randomplaybuttontext.get_rect(center = (635,275))
        """Play Pre-Created"""
        self.createdplaybutton = self.buttonwoodtexture
        self.createdplaybuttoncoll = self.createdplaybutton.get_rect(midleft = (335,425))
        self.createdplaybuttontext = self.menufontlittle.render('PLAY PRE-CREATED',True,[0,0,0])
        self.createdplaybuttontextcoll = self.createdplaybuttontext.get_rect(center = (635,425))
        """Game Resources"""
        self.gamebackground = pygame.image.load('resources/icons/mapsize.jpg')
        self.gamebackgroundscaled = pygame.transform.scale2x(self.gamebackground)
        self.defaultcursor = pygame.image.load('resources/icons/defaultcursor.png').convert_alpha()
        self.swordcursor = pygame.image.load('resources/icons/swordcursor.png').convert_alpha()
        self.handcursor = pygame.image.load('resources/icons/handcursor.png').convert_alpha()
        self.foundersprite = pygame.image.load('resources/icons/foundersprite.png')
        self.founderspritescaled = pygame.transform.scale2x(self.foundersprite)
        self.founderspriteposx = 515
        self.founderspriteposy = 325
        self.founderspritecoll = self.founderspritescaled.get_rect().move(self.founderspriteposx,self.founderspriteposy)
        self.nonreachables = []
        self.menuLoop()

    """Function menuLoop, is the menu loop"""
    def menuLoop(self):
        while True:

            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            """Events Manager"""
            for event in pygame.event.get():
                """Exit Event"""
                if event.type == pygame.QUIT:
                    self.exitUI('menu')
                """Mouse Events"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseclicked = True
                else:
                    self.mouseclicked = False

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
                    self.gameMapSelector(True)
            """Credits"""
            if self.menubuttoncreditscoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttoncreditscoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.creditsOpen(True)
            """Instructions"""
            if self.menubuttoninstructionscoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttoninstructionscoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.instructionsOpen(True)

            """System"""
            pygame.display.update()
            self.clock.tick(30)

    """Function exitUI, ask if you want to exit"""
    def exitUI(self,gamemode):
        while True:
            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(True)

            """Events Manager"""
            for event in pygame.event.get():
                """Mouse Events"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseclicked = True
                else:
                    self.mouseclicked = False
            
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
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    if gamemode == 'random':
                        self.randomMapMode(True)
                    elif gamemode == 'created':
                        self.preCreatedMapMode(True)
                    elif gamemode == 'menu':
                        self.menuLoop()
                    elif gamemode == 'credits':
                        self.creditsOpen(True)
                    elif gamemode == 'instructions':
                        self.instructionsOpen(True)
                    elif gamemode == 'mode':
                        self.gameMapSelector(True)
            
            """System"""
            pygame.display.update()
            self.clock.tick(30)

    """Function creditsOpen, put the credits on screen"""
    def creditsOpen(self,playing):
        self.playing = playing
        while self.playing == True:
            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            """Events Manager"""
            for event in pygame.event.get():
                """Exit Event"""
                if event.type == pygame.QUIT:
                    self.exitUI('credits')
                """Keyboard Events"""
                """Pressed"""
                if event.type == pygame.KEYDOWN:
                    """Escape"""
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
            
            """Draw Calls"""
            """Background"""
            self.screen.blit(self.defaultbackground,(0,0))
            """Under Construction"""
            self.screen.blit(self.creditstemporaly,(275,300))
            self.screen.blit(self.underconstruction,(425,75))
            self.screen.blit(self.defaultcursor,self.mousepos)

            """System"""
            pygame.display.update()
            self.clock.tick(30)

        self.menuLoop()

    """Function instructionsOpen, put the instructions on screen"""
    def instructionsOpen(self,playing):
        self.playing = playing
        while self.playing == True:
            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            """Events Manager"""
            for event in pygame.event.get():
                """Exit Event"""
                if event.type == pygame.QUIT:
                    self.exitUI('instructions')
                """Keyboard Events"""
                """Pressed"""
                if event.type == pygame.KEYDOWN:
                    """Escape"""
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
            
            """Background"""
            self.screen.blit(self.defaultbackground,(0,0))
            """Under Construction"""
            self.screen.blit(self.instructionstemporaly,(275,300))
            self.screen.blit(self.underconstruction,(425,75))
            self.screen.blit(self.defaultcursor,self.mousepos)

            """System"""
            pygame.display.update()
            self.clock.tick(30)

        self.menuLoop()

    """Function gameMapSelector, is the game map selector"""
    def gameMapSelector(self,playing):
        self.playing = playing
        while self.playing == True:

            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            """Events Manager"""
            for event in pygame.event.get():
                """Exit Event"""
                if event.type == pygame.QUIT:
                    self.exitUI('mode')
                """Keyboard Events"""
                """Pressed"""
                if event.type == pygame.KEYDOWN:
                    """Escape"""
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                """Mouse Events"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseclicked = True
                else:
                    self.mouseclicked = False

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
                    self.randomMapMode(True)
            """Pre-Created Map"""
            if self.createdplaybuttoncoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.createdplaybuttoncoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.preCreatedMapMode(True)
            
            """System"""
            pygame.display.update()
            self.clock.tick(30)

        self.menuLoop()
    
    """Function randomMapMode, plays the game on a random map"""
    def randomMapMode(self,playing):
        self.playing = playing
        world = GameBoard()
        offsetposy = 0
        offsetposx = 0
        while self.playing == True:

            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            """Events Manager"""
            for event in pygame.event.get():
                """Exit Event"""
                if event.type == pygame.QUIT:
                    self.exitUI('random')
                """Mouse Events"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mousedown = True
                """Keyboard Events"""
                """Pressed"""
                if event.type == pygame.KEYDOWN:
                    """Escape"""
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                    """Arrows"""
                    if event.key == pygame.K_UP and offsetposy <= 0 and offsetposy >= -1408:
                        self.cameraup = True
                    if event.key == pygame.K_DOWN and offsetposy <= 0 and offsetposy >= -1408:
                        self.cameradown = True
                    if event.key == pygame.K_LEFT and offsetposx <= 0 and offsetposx >= -2432:
                        self.cameraleft = True
                    if event.key == pygame.K_RIGHT and offsetposx <= 0 and offsetposx >= -2432:
                        self.cameraright = True
                    """Letters"""
                    if event.key == pygame.K_w:
                        self.keyup = True
                    if event.key == pygame.K_s:
                        self.keydown = True
                    if event.key == pygame.K_a:
                        self.keyleft = True
                    if event.key == pygame.K_d:
                        self.keyright = True
                """Released"""
                if event.type == pygame.KEYUP:
                    """Arrows"""
                    if event.key == pygame.K_UP and offsetposy <= 0 and offsetposy >= -1408:
                        self.cameraup = False
                    if event.key == pygame.K_DOWN and offsetposy <= 0 and offsetposy >= -1408:
                        self.cameradown = False
                    if event.key == pygame.K_LEFT and offsetposx <= 0 and offsetposx >= -2432:
                        self.cameraleft = False
                    if event.key == pygame.K_RIGHT and offsetposx <= 0 and offsetposx >= -2432:
                        self.cameraright = False
                    """Letters"""
                    if event.key == pygame.K_w:
                        self.keyup = False
                    if event.key == pygame.K_s:
                        self.keydown = False
                    if event.key == pygame.K_a:
                        self.keyleft = False
                    if event.key == pygame.K_s:
                        self.keyright = False

            """Draw Calls"""
            self.screen.fill([255,255,255])
            for Y in range(23):
                for X in range(40):
                    tile = pygame.transform.scale2x(pygame.image.load('resources/icons/map/floor/' + str(world.getTiles(Y, X)) + '.png').convert())
                    hidden =pygame.transform.scale2x(pygame.image.load('resources/icons/map/floor/offworld.png').convert())
                    x = 64 * X
                    y = 64 * Y

                    #Check map limit on X
                    if offsetposx >= 0:
                       offsetposx = 0 
                    if offsetposx <= -1280:
                        offsetposx = -1280
                    
                    #Check map limit on Y
                    if offsetposy >= 0:
                       offsetposy = 0 
                    if offsetposy <= -768:
                        offsetposy = -768
                    
                    if ((X-self.founderspriteposx/64)**2+(Y-self.founderspriteposy/64)**2)**(1/2) <= 3:
                        world.cells[Y][X].revealed = True

                    if world.cells[Y][X].revealed == True:
                        self.screen.blit(tile,(x + offsetposx,y + offsetposy))
                    else:
                        self.screen.blit(hidden,(x + offsetposx,y + offsetposy))

                    #Imposible cells
                    if world.getTiles(Y, X) == "mountain" or world.getTiles(Y,X) == "water":
                        self.nonreachables.append(str(x)+ " " +str(y))

            """Control"""
            """Character"""
            prevposx = self.founderspriteposx
            prevposy = self.founderspriteposy
            if self.keyup == True:
                self.founderspriteposy -= 64
            elif self.keyup == False:
                pass
            if self.keydown == True:
                self.founderspriteposy += 64
            elif self.keydown == False:
                pass
            if self.keyright == True:
                self.founderspriteposx += 64
            elif self.keyright == False:
                pass
            if self.keyleft == True:
                self.founderspriteposx -= 64
            elif self.keyleft == False:
                pass
            coord = str(self.founderspriteposx)+ " " + str(self.founderspriteposy)
            movementx = self.founderspriteposx + offsetposx
            movementy = self.founderspriteposy + offsetposy
            if not coord in self.nonreachables:
                self.founderspritecoll.move(movementx,movementy)
                self.screen.blit(self.founderspritescaled,(movementx,movementy))
            else:
                self.founderspriteposx = prevposx
                self.founderspriteposy = prevposy
            """Camera"""
            if self.cameraup == True:
                offsetposy += 64
            if self.cameradown == True:
                offsetposy -= 64
            if self.cameraright == True:
                offsetposx -= 64
            if self.cameraleft == True:
                offsetposx += 64

            """Cursor Draw Update"""
            if self.founderspritecoll.collidepoint(self.mousepos) == True:
                self.screen.blit(self.swordcursor,self.mousepos)
            else:
                self.screen.blit(self.defaultcursor,self.mousepos)

            """System"""
            pygame.display.update()
            self.clock.tick(60)

        self.gameMapSelector(True)

    """Function preCreatedMapMode, plays the game on pre-created map"""
    def preCreatedMapMode(self,playing):
        self.playing = playing
        offsetposy = 0
        offsetposx = 0
        while self.playing == True:

            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            """Events Manager"""
            for event in pygame.event.get():
                """Exit Event"""
                if event.type == pygame.QUIT:
                    self.exitUI('created')
                """Mouse Events"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mousedown = True
                """Keyboard Events"""
                """Pressed"""
                if event.type == pygame.KEYDOWN:
                    """Escape"""
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                    """Arrows"""
                    if event.key == pygame.K_UP and offsetposy <= 0 and offsetposy >= -1408:
                        self.cameraup = True
                    if event.key == pygame.K_DOWN and offsetposy <= 0 and offsetposy >= -1408:
                        self.cameradown = True
                    if event.key == pygame.K_LEFT and offsetposx <= 0 and offsetposx >= -2432:
                        self.cameraleft = True
                    if event.key == pygame.K_RIGHT and offsetposx <= 0 and offsetposx >= -2432:
                        self.cameraright = True
                    """Letters"""
                    if event.key == pygame.K_w:
                        self.keyup = True
                    if event.key == pygame.K_s:
                        self.keydown = True
                    if event.key == pygame.K_a:
                        self.keyleft = True
                    if event.key == pygame.K_d:
                        self.keyright = True
                """Released"""
                if event.type == pygame.KEYUP:
                    """Arrows"""
                    if event.key == pygame.K_UP and offsetposy <= 0 and offsetposy >= -1408:
                        self.cameraup = False
                    if event.key == pygame.K_DOWN and offsetposy <= 0 and offsetposy >= -1408:
                        self.cameradown = False
                    if event.key == pygame.K_LEFT and offsetposx <= 0 and offsetposx >= -2432:
                        self.cameraleft = False
                    if event.key == pygame.K_RIGHT and offsetposx <= 0 and offsetposx >= -2432:
                        self.cameraright = False
                    """Letters"""
                    if event.key == pygame.K_w:
                        self.keyup = False
                    if event.key == pygame.K_s:
                        self.keydown = False
                    if event.key == pygame.K_a:
                        self.keyleft = False
                    if event.key == pygame.K_s:
                        self.keyright = False

            """Draw Calls"""
            """Background"""
            self.screen.blit(self.gamebackgroundscaled,(0,0))
            """Camera"""
            for Y in range(23):
                for X in range(40):
                    #Check map limit on X
                    if offsetposx >= 0:
                       offsetposx = 0 
                    if offsetposx <= -1280:
                        offsetposx = -1280
                    
                    #Check map limit on Y
                    if offsetposy >= 0:
                       offsetposy = 0 
                    if offsetposy <= -768:
                        offsetposy = -768
            """Character"""
            coord = str(self.founderspriteposx)+ " " + str(self.founderspriteposy)
            movementx = self.founderspriteposx + offsetposx
            movementy = self.founderspriteposy + offsetposy
            self.founderspritecoll.move(movementx,movementy)
            self.screen.blit(self.founderspritescaled,(movementx,movementy))

            """Control"""
            """Character"""
            prevposx = self.founderspriteposx
            prevposy = self.founderspriteposy
            if self.keyup == True:
                self.founderspriteposy -= 64
            elif self.keyup == False:
                pass
            if self.keydown == True:
                self.founderspriteposy += 64
            elif self.keydown == False:
                pass
            if self.keyright == True:
                self.founderspriteposx += 64
            elif self.keyright == False:
                pass
            if self.keyleft == True:
                self.founderspriteposx -= 64
            elif self.keyleft == False:
                pass
            """Camera"""
            if self.cameraup == True:
                offsetposy += 64
            if self.cameradown == True:
                offsetposy -= 64
            if self.cameraright == True:
                offsetposx -= 64
            if self.cameraleft == True:
                offsetposx += 64

            """Cursor Draw Update"""
            if self.founderspritecoll.collidepoint(self.mousepos) == True:
                self.screen.blit(self.swordcursor,self.mousepos)
            else:
                self.screen.blit(self.defaultcursor,self.mousepos)

            """System"""
            pygame.display.update()
            self.clock.tick(60)

        self.gameMapSelector(True)

"""Main"""
if __name__ == '__main__':
    gameBegins = GameMain()
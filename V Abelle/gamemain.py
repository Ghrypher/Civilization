'''Libraries'''
import pygame
from pygame.constants import QUIT
import sys

'''Pygame Init'''
pygame.init()

class GameMain():

    '''Function __init__'''
    def __init__(self):
        self.screensx = 1280
        self.screensy = 736
        self.mousepos = (0,0)
        self.playing = True
        self.mousedown = False
        self.keyup = False
        self.keydown = False
        self.keyleft = False
        self.keyright = False
        self.mouseclicked = False
        self.screensize = (self.screensx,self.screensy)
        self.screen = pygame.display.set_mode(self.screensize)
        self.clock = pygame.time.Clock()
        self.menufont = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',100)
        self.windowname = pygame.display.set_caption('T-H-E')
        self.windowiconload = pygame.image.load('resources/icons/windowicon.png')
        self.windowicon = pygame.display.set_icon(self.windowiconload)
        self.screenlogo = pygame.image.load('resources/images/gamelogo.png')
        self.screenlogocoll = self.screenlogo.get_rect(center = (350,360))
        '''Buttons'''
        self.underconstruction = pygame.image.load('resources/images/underconstruction.png').convert_alpha()
        '''Play'''
        self.menubuttonplay = pygame.image.load('resources/images/menubuttontexture.jpg')
        self.menubuttonplaycoll = self.menubuttonplay.get_rect(midleft = (640,238))
        self.menubuttonplaytext = self.menufont.render('PLAY',True,[0,0,0])
        self.menubuttonplaytextcoll = self.menubuttonplaytext.get_rect(center = (952,230))
        '''Credits'''
        self.menubuttoncredits = pygame.image.load('resources/images/menubuttontexture.jpg')
        self.menubuttoncreditstext = self.menufont.render('CREDITS',True,[0,0,0])
        self.menubuttoncreditscoll = self.menubuttoncredits.get_rect(midleft = (640,368))
        self.menubuttoncreditstextcoll = self.menubuttoncreditstext.get_rect(center = (952,368))
        self.creditstemporaly = self.menufont.render('WORK IN PROGRESS',True,[0,0,0])
        '''Instructions'''
        self.menubuttoninstructions = pygame.image.load('resources/images/menubuttontexture.jpg')
        self.menubuttoninstructionstext = self.menufont.render('INSTRUCTIONS',True,[0,0,0])
        self.menubuttoninstructionscoll = self.menubuttoninstructions.get_rect(midleft = (640,498))
        self.menubuttoninstructionstextcoll = self.menubuttoninstructionstext.get_rect(center = (940,498))
        self.instructionstemporaly = self.menufont.render('WORK IN PROGRESS',True,[0,0,0])
        '''Game Resources'''
        self.gamebackground = pygame.image.load('resources/images/mapsize.jpg')
        self.gamebackgroundscaled = pygame.transform.scale2x(self.gamebackground)
        self.cursorswordico = pygame.image.load('resources/icons/cursorswordbasic.png').convert_alpha()
        self.foundersprite = pygame.image.load('resources/icons/foundersprite.png')
        self.founderspritescaled = pygame.transform.scale2x(self.foundersprite)
        self.founderspriteposx = 600
        self.founderspriteposy = 350
        self.founderspritecoll = self.founderspritescaled.get_rect(center = (600,350))
        self.menuLoop()

    '''Function gameLoop, is the game loop'''
    def gameLoop(self,playing):
        self.playing = playing
        while self.playing == True:

            '''Mouse'''
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            '''Events Manager'''
            for event in pygame.event.get():
                '''Mouse Events'''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mousedown = True
                '''Keyboard Events'''
                '''Pressed'''
                if event.type == pygame.KEYDOWN:
                    '''Arrows'''
                    if event.key == pygame.K_UP:
                        self.keyup = True
                    if event.key == pygame.K_DOWN:
                        self.keydown = True
                    if event.key == pygame.K_LEFT:
                        self.keyleft = True
                    if event.key == pygame.K_RIGHT:
                        self.keyright = True
                    '''Escape'''
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                '''Released'''
                '''Arrows'''
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.keyup = False
                    if event.key == pygame.K_DOWN:
                        self.keydown = False
                    if event.key == pygame.K_LEFT:
                        self.keyleft = False
                    if event.key == pygame.K_RIGHT:
                        self.keyright = False

            '''Draw Calls'''
            self.screen.fill([255,255,255])
            self.screen.blit(self.gamebackgroundscaled,(0,0))
            self.screen.blit(self.founderspritescaled,(self.founderspriteposx,self.founderspriteposy))
            self.screen.blit(self.cursorswordico,self.mousepos)

            '''Control'''
            if self.keyup == True:
                self.founderspriteposy -= 15
            if self.keydown == True:
                self.founderspriteposy += 15
            if self.keyright == True:
                self.founderspriteposx += 15
            if self.keyleft == True:
                self.founderspriteposx -= 15

            '''System'''
            pygame.display.update()
            self.clock.tick(60)

        self.menuLoop()

    '''Function creditsOpen, put the credits on screen'''
    def creditsOpen(self,playing):
        self.playing = playing
        while self.playing == True:
            '''Mouse'''
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            '''Events Manager'''
            for event in pygame.event.get():
                '''Keyboard Events'''
                '''Pressed'''
                if event.type == pygame.KEYDOWN:
                    '''Escape'''
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
            
            '''Draw Calls'''
            self.screen.fill([255,255,255])
            self.screen.blit(self.creditstemporaly,(275,300))
            self.screen.blit(self.underconstruction,(425,75))
            self.screen.blit(self.cursorswordico,self.mousepos)

            '''System'''
            pygame.display.update()
            self.clock.tick(60)

        self.menuLoop()

    '''Function instructionsOpen, put the instructions on screen'''
    def instructionsOpen(self,playing):
        self.playing = playing
        while self.playing == True:
            '''Mouse'''
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            '''Events Manager'''
            for event in pygame.event.get():
                '''Keyboard Events'''
                '''Pressed'''
                if event.type == pygame.KEYDOWN:
                    '''Escape'''
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
            
            '''Draw Calls'''
            self.screen.fill([255,255,255])
            self.screen.blit(self.instructionstemporaly,(275,300))
            self.screen.blit(self.underconstruction,(425,75))
            self.screen.blit(self.cursorswordico,self.mousepos)

            '''System'''
            pygame.display.update()
            self.clock.tick(60)

        self.menuLoop()

    '''Function menuLoop, is the menu loop'''
    def menuLoop(self):
        while True:

            '''Mouse'''
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(True)

            '''Events Manager'''
            for event in pygame.event.get():
                '''Exit Event'''
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                '''Mouse Events'''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseclicked = True
                else:
                    self.mouseclicked = False

            '''Draw Calls'''
            self.screen.fill([255,255,255])
            self.screen.blit(self.screenlogo,self.screenlogocoll)
            '''Buttons'''
            '''Play'''
            self.screen.blit(self.menubuttonplay,self.menubuttonplaycoll)
            self.screen.blit(self.menubuttonplaytext,self.menubuttonplaytextcoll)
            '''Credits'''
            self.screen.blit(self.menubuttoncredits,self.menubuttoncreditscoll)
            self.screen.blit(self.menubuttoncreditstext,self.menubuttoncreditstextcoll)
            '''Instructions'''
            self.screen.blit(self.menubuttoninstructions,self.menubuttoninstructionscoll)
            self.screen.blit(self.menubuttoninstructionstext,self.menubuttoninstructionstextcoll)

            '''Control'''
            '''Mouse Passes Over the Buttons'''
            '''Play'''
            if self.menubuttonplaycoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttonplaycoll))
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.gameLoop(True)
            '''Credits'''
            if self.menubuttoncreditscoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttoncreditscoll))
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.creditsOpen(True)
            '''Instructions'''
            if self.menubuttoninstructionscoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttoninstructionscoll))
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.instructionsOpen(True)

            '''System'''
            pygame.display.update()
            self.clock.tick(30)

'''Main'''
if __name__ == '__main__':
    gameBegins = GameMain()
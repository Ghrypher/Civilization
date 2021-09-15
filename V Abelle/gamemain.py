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
        self.keyupon = False
        self.keyupoff = True
        self.keydownon = False
        self.keydownoff = True
        self.keylefton = False
        self.keyleftoff = True
        self.keyrighton = False
        self.keyrightoff = True
        self.screensize = (self.screensx,self.screensy)
        self.screen = pygame.display.set_mode(self.screensize)
        self.clock = pygame.time.Clock()
        self.menufont = pygame.font.Font('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/V Abelle/resources/fonts/echantedland/Enchanted Land.otf',100)
        self.windowname = pygame.display.set_caption('T-H-E')
        self.windowiconload = pygame.image.load('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/V Abelle/resources/icons/windowicon.png')
        self.windowicon = pygame.display.set_icon(self.windowiconload)
        self.screenlogo = pygame.image.load('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/V Abelle/resources/images/gamelogo.png')
        self.screenlogocoll = self.screenlogo.get_rect(center = (350,360))
        self.menubuttonplay = pygame.image.load('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/V Abelle/resources/images/menubuttontexture.jpg')
        self.menubuttonplaycoll = self.menubuttonplay.get_rect(midleft = (640,250))
        self.menubuttonplaytext = self.menufont.render('PLAY',True,[0,0,0])
        self.menubuttonplaytextcoll = self.menubuttonplaytext.get_rect(center = (952,245))
        self.menubuttoncredits = pygame.image.load('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/V Abelle/resources/images/menubuttontexture.jpg')
        self.menubuttoncreditstext = self.menufont.render('CREDITS',True,[0,0,0])
        self.menubuttoncreditscoll = self.menubuttoncredits.get_rect(midleft = (640,450))
        self.menubuttoncreditstextcoll = self.menubuttoncreditstext.get_rect(center = (952,450))
        self.gamebackground = pygame.image.load('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/V Abelle/resources/images/mapsize.jpg')
        self.gamestart = False
        self.menuLoop()

    '''Function gameLoop, is the game loop'''
    def gameLoop(self,playing):
        self.playing = playing
        while self.playing == True:

            '''Get Mouse Position'''
            self.mousepos = pygame.mouse.get_pos()

            '''Events Manager'''
            for event in pygame.event.get():
                '''Mouse Events'''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mousedown = True
                '''Keyboard Events'''
                '''Arrows'''
                '''Pressed'''
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_UP:
                        self.keyupon = True
                    if event.type == pygame.K_DOWN:
                        self.keydownon = True
                    if event.type == pygame.K_LEFT:
                        self.keylefton = True
                    if event.type == pygame.K_RIGHT:
                        self.keyrighton = True
                    '''Escape'''
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                '''Released'''
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_UP:
                        self.keyupoff = False
                    if event.type == pygame.K_DOWN:
                        self.keydownoff = False
                    if event.type == pygame.K_LEFT:
                        self.keyleftoff = False
                    if event.type == pygame.K_RIGHT:
                        self.keyrightoff = False

            '''Draw Calls'''
            self.screen.fill([255,255,255])
            self.screen.blit(self.gamebackground,(0,0))

            '''Control'''
                
            '''System'''
            pygame.mouse.set_visible(True)
            pygame.display.update()
            self.clock.tick(30)
        self.menuLoop()

    '''Function menuLoop, is the menu loop'''
    def menuLoop(self):
        while True:

            '''Internal Variables'''
            self.mousepos = pygame.mouse.get_pos()

            '''Events Manager'''
            for event in pygame.event.get():
                '''Exit Event'''
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                '''Mouse Events'''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.gamestart = True

            '''Draw Calls'''
            self.screen.fill([255,255,255])
            self.screen.blit(self.screenlogo,self.screenlogocoll)
            self.screen.blit(self.menubuttonplay,self.menubuttonplaycoll)
            self.screen.blit(self.menubuttonplaytext,self.menubuttonplaytextcoll)
            self.screen.blit(self.menubuttoncredits,self.menubuttoncreditscoll)
            self.screen.blit(self.menubuttoncreditstext,self.menubuttoncreditstextcoll)

            '''Control'''
            '''Mouse Passes Over the Buttons'''
            if self.menubuttonplaycoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttonplaycoll))
            if self.menubuttoncreditscoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttoncreditscoll))
            if self.gamestart == True:
                self.gamestart = False
                self.gameLoop(True)

            '''System'''
            pygame.mouse.set_visible(True)
            pygame.display.update()
            self.clock.tick(30)

'''Main'''
if __name__ == '__main__':
    gameBegins = GameMain()
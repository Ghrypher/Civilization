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
        self.screensy = 720
        self.screensize = (self.screensx,self.screensy)
        self.screen = pygame.display.set_mode(self.screensize)
        self.clock = pygame.time.Clock()
        self.menufont = pygame.font.Font('resources/fonts/echantedland/Enchanted Land.otf',100)
        self.windowname = pygame.display.set_caption('T-H-E')
        self.windowiconload = pygame.image.load('resources/icons/windowicon.png')
        self.windowicon = pygame.display.set_icon(self.windowiconload)
        self.screenlogo = pygame.image.load('resources/images/gamelogo.png')
        self.screenlogocoll = self.screenlogo.get_rect(center = (350,360))
        self.menubuttonplay = pygame.image.load('resources/images/menubuttontexture.jpg')
        self.menubuttonplaycoll = self.menubuttonplay.get_rect(midleft = (640,250))
        self.menubuttonplaytext = self.menufont.render('PLAY',True,[0,0,0])
        self.menubuttonplaytextcoll = self.menubuttonplaytext.get_rect(center = (952,245))
        self.menubuttoncredits = pygame.image.load('resources/images/menubuttontexture.jpg')
        self.menubuttoncreditstext = self.menufont.render('CREDITS',True,[0,0,0])
        self.menubuttoncreditscoll = self.menubuttoncredits.get_rect(midleft = (640,450))
        self.menubuttoncreditstextcoll = self.menubuttoncreditstext.get_rect(center = (952,450))
        self.gameLoop()

    '''Function gameLoop, is the game loop'''
    def gameLoop(self):
        while True:

            '''Internal Variables'''
            mousepos = (1279, 29)
            mousepos = pygame.mouse.get_pos()

            '''Events Manager'''
            for event in pygame.event.get():
                '''Exit Event'''
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                '''Mouse Events'''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()

            '''Draw Calls'''
            self.screen.fill([255,255,255])
            self.screen.blit(self.screenlogo,self.screenlogocoll)
            self.screen.blit(self.menubuttonplay,self.menubuttonplaycoll)
            self.screen.blit(self.menubuttonplaytext,self.menubuttonplaytextcoll)
            self.screen.blit(self.menubuttoncredits,self.menubuttoncreditscoll)
            self.screen.blit(self.menubuttoncreditstext,self.menubuttoncreditstextcoll)

            '''Control'''
            '''Mouse Passes Over the Buttons'''
            if self.menubuttonplaycoll.collidepoint(mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttonplaycoll))
            if self.menubuttoncreditscoll.collidepoint(mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttoncreditscoll))

            '''System'''
            pygame.mouse.set_visible(True)
            pygame.display.update()
            self.clock.tick(30)

'''Main'''
if __name__ == '__main__':
    gameBegins = GameMain()
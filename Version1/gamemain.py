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
        self.menufont = pygame.font.Font('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/resources/fonts/echantedland/Enchanted Land.otf',100)
        self.windowname = pygame.display.set_caption('T-H-E')
        self.windowiconload = pygame.image.load('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/resources/icons/windowicon.png')
        self.windowicon = pygame.display.set_icon(self.windowiconload)
        self.screenlogo = pygame.image.load('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/resources/images/gamelogo.png')
        self.screenlogocoll = self.screenlogo.get_rect(center = (350,360))
        self.menubuttonplay = pygame.image.load('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/resources/images/menubuttontexture.jpg')
        self.menubuttonplaycoll = self.menubuttonplay.get_rect(midleft = (640,360))
        self.menubuttonplaytext = self.menufont.render('PLAY',True,[0,0,0])
        self.menubuttonplaytextcoll = self.menubuttonplaytext.get_rect(center = (952,355))
        self.gameLoop()

    '''Function gameLoop, is the game loop'''
    def gameLoop(self):
        while True:
            for event in pygame.event.get():
                '''Exit Event'''
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                '''Mouse Events'''
                if event.type == pygame.MOUSEMOTION:
                    mousepos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()

            '''Draw Calls'''
            self.screen.fill([255,255,255])
            self.screen.blit(self.screenlogo,self.screenlogocoll)
            self.screen.blit(self.menubuttonplay,self.menubuttonplaycoll)
            self.screen.blit(self.menubuttonplaytext,self.menubuttonplaytextcoll)

            '''Control'''
            '''Mouse Passes Over the Button'''
            if self.menubuttonplaycoll.collidepoint(mousepos):
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttonplaycoll))

            '''System'''
            pygame.display.update()
            self.clock.tick(60)

'''Main'''
if __name__ == '__main__':
    gameBegins = GameMain()
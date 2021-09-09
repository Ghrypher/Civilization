import pygame
from pygame.constants import QUIT
import sys

pygame.init()

class GameMain():

    '''Function __init__'''
    def __init__(self):
        self.screensx = 1280
        self.screensy = 720
        self.screensize = (self.screensx,self.screensy)
        self.screen = pygame.display.set_mode(self.screensize)
        self.clock = pygame.time.Clock()
        self.gameLoop()

    '''Function gameLoop, is the game loop'''
    def gameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill([255,255,255])

            pygame.display.update()
            self.clock.tick(30)

'''Main'''
if __name__ == '__main__':
    gameBegins = GameMain()
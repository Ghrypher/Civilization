import pygame

pygame.init()

class SystemController():
    def __init__(self):
        self.event = None
        self.mousepos = None

    def controlInputsEvents(self,mode):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                return 'exit'
            """For All Except Credits, Instructions"""
            if mode != 'credits' or mode != 'insts':
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    return 'mouseon'
            """Only for WorkInProgress, Credits, Instructions, MapSelector"""
            if mode == 'work' or mode == 'credits' or mode == 'insts' or mode == 'map':
                if self.event.type == pygame.KEYDOWN:
                    """Escape"""
                    if self.event.key == pygame.K_ESCAPE:
                        return 'nonexit'

    def controlMouseMovement(self):
        self.mousepos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        return self.mousepos

    def createScreen(self,screensize):
        screen = pygame.display.set_mode(screensize, pygame.RESIZABLE)
        return screen

    def createClock(self):
        clock = pygame.time.Clock()
        return clock

    def screenUpdate(self,clock,fps):
        pygame.display.update()
        clock.tick(fps)
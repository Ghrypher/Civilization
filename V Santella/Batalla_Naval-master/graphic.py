from tablero import Tablero
import pygame

pygame.init()

class Graphic:
    """ clase Jugador encargada de cambiar el turno y crear nuevas partidas """

    def __init__(self):
        """ constructor de la clase """
        self.world = None
        self.screen = None
        self.generate_world()


    def generate_world(self):
        self.screen = pygame.display.set_mode((1280,704))
        self.world = Tablero()
        for Y in range(23):
            for X in range(40):
                tile = pygame.image.load('asets/floor/' + str(self.world.get_tiles(Y, X)) + '.png').convert()
                x = 32 * X
                y = 32 * Y
                self.screen.blit(tile,(x, y))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.display.update()


G = Graphic()
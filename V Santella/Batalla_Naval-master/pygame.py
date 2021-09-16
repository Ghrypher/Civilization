from tablero import Tablero
import pygame

pygame.init()

class Graphic:
    """ clase Jugador encargada de cambiar el turno y crear nuevas partidas """

    def __init__(self):
        """ constructor de la clase """
        self.generate_world()
        self.world = None
        self.screen = None

    def generate_world(self):
        screen = pygame.display.set_mode((1280,736))
        self.world = Tablero()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

        """for Y in range(23):
            for x in range(40):
                self.screen.blit(self.world.cells[y][x].tile,)"""
        

P = Graphic()
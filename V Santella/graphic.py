from tablero import Tablero
import pygame

pygame.init()

class Graphic:
    """ clase Jugador encargada de cambiar el turno y crear nuevas partidas """

    def __init__(self):
        """ constructor de la clase """
        self.world = None
        self.screen = None
        self.character_pos_x = 576  
        self.character_pos_y = 320
        self.non_reachables = []
        self.character = pygame.image.load('asets/characters/Main.png')
        self.generate_world()

    def generate_world(self):
        self.screen = pygame.display.set_mode((1280,704))
        self.world = Tablero()
        while True:
            for event in pygame.event.get():
                mov_pos_y = 0
                mov_pos_x = 0
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        mov_pos_y = -64
                    if event.key == pygame.K_s:
                        mov_pos_y = 64
                    if event.key == pygame.K_a:
                        mov_pos_x = -64
                    if event.key == pygame.K_d:
                        mov_pos_x = 64
            for Y in range(23):
                for X in range(40):
                    tile = pygame.transform.scale2x(pygame.image.load('asets/floor/' + str(self.world.get_tiles(Y, X)) + '.png').convert())
                    x = 64 * X
                    y = 64 * Y
                    self.screen.blit(tile,(x, y))
                    if self.world.get_tiles(Y, X) == "Mountains" or self.world.get_tiles(Y, X) == "Water":
                        self.non_reachables.append(x)
                        self.non_reachables.append(y)

            prev_pos_x =self.character_pos_x
            prev_pos_y =self.character_pos_y
            self.character_pos_x += mov_pos_x
            self.character_pos_y += mov_pos_y
            if not self.character_pos_x in self.non_reachables and self.character_pos_y in self.non_reachables:
                self.character_pos_x = prev_pos_x
                self.character_pos_y = prev_pos_y

            self.screen.blit(self.character,(self.character_pos_x, self.character_pos_y))
            mov_pos_y = 0
            mov_pos_x = 0
            pygame.display.update()
            


G = Graphic()
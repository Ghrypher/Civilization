from tablero import Tablero
import pygame

pygame.init()

class Graphic:
    """ clase graphic encargada del apartado grafico """

    def __init__(self):
        """ constructor de la clase """
        self.world = None
        self.screen = None
        self.character_pos_x = 576  
        self.character_pos_y = 320
        self.tile_size = 32
        self.non_reachables =[]
        self.screen = pygame.display.set_mode((1056,544))
        self.character = pygame.image.load('asets/characters/Fundador_temp.png').convert()
        self.generate_world()

    def generate_world(self):
        """ funcion encargada de crear el mundo y adminstrar personajes """
        self.world = Tablero()
        offset_pos_y = 0
        offset_pos_x = 0
        self.blit(offset_pos_x, offset_pos_y)
        while True:
            for event in pygame.event.get():
                mov_pos_y = 0
                mov_pos_x = 0
                
                #salir del juego con cruz
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.KEYUP:

                    #movimiento del personaje
                    if event.key == pygame.K_w:
                        mov_pos_y = -self.tile_size
                    if event.key == pygame.K_s:
                        mov_pos_y = self.tile_size
                    if event.key == pygame.K_a:
                        mov_pos_x = -self.tile_size
                    if event.key == pygame.K_d:
                        mov_pos_x = self.tile_size
                    
                    #movimiento del mapa
                    if event.key == pygame.K_UP and offset_pos_y <= -32:
                        offset_pos_y += self.tile_size
                    if event.key == pygame.K_DOWN and offset_pos_y >= -160:
                        offset_pos_y -= self.tile_size
                    if event.key == pygame.K_LEFT and offset_pos_x <= -32:
                        offset_pos_x += self.tile_size
                    if event.key == pygame.K_RIGHT and offset_pos_x >= -192:
                        offset_pos_x -= self.tile_size
                    
                    self.blit(offset_pos_x, offset_pos_y)
            
            #posicion previa
            prev_pos_x =self.character_pos_x
            prev_pos_y =self.character_pos_y
            #posicion nueva
            self.character_pos_x += mov_pos_x
            self.character_pos_y += mov_pos_y
            coord= str(self.character_pos_x)+ " " + str(self.character_pos_y)

            #revisar si la celda esta libre
            if not coord in self.non_reachables:
                self.screen.blit(self.character,(self.character_pos_x + offset_pos_x, self.character_pos_y + offset_pos_y))
            else:
                self.character_pos_x = prev_pos_x
                self.character_pos_y = prev_pos_y
            mov_pos_y = 0
            mov_pos_x = 0
            
            pygame.display.update()
        
    def blit(self, offset_pos_x, offset_pos_y): 
        for Y in range(23):
                for X in range(40):
                    #obtencion de pngs
                    tile = pygame.image.load('asets/floor/' + str(self.world.get_tiles(Y, X)) + '.png').convert()
                    hidden =pygame.image.load('asets/floor/off_world.png').convert()
                    x = self.tile_size * X
                    y = self.tile_size * Y
                    
                    if ((X-self.character_pos_x/self.tile_size)**2 + (Y-self.character_pos_y/self.tile_size)**2)**(1/2) <= 50:
                        self.world.cells[Y][X].revealed = True

                    if self.world.cells[Y][X].revealed == True:
                        self.screen.blit(tile,(x + offset_pos_x,y + offset_pos_y))
                    else:
                        self.screen.blit(hidden,(x + offset_pos_x,y + offset_pos_y))

                    # guadado de celdas inalcanzables
                    if self.world.get_tiles(Y, X) == "Mountain" or self.world.get_tiles(Y, X) == "Water" or Y == 0 or X == 0:
                        self.non_reachables.append(str(x)+ " " +str(y))
    
    def Load_map (self):
        
        M_width = len(M_Obj) * self.tile_size
        M_height = len(M_Obj[0]) * self.tile_size

        M_surf = pygame.surface((M_width, M_height))

G = Graphic()
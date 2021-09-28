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
        self.non_reachables =[]
        self.character = pygame.image.load('asets/characters/Main.png')
        self.generate_world()

    def generate_world(self):
        """ funcion encargada de crear el mundo y adminstrar personajes """
        self.screen = pygame.display.set_mode((1280,704))
        self.world = Tablero()
        offset_pos_y = 0
        offset_pos_x = 0
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
                        mov_pos_y = -64
                    if event.key == pygame.K_s:
                        mov_pos_y = 64
                    if event.key == pygame.K_a:
                        mov_pos_x = -64
                    if event.key == pygame.K_d:
                        mov_pos_x = 64
                    
                    #movimiento del mapa
                    if event.key == pygame.K_UP and offset_pos_y <= 0 and offset_pos_y >= -1408:
                        offset_pos_y += 64
                    if event.key == pygame.K_DOWN and offset_pos_y <= 0 and offset_pos_y >= -1408:
                        offset_pos_y -= 64
                    if event.key == pygame.K_LEFT and offset_pos_x <= 0 and offset_pos_x >= -2432:
                        offset_pos_x += 64
                    if event.key == pygame.K_RIGHT and offset_pos_x <= 0 and offset_pos_x >= -2432:
                        offset_pos_x -= 64
                
            for Y in range(23):
                for X in range(40):
                    #obtencion de pngs
                    tile = pygame.transform.scale2x(pygame.image.load('asets/floor/' + str(self.world.get_tiles(Y, X)) + '.png').convert())
                    hidden =pygame.transform.scale2x(pygame.image.load('asets/floor/off_world.png').convert())
                    x = 64 * X
                    y = 64 * Y

                    # chequeo del limite del mapa en x
                    if offset_pos_x >= 0:
                       offset_pos_x = 0 
                    if offset_pos_x <= -1280:
                        offset_pos_x = -1280
                    
                    # chequeo del limite del mapa en y
                    if offset_pos_y >= 0:
                       offset_pos_y = 0 
                    if offset_pos_y <= -768:
                        offset_pos_y = -768
                    
                    if ((X-self.character_pos_x/64)**2+(Y-self.character_pos_y/64)**2)**(1/2) <= 3:
                        self.world.cells[Y][X].revealed = True

                    if self.world.cells[Y][X].revealed == True:
                        self.screen.blit(tile,(x + offset_pos_x,y + offset_pos_y))
                    else:
                        self.screen.blit(hidden,(x + offset_pos_x,y + offset_pos_y))

                    # guadado de celdas inalcanzables
                    if self.world.get_tiles(Y, X) == "Mountain" or self.world.get_tiles(Y, X) == "Water":
                        self.non_reachables.append(str(x)+ " " +str(y))

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
            


G = Graphic()
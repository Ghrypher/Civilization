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
        self.mousepos = (0,0)
        self.screen = pygame.display.set_mode((1280,704))
        self.clock = pygame.time.Clock()
        self.mouse_img = pygame.image.load('asets/menus/Mouse.png')
        self.character = pygame.image.load('asets/characters/Main.png')
        self.filtro = pygame.image.load('asets/menus/Menu_Filter.png')
        self.hidden = pygame.transform.scale2x(pygame.image.load('asets/floor/off_world.png').convert())
        # start menu
        self.screenlogo = pygame.transform.scale2x(pygame.image.load('asets/menus/logo.png'))
        self.screenlogocoll = self.screenlogo.get_rect(center = (350,360))
        # play button
        self.menu_button_play_p = pygame.image.load('asets/menus/menu_button_play_pressed.png')
        self.menu_button_play = pygame.image.load('asets/menus/menu_button_play.png')
        self.menubuttonplaycoll = self.menu_button_play.get_rect(midleft = (640,238))
        pygame.display.set_icon(pygame.image.load('asets/menus/icon.png'))
        pygame.display.set_caption('Civilization_POO')
        self.menu_loop()

    def menu_loop(self):
        self.world = Tablero()
        while True:

            '''Mouse'''
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(True)

            '''Events Manager'''
            for event in pygame.event.get():
                # Exit Event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # Mouse Events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseclicked = True
                else:
                    self.mouseclicked = False

            # Draw Calls

            self.Load_background()
            self.screen.blit(self.screenlogo,self.screenlogocoll)
            
            # Play button 
            self.screen.blit(self.menu_button_play,self.menubuttonplaycoll)
            if self.menubuttonplaycoll.collidepoint(self.mousepos) == True:
                self.screen.blit(self.menu_button_play_p,(self.menubuttonplaycoll))
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.game_loop()

            '''System'''
            pygame.display.update()
            self.clock.tick(30)

    def game_loop(self):
        """ funcion encargada de crear el mundo y adminstrar personajes """
        self.world = Tablero()
        offset_pos_y = 0
        offset_pos_x = 0
        mov_pos_y = 0
        mov_pos_x = 0
        loop = True
        while loop:
            '''Mouse'''
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

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
                    if event.key == pygame.K_ESCAPE:
                        loop = False
                    
                    #movimiento del mapa
                    if event.key == pygame.K_UP and offset_pos_y <= 0 and offset_pos_y >= -1408:
                        offset_pos_y += 64
                    if event.key == pygame.K_DOWN and offset_pos_y <= 0 and offset_pos_y >= -1408:
                        offset_pos_y -= 64
                    if event.key == pygame.K_LEFT and offset_pos_x <= 0 and offset_pos_x >= -2432:
                        offset_pos_x += 64
                    if event.key == pygame.K_RIGHT and offset_pos_x <= 0 and offset_pos_x >= -2432:
                        offset_pos_x -= 64

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

            self.generate_world(offset_pos_x, offset_pos_y)    
            self. check_charac_pos(mov_pos_x, mov_pos_y, offset_pos_x, offset_pos_y)

            mov_pos_y = 0
            mov_pos_x = 0

            self.screen.blit(self.mouse_img,self.mousepos)
            pygame.display.update()
            self.clock.tick(60)
        self.menu_loop()
    
    def generate_world(self, offset_pos_x, offset_pos_y):
        for Y in range(23):
                for X in range(40):
                    #obtencion de pngs
                    tile = pygame.transform.scale2x(pygame.image.load('asets/floor/' + str(self.world.get_tiles(Y, X)) + '.png').convert())
                    x = 64 * X
                    y = 64 * Y
                    
                    if ((X-self.character_pos_x/64)**2+(Y-self.character_pos_y/64)**2)**(1/2) <= 5:
                        self.world.cells[Y][X].active = True
                    """else:
                        self.world.cells[Y][X].active = False"""

                    if self.world.cells[Y][X].active == True:
                        self.screen.blit(tile,(x + offset_pos_x,y + offset_pos_y))
                    else:
                        self.screen.blit(self.hidden,(x + offset_pos_x,y + offset_pos_y))

                    # guadado de celdas inalcanzables
                    if self.world.get_tiles(Y, X) == "Mountain" or self.world.get_tiles(Y, X) == "Water" or Y == 0 or X == 0 or Y == 22 or X == 39:
                        self.non_reachables.append(str(x)+ " " +str(y))
    
    def check_charac_pos(self, mov_pos_x, mov_pos_y, offset_pos_x, offset_pos_y):
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
    
    def Load_background(self):
        for Y in range(12):
                for X in range(21):
                    tile = pygame.transform.scale2x(pygame.image.load('asets/floor/' + str(self.world.get_tiles(Y, X)) + '.png').convert())
                    x = 64 * X
                    y = 64 * Y
                    self.screen.blit(tile,(x - 64,y - 64))
        self.screen.blit(self.filtro,(0, 0))

G = Graphic()
from tablero import Tablero
import random, sys, copy, os, pygame
from pygame.locals import *

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
        self.mousepos = (0,0)
        self.M_Obj = None
        self.screen = pygame.display.set_mode((1280,704))
        self.clock = pygame.time.Clock()
        self.mouse_img = pygame.image.load('asets/menus/Mouse.png')
        self.character = pygame.image.load('asets/characters/Fundador_temp.png')
        self.filtro = pygame.image.load('asets/menus/Menu_Filter.png')
        self.hidden = pygame.image.load('asets/floor/off_world.png').convert()
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

    def game_loop(self):
        """ funcion encargada de crear el mundo y adminstrar personajes """
        self.world = Tablero()
        self.world.random_world()
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
                    
            self.generate_Random_world(offset_pos_x, offset_pos_y)  
            self.check_charac_pos(mov_pos_x, mov_pos_y, offset_pos_x, offset_pos_y)

            mov_pos_y = 0
            mov_pos_x = 0

            self.screen.blit(self.mouse_img,self.mousepos)
            pygame.display.update()
            self.clock.tick(60)
        self.menu_loop()
    
    def generate_Random_world(self, offset_pos_x, offset_pos_y):
        for Y in range(23):
                for X in range(40):
                    #obtencion de pngs
                    tile = pygame.image.load('asets/floor/' + str(self.world.get_tiles(Y, X)) + '.png').convert()
                    x = self.tile_size * X
                    y = self.tile_size * Y
                    
                    if ((X-self.character_pos_x/self.tile_size)**2 + (Y-self.character_pos_y/self.tile_size)**2)**(1/2) <= 50:
                        self.world.cells[Y][X].revealed = True

                    if self.world.cells[Y][X].revealed == True:
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
        
    def blit(self, offset_pos_x, offset_pos_y): 
        """ """
    
    def Load_map (self, M_Obj):
        """ """
        
        M_width = len(M_Obj) * self.tile_size
        M_height = len(M_Obj[0]) * self.tile_size

        M_surf = pygame.surface((M_width, M_height))
    
    def Read_Map (self, file):
        """ """
        assert os.path.exists(file), 'Cannot find the level file: %s' % (file)
        M_File = open(file, "r")
        content = M_File.readlines() + ["\r\n"]
        M_File.close()

        M_TextLines = []
        M_Obj = []

        for lineNum in range(len(content)):
            line = content[lineNum].rstrip('\r\n')

            # Si encuentra un ";" en la linea actual devuelve ""
            if ";" in line:
                line = line[:line.find(";")]

            # Si tiene algo lo añade a la lista con las lineas de texto del mapa
            if line != "":
                M_TextLines.append(line)

            elif line == "" and len(M_TextLines) > 0:
                maxWidth = -1

                # Busca la fila mas larga de todas
                for i in range(len(M_TextLines)):
                    if len(M_TextLines[i]) > maxWidth:
                        maxWidth = len(M_TextLines[i])

                # Las empareja llenando con espacios si es que hace falta
                for i in range (len(M_TextLines)):
                    M_TextLines[i] += " " * (maxWidth - len(M_TextLines[i]))

                # Añade una lista por cada linea de mapa
                for x in range (len(M_TextLines[0])):
                    M_Obj.append([])

                # Invierte el mapa para que quede al derecho en la matriz
                for y in range (len(M_TextLines)):
                    for x in range (maxWidth):
                        M_Obj[x].append(M_TextLines[y][x])
        return M_Obj

    def menu_loop(self):
        self.world = Tablero()
        self.world.background_world()
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
                    self.M_Obj = self.Read_Map("maps/map1.txt")
            
            # Play button 
            self.screen.blit(self.menu_button_play,self.menubuttonplaycoll + 100)
            if self.menubuttonplaycoll.collidepoint(self.mousepos) == True:
                self.screen.blit(self.menu_button_play_p,(self.menubuttonplaycoll))
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.game_loop()
                    self.M_Obj = self.Read_Map("maps/map1.txt")

            '''System'''
            pygame.display.update()
            self.clock.tick(30)
        
    def Load_background(self):
        for Y in range(23):
            for X in range(40):
                tile = pygame.image.load('asets/floor/' + str(self.world.get_tiles(Y, X)) + '.png').convert()
                x = self.tile_size * X
                y = self.tile_size * Y
                self.screen.blit(tile,(x ,y))
        self.screen.blit(self.filtro,(0, 0))

G = Graphic()
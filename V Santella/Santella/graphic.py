from tablero import Tablero
import random, sys, copy, os, pygame
from pygame.locals import *

pygame.init()
Map_to_Tile = {"X": pygame.image.load("asets/floor/Dirt.png"),
                  "Y": pygame.image.load("asets/floor/Mountain.png"),
                  "M": pygame.image.load("asets/floor/Water.png")}

class Graphic:
    """ clase graphic encargada del apartado grafico """

    def __init__(self):
        """ constructor de la clase """
        self.world = None
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
        self.screenlogocoll = self.screenlogo.get_rect(center = (350, 360))
        # play button
        self.menu_button_play_p = pygame.image.load('asets/menus/menu_button_play_pressed.png')
        self.menu_button_play = pygame.image.load('asets/menus/menu_button_play.png')
        self.menubuttonplaycoll = self.menu_button_play.get_rect(midleft = (640, 238))
        self.menubuttonplaycoll_2 = self.menu_button_play.get_rect(midleft = (640, 476))
        pygame.display.set_icon(pygame.image.load('asets/menus/icon.png'))
        pygame.display.set_caption('Civilization_POO')
        self.menu_loop()

    def random_game_loop(self):
        """ funcion encargada de crear el mundo y adminstrar personajes """
        self.world = Tablero(40, 23)
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

                if event.type == pygame.KEYDOWN:

                    #movimiento del personaje
                    if event.key == K_w:
                        mov_pos_y = -self.tile_size
                    if event.key == K_s:
                        mov_pos_y = self.tile_size
                    if event.key == K_a:
                        mov_pos_x = -self.tile_size
                    if event.key == K_d:
                        mov_pos_x = self.tile_size
                    
                    #movimiento del mapa
                    if event.key == K_UP and offset_pos_y <= -32:
                        offset_pos_y += self.tile_size
                    if event.key == K_DOWN and offset_pos_y >= -160:
                        offset_pos_y -= self.tile_size
                    if event.key == K_LEFT and offset_pos_x <= -32:
                        offset_pos_x += self.tile_size
                    if event.key == K_RIGHT and offset_pos_x >= -192:
                        offset_pos_x -= self.tile_size
                    
                    if event.key == K_ESCAPE:
                        loop = False
                    
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
                    
                    if ((X-self.character_pos_x/self.tile_size)**2 + (Y-self.character_pos_y/self.tile_size)**2)**(1/2) <= 5:
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
            return True
        else:
            self.character_pos_x = prev_pos_x
            self.character_pos_y = prev_pos_y
            return False
    
    def Load_map(self, M_Obj):
        """ """
        
        M_width = len(self.M_Obj) * self.tile_size
        M_height = len(self.M_Obj[0]) * self.tile_size

        M_surf = pygame.Surface((M_width, M_height))
        for x in range(len(M_Obj)):
            for y in range(len(M_Obj[x])):
                spaceRect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                baseTile = Map_to_Tile[M_Obj[x][y]]

                # Dibuja el la casilla con el bioma en la superficie
                M_surf.blit(baseTile, spaceRect)

        # Obtiene la posicion del personaje y lo dibuja
        spaceRect = pygame.Rect(self.character_pos_x * self.tile_size, self.character_pos_x * self.tile_size, self.tile_size, self.tile_size)
        baseCharacter = pygame.image.load("asets/characters/fundador_temp.png")
        M_surf.blit(baseCharacter, spaceRect)
        
        return M_surf
    
    def Read_Map (self, file):
        """ """
        assert os.path.exists(file), 'Cannot find the level file: %s' % (file)
        M_File = open(file, "r")
        content = M_File.readlines() + ["\r\n"]
        M_File.close()

        M_TextLines = []
        self.M_Obj = []

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
                    self.M_Obj.append([])

                # Invierte el mapa para que quede al derecho en la matriz
                for y in range (len(M_TextLines)):
                    for x in range (maxWidth):
                        self.M_Obj[x].append(M_TextLines[y][x])
        return self.M_Obj

    def menu_loop(self):
        self.world = Tablero(40, 23)
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
                    self.random_game_loop()
            
            # load button 
            self.screen.blit(self.menu_button_play, self.menubuttonplaycoll_2)
            if self.menubuttonplaycoll_2.collidepoint(self.mousepos) == True:
                self.screen.blit(self.menu_button_play_p,(self.menubuttonplaycoll_2))
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.M_Obj = self.Read_Map("maps/map1.txt")
                    self.load_game_loop(self.M_Obj)

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
    
    def load_game_loop(self, M_Obj):
        M_width = len(self.M_Obj) * self.tile_size
        M_height = len(self.M_Obj[0]) * self.tile_size
        mapNeedRedraw = True # verdadero para qe llame a drawMap()
        half_winWIdth = 640
        half_winHeight = 352
        c_Move= 0.5

        c_SetOffX = 0
        c_SetOffY = 0 

        # Crea el tablero en la clase board
        self.createBoard(self.M_Obj)

        posX, posY = self.setPositionRandom(len(self.M_Obj), len(self.M_Obj[0]), c_SetOffX, c_SetOffY)
        self.character_pos_x = 0 
        self.character_pos_y = 0

        # Establece el limite de hasta donde puede moverse la camara
        max_cam_move_X = abs(half_winWIdth - int(M_width/2))
        max_cam_move_Y = abs(half_winHeight - int(M_height/2))

        # Rastrea si las teclas para mover la camara estan presionadas 
        c_Up = False
        c_Down = False
        c_Left = False
        c_Right = False

        # Comienza el loop del juego hasta que el juegador cierre el juego
        while True: 
            mov_pos_y = 0
            mov_pos_x = 0
            

            # Registra y obtiene todos los eventos que realizo el usuario como un click o apretar una tecla
            for event in pygame.event.get():
                if event.type == QUIT:
                    # El usuario presiono la "X" para cerrar la aplicacion
                    self.terminate()

                # Maneja las teclas que fueron presionadas
                if event.type == KEYDOWN:

                    # camera
                    if event.key == K_LEFT:
                        c_Left = True
                    if event.key == K_RIGHT:
                        c_Right = True
                    if event.key == K_DOWN:
                        c_Down = True
                    if event.key == K_UP:
                        c_Up = True

                    #Character
                    if event.key == K_w:
                        mov_pos_y = -self.tile_size
                    if event.key == K_s:
                        mov_pos_y = self.tile_size
                    if event.key == K_a:
                        mov_pos_x = -self.tile_size
                    if event.key == K_d:
                        mov_pos_x = self.tile_size
                
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        c_Left = False
                    if event.key == K_RIGHT:
                        c_Right = False
                    if event.key == K_UP:
                        c_Up = False
                    if event.key == K_DOWN:
                        c_Down = False

            # Si mapNeedRedraw entonces se recarga el mapa
            if mapNeedRedraw:
                M_surf = self.Load_map(self.M_Obj)
                mapNeedRedraw = False
            
            # Cambia la variable del movimiento de la camara si el usuario presiono la tecla y no supera el limite
            if c_Up and c_SetOffY < max_cam_move_Y:
                c_SetOffY += c_Move
            if c_Down and c_SetOffY > -max_cam_move_Y:
                c_SetOffY -= c_Move
            if c_Left and c_SetOffX < max_cam_move_X:
                c_SetOffX += c_Move
            if c_Right and c_SetOffX > -max_cam_move_X:
                c_SetOffX -= c_Move

            # Ajusta el centro del mapa segun que tanto lo movio el usuario del centro
            mapRect = M_surf.get_rect()
            mapRect.center = (half_winWIdth + c_SetOffX, half_winHeight + c_SetOffY)

            self.screen.fill((0,0,0))

            # Dibuja el mapa en la pantalla del display
            self.screen.blit(M_surf, mapRect)
            self.check_charac_pos(mov_pos_x, mov_pos_y, c_SetOffX, c_SetOffY)

            pygame.display.update()
            self.clock.tick()
        
    def setPositionRandom(width, height):
        # Selecciona de mandera aleatoria 2 posiciones para spawnear
        while True:
            positionX = random.randrange(0, width + 1)
            positionY = random.randrange(0, height + 1)
            if movementPosible(positionX, positionY) == True:
                break
        return positionX, positionY
    
    def createBoard(self, M_Obj):
        """Crea el tablero de la clase board y le asigna el bioma a cada celda"""
        global board
        board = Tablero(len(M_Obj), len(M_Obj[0]))
        for x in range(len(M_Obj)):
            for y in range(len(M_Obj[0])):
                board.addCellAndBiome(y, x, M_Obj[x][y])
    
    def setPositionRandom(self, width, height, c_SetOffX, c_SetOffY):
        # Selecciona de mandera aleatoria 2 posiciones para spawnear
        while True:
            positionX = random.randrange(0, width + 1)
            positionY = random.randrange(0, height + 1)
            if self.check_charac_pos(positionX, positionY, c_SetOffX, c_SetOffY) == True:
                break
        return positionX, positionY

    def terminate(self):
        """Finaliza el programa y cierra todo"""
        pygame.quit()
        sys.exit()

G = Graphic()
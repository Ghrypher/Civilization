from tablero import Tablero
from units import Unit
import random, sys, copy, os, pygame
from pygame.locals import *

pygame.init()

class Graphic:
    """ clase graphic encargada del apartado grafico """

    def __init__(self):
        """ constructor de la clase """
        self.world = None
        self.character_pos_x = 576  
        self.character_pos_y = 320
        self.tile_size = 32
        self.non_reachables =[]
        self.non_reachables_load= []
        self.mousepos = (0,0)
        self.M_Obj = None
        self.Unit = None
        self.screen = pygame.display.set_mode((1280,704))
        self.screen_width = 1280
        self.screen_height = 704
        self.width = 70
        self.height = 40
        self.max_cam_move_X = int
        self.max_cam_move_Y = int
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
        # save system
        self.tecx_to_map = {"B" : pygame.image.load("asets/floor/Barrier.png"),
                            "D" : pygame.image.load("asets/floor/Dirt.png"),
                            "W" :pygame.image.load("asets/floor/Water.png"),
                            "M" : pygame.image.load("asets/floor/Mountain.png"),
                            "R" : "Revealed",
                            "H" : "Hidden",
                            "0" : False,
                            "1" : True}
                    
        self.menu_loop()

    def Load_map(self, M_Obj):
        """ """
        
        M_width = len(self.M_Obj) * self.tile_size
        M_height = len(self.M_Obj[0]) * self.tile_size
        positionX, positionY = self.Unit.getPosition()
        M_surf = pygame.Surface((M_width, M_height))
        for x in range(len(M_Obj)):
            for y in range(len(M_Obj[x])):
                spaceRect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                baseTile = self.tecx_to_map[M_Obj[x][y]]

                # Dibuja el la casilla con el bioma en la superficie
                M_surf.blit(baseTile, spaceRect)

        spaceRect = pygame.Rect(positionX * self.tile_size, positionY * self.tile_size, self.tile_size, self.tile_size)
        M_surf.blit(self.character, spaceRect)        
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
        background = self.Load_background()
        while True:
            self.screen.blit(background, (0,0))

            '''Mouse'''
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

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

            # Play button 
            self.screen.blit(self.menu_button_play,self.menubuttonplaycoll)
            if self.menubuttonplaycoll.collidepoint(self.mousepos) == True:
                self.screen.blit(self.menu_button_play_p,(self.menubuttonplaycoll))
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.non_reachables =[]
                    self.world = Tablero(self.width, self.height)
                    self.world.random_world()
                    self.M_Obj = self.Read_Map("maps/random_world.txt")
                    self.game_loop(self.M_Obj)
            
            # load button 
            self.screen.blit(self.menu_button_play, self.menubuttonplaycoll_2)
            if self.menubuttonplaycoll_2.collidepoint(self.mousepos) == True:
                self.screen.blit(self.menu_button_play_p,(self.menubuttonplaycoll_2))
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.non_reachables =[]
                    self.M_Obj = self.Read_Map("maps/map1.txt")
                    self.game_loop(self.M_Obj)

            '''System'''
            self.screen.blit(self.screenlogo,self.screenlogocoll)
            self.screen.blit(self.mouse_img,self.mousepos)
            pygame.display.update()
            self.clock.tick(30)
        
    def Load_background(self):    
        M_width =40 * self.tile_size
        M_height = 23 * self.tile_size

        M_surf = pygame.Surface((M_width, M_height))
        for y in range(23):
            for x in range(40):
                spaceRect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                baseTile = pygame.image.load('asets/floor/' + str(self.world.get_tiles(y, x)) + '.png').convert()
                # Dibuja el la casilla con el bioma en la superficie
                M_surf.blit(baseTile, spaceRect)
        return M_surf
    
    def game_loop(self, M_Obj):
        M_width = len(self.M_Obj) * self.tile_size
        M_height = len(self.M_Obj[0]) * self.tile_size
        mapNeedRedraw = True # verdadero para qe llame a drawMap()
        half_winWIdth = self.screen_width/2
        half_winHeight = self.screen_height/2
        c_Move= 1.5

        # Crea el tablero en la clase board
        self.createBoard(self.M_Obj)

        self.Unit = Unit("Wk","a")
        posX, posY = self.setPositionRandom(len(self.M_Obj), len(self.M_Obj[0]))
        self.Unit.setPosition(posX, posY)

        c_SetOffX = 0
        c_SetOffY = 0 

        M_surf = self.Load_map(self.M_Obj)
        mapRect = M_surf.get_rect()
        mapRect.center = (half_winWIdth + c_SetOffX, half_winHeight + c_SetOffY)
        self.character_pos_x, self.character_pos_y = mapRect.center 

        # Establece el limite de hasta donde puede moverse la camara
        self.max_cam_move_X = abs(half_winWIdth - int(M_width/2))
        self.max_cam_move_Y = abs(half_winHeight - int(M_height/2))

        # Rastrea si las teclas para mover la camara estan presionadas 
        c_Up = False
        c_Down = False
        c_Left = False
        c_Right = False

        # Comienza el loop del juego hasta que el juegador cierre el juego
        loop = True
        while loop: 
            '''Mouse'''
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

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
                        posX, posY = self.Unit.getPosition()
                        if self.movementPosible(posX, posY - 1):
                            self.Unit.setPosition(posX, posY - 1)
                            mapNeedRedraw = True
                    elif event.key == K_s:
                        posX, posY = self.Unit.getPosition()
                        if self.movementPosible(posX, posY + 1):
                            self.Unit.setPosition(posX, posY + 1)
                            mapNeedRedraw = True
                    if event.key == K_a:
                        posX, posY = self.Unit.getPosition()
                        if self.movementPosible(posX - 1, posY):
                            self.Unit.setPosition(posX - 1, posY)
                            mapNeedRedraw = True
                    elif event.key == K_d:
                        posX, posY = self.Unit.getPosition()
                        if self.movementPosible(posX + 1, posY):
                            self.Unit.setPosition(posX + 1, posY)
                            mapNeedRedraw = True
                    
                    if event.key == K_ESCAPE:
                        loop = False
                
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
            if c_Up and c_SetOffY < self.max_cam_move_Y:
                c_SetOffY += c_Move
            if c_Down and c_SetOffY > -self.max_cam_move_Y:
                c_SetOffY -= c_Move
            if c_Left and c_SetOffX < self.max_cam_move_X:
                c_SetOffX += c_Move
            if c_Right and c_SetOffX > -self.max_cam_move_X:
                c_SetOffX -= c_Move

            # Ajusta el centro del mapa segun que tanto lo movio el usuario del centro
            mapRect = M_surf.get_rect()
            mapRect.center = (half_winWIdth + c_SetOffX, half_winHeight + c_SetOffY)
            self.screen.fill((0,0,0))

            # Dibuja el mapa en la pantalla del display
            self.screen.blit(M_surf, mapRect)
            
            self.screen.blit(self.mouse_img,self.mousepos)
            pygame.display.update()
            self.clock.tick()
        self.menu_loop()
    
    def createBoard(self, M_Obj):
        """Crea el tablero de la clase board y le asigna el bioma a cada celda"""

        self.world = Tablero(len(M_Obj), len(M_Obj[0]))
        self.world.assignSize(len(self.M_Obj))
        for x in range(len(M_Obj)):
            for y in range(len(M_Obj[0])):
                self.world.addCellAndBiome(x, y, self.M_Obj[x][y])

    def setPositionRandom(self, width, height):
        # Selecciona de mandera aleatoria 2 posiciones para spawnear
        while True:
            positionX = random.randrange(0, width + 1)
            positionY = random.randrange(0, height + 1)
            if self.movementPosible(positionX, positionY) == True:
                break
        return positionX, positionY
    
    def movementPosible(self, posX, posY):
        """Obtiene el bioma de la celda y si es posible caminar sobre el devuelve True de lo contrario devuelve False"""
        if posX >= 0 and posY >= 0:
            try:
                coord = str(posX)+ " " + str(posY)
                biome = self.world.get_biome(posX, posY)
                if biome == "D" :
                    return True
                else:
                    return False
            except:
                return False
        else:
            return False

    def terminate(self):
        """Finaliza el programa y cierra todo"""
        pygame.quit()
        sys.exit()


G = Graphic()
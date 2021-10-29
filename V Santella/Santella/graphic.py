from tablero import Tablero
from units import Unit
import random, sys, pygame, math
from pygame.locals import *

pygame.init()

class Graphic:
    """ clase graphic encargada del apartado grafico """

    def __init__(self):
        """ constructor de la clase """
        self.world = None
        self.carachter_index = 0
        self.tile_size = 32
        self.non_reachables =[]
        self.non_reachables_load= []
        self.mousepos = (0,0)
        self.map = None
        self.units = 5
        
        self.screen = pygame.display.set_mode((1280,704))
        self.screen_width = 1280
        self.screen_height = 704
        self.width = 70
        self.height = 40
        self.max_cam_move_X = int
        self.max_cam_move_Y = int
        self.clock = pygame.time.Clock()
        self.mouse_img = pygame.image.load('asets/menus/Mouse.png')
        self.character = pygame.image.load('asets/characters/Red_Founder.png')
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
        self.text_to_map = {"B" : pygame.image.load("asets/floor/Barrier.png"),
                            "D" : pygame.image.load("asets/floor/Dirt.png"),
                            "F" : pygame.image.load("asets/floor/Forest.png"),
                            "W" :pygame.image.load("asets/floor/Water.png"),
                            "M" : pygame.image.load("asets/floor/Mountain.png"),
                            "I" : pygame.image.load("asets/floor/Iron_Mountain.png"),
                            "G" : pygame.image.load("asets/floor/Gold_Mountain.png"),
                            "R" : "Revealed",
                            "H" : "Hidden",
                            "0" : False,
                            "1" : True}
        
                    
        self.menu_loop()

    def Load_map(self):
        """ """
        
        M_width = len(self.map) * self.tile_size
        M_height = len(self.map[0]) * self.tile_size
        M_surf = pygame.Surface((M_width, M_height))
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                spaceRect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                baseTile = self.text_to_map[self.map[x][y]]

                 # Dibuja el la casilla con el bioma en la superficie
                M_surf.blit(baseTile, spaceRect)
        for x in range(self.units):
            positionX, positionY = self.world.Unit[x].getPosition()
            spaceRect = pygame.Rect(positionX * self.tile_size, positionY * self.tile_size, self.tile_size, self.tile_size)
            M_surf.blit(self.character, spaceRect)        
        return M_surf

    def menu_loop(self):
        self.world = Tablero(40, 23)
        self.world.random_world()
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
                    self.map = self.world.Read_Map("maps/random_world.txt")
                    self.game_loop()
            
            # load button 
            self.screen.blit(self.menu_button_play, self.menubuttonplaycoll_2)
            if self.menubuttonplaycoll_2.collidepoint(self.mousepos) == True:
                self.screen.blit(self.menu_button_play_p,(self.menubuttonplaycoll_2))
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.non_reachables =[]
                    self.map = self.world.Read_Map("maps/map1.txt")
                    self.game_loop()

            '''System'''
            self.screen.blit(self.screenlogo,self.screenlogocoll)
            self.screen.blit(self.mouse_img,self.mousepos)
            pygame.display.update()
            self.clock.tick(30)
        
    def Load_background(self):    
        self.world = Tablero(40, 23)
        self.world.random_world()
        map = self.world.Read_Map("maps/random_world.txt")
        M_width = 40 * self.tile_size
        M_height = 23 * self.tile_size
        M_surf = pygame.Surface((M_width, M_height))
        for x in range(40):
            for y in range(23):
                spaceRect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                baseTile = self.text_to_map[map[x][y]]
                M_surf.blit(baseTile, spaceRect)       
        return M_surf
    
    def game_loop(self):
        M_width = len(self.map) * self.tile_size
        M_height = len(self.map[0]) * self.tile_size
        mapNeedRedraw = True # verdadero para qe llame a drawMap()
        save_game = False
        half_winWIdth = self.screen_width/2
        half_winHeight = self.screen_height/2
        c_Move= 18.5
        self.world.erase_Units()

        # Crea el tablero en la clase board
        self.createBoard(self.map)
        for x in range (self.units):
            posX, posY = self.setPositionRandom(len(self.map), len(self.map[0]))
            self.world.addUnit(posX, posY, x, "Wk","Red")
            self.world.Unit[x].setIndex(x)
        
        c_SetOffX = 0
        c_SetOffY = 0 

        mousePressed = False

        M_surf = self.Load_map()
        mapRect = M_surf.get_rect()
        mapRect.center = (half_winWIdth + c_SetOffX, half_winHeight + c_SetOffY)

        # Establece el limite de hasta donde puede moverse la camara
        self.max_cam_move_X = abs(half_winWIdth - int(M_width/2))
        self.max_cam_move_Y = abs(half_winHeight - int(M_height/2))

        # Rastrea si las teclas para mover la camara estan presionadas 
        c_Up = False
        c_Down = False
        c_Left = False
        c_Right = False

        s_index = 0
        
        # Comienza el loop del juego hasta que el juegador cierre el juego
        loop = True
        while loop: 
            '''Mouse'''
            self.mousepos = pygame.mouse.get_pos()
            mousePos =  pygame.mouse.get_pos()
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
                        posX, posY = self.world.Unit[s_index].getPosition()
                        if self.movementPosible(posX, posY - 1):
                            self.world.Unit[s_index].setPosition(posX, posY - 1)
                            mapNeedRedraw = True
                    elif event.key == K_s:
                        posX, posY = self.world.Unit[s_index].getPosition()
                        if self.movementPosible(posX, posY + 1):
                            self.world.Unit[s_index].setPosition(posX, posY + 1)
                            mapNeedRedraw = True
                    if event.key == K_a:
                        posX, posY = self.world.Unit[s_index].getPosition()
                        if self.movementPosible(posX - 1, posY):
                            self.world.Unit[s_index].setPosition(posX - 1, posY)
                            mapNeedRedraw = True
                    elif event.key == K_d:
                        posX, posY = self.world.Unit[s_index].getPosition()
                        if self.movementPosible(posX + 1, posY):
                            self.world.Unit[s_index].setPosition(posX + 1, posY)
                            mapNeedRedraw = True

                    if event.key == K_g:
                        mapNeedRedraw = True
                        save_game = True
                    
                    if event.key == K_ESCAPE:
                        loop = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePressed = True
                
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        c_Left = False
                    if event.key == K_RIGHT:
                        c_Right = False
                    if event.key == K_UP:
                        c_Up = False
                    if event.key == K_DOWN:
                        c_Down = False
            
            mapRectX, mapRectY = mapRect.topleft
            topLeftPos = abs(mapRectX), abs(mapRectY)
            mousePos = tuple(sum(x) for x in zip(mousePos, topLeftPos))

            if mousePressed:
                posX, posY = mousePos
                unit = self.world.checkUnit(math.floor(posX/32), math.floor(posY/32))
                if unit != None:
                    s_index = unit
                mousePressed = False

            # Si mapNeedRedraw entonces se recarga el mapa
            if mapNeedRedraw:
                M_surf = self.Load_map()
                mapNeedRedraw = False
                if save_game:
                    self.world.save_game(self.map)
                    save_game = False
            
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
            self.clock.tick(30)
        self.menu_loop()
    
    def createBoard(self, M_Obj):
        """Crea el tablero de la clase board y le asigna el bioma a cada celda"""

        self.world.assignSize(len(M_Obj))
        for x in range(len(M_Obj)):
            for y in range(len(M_Obj[0])):
                self.world.addCellAndBiome(x, y, M_Obj[x][y])

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
try:
    import pygame
except ImportError:
    print("PyGame library is not installed. Please install it. CMD: pip install pygame")

import random, os, math
from character import Character
from gameboard import GameBoard
from gameview import GameView

pygame.init()

class SystemController():
    def __init__(self):
        """Function __init__"""
        self.gameview = GameView()
        self.screen_width = 1280
        self.screen_height = 656
        self.world = None
        self.units = 5
        self.character_pos_x = 576  
        self.character_pos_y = 320
        self.tile_size = 32
        self.mousepos = (0,0)
        self.map = None
        self.Unit = None
        self.width = 70
        self.height = 40
        self.max_cam_move_X = int
        self.max_cam_move_Y = int
        self.event = None
        self.menufont = None
        self.menufontlittle = None
        self.menufontlittle2 = None
        self.buttexture = None

    def controlInputsEvents(self,mode):
        """Function controlInputsEvents, controls the keyboard or mouse inputs"""
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                return 'exit'
            """For All Except Credits, Instructions"""
            if mode != 'credits' or mode != 'insts':
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    return 'mouseon'
            """Only for WorkInProgress, Credits, Instructions, MapSelector"""
            if mode == 'work' or mode == 'credits' or mode == 'insts' or mode == 'map' or mode == 'game':
                if self.event.type == pygame.KEYDOWN:
                    """Escape"""
                    if self.event.key == pygame.K_ESCAPE:
                        return 'nonexit'
                    if mode == 'game':
                        if self.event.key == pygame.K_LEFT:
                            return 'K_LEFTT'
                        if self.event.key == pygame.K_RIGHT:
                            return 'K_RIGHTT'
                        if self.event.key == pygame.K_DOWN:
                            return 'K_DOWNT'
                        if self.event.key == pygame.K_UP:
                            return 'K_UPT'
                        if self.event.key == pygame.K_RETURN:
                            return 'K_RETURN'
                        

                        if self.event.key == pygame.K_w:
                            return 'K_W'
                        elif self.event.key == pygame.K_s:
                            return 'K_S'
                        if self.event.key == pygame.K_a:
                            return 'K_A'
                        elif self.event.key == pygame.K_d:
                            return 'K_D'
                        
                        if self.event.key == pygame.K_g:
                            return 'K_G'

                if self.event.type == pygame.KEYUP and mode == 'game':
                    if self.event.key == pygame.K_LEFT:
                        return 'K_LEFTF'
                    if self.event.key == pygame.K_RIGHT:
                        return 'K_RIGHTF'
                    if self.event.key == pygame.K_UP:
                        return 'K_UPF'
                    if self.event.key == pygame.K_DOWN:
                        return 'K_DOWNF'                    

    def controlMouseMovement(self):
        """Function controlMouseMovement, gets the mouse position and sets the cursor on non visible"""
        mousepos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        return mousepos

    def progressBar(self,mode):
        """Function loadingBarProgress, establishes the progress from the loading bar"""
        self.defaultbackground,self.menumusic,self.defaultcursor,self.handcursor,self.workinprogressmessage,self.underconstruction,self.exitbackground,self.exitbackgroundpos,self.exittext,self.exittextpos,self.exitbuttonyes,self.exitbuttonyescoll,self.exitbuttonyestext,self.exitbuttonyestextcoll,self.exitbuttonno,self.exitbuttonnocoll,self.exitbuttonnotext,self.exitbuttonnotextcoll,self.mapselectorbutton,self.mapselectorbuttoncoll,self.mapselectorbuttontext,self.mapselectorbuttontextcoll,self.menubuttoncredits,self.menubuttoncreditstext,self.menubuttoncreditscoll,self.menubuttoncreditstextcoll,self.menubuttoninstructions,self.menubuttoninstructionstext,self.menubuttoninstructionscoll,self.menubuttoninstructionstextcoll,self.randomplaybutton,self.randomplaybuttoncoll,self.randomplaybuttontext,self.randomplaybuttontextcoll,self.createdplaybutton,self.createdplaybuttoncoll,self.createdplaybuttontext,self.createdplaybuttontextcoll,self.swordcursor,self.foundersprite,self.founderspriteposx,self.founderspriteposy,self.founderspritecoll,self.biometiles,self.hidden,self.gamemusic1,self.gamemusic2 = self.gameview.loadBarView(mode)

    def menuLoop(self):
        """Function menuLoop, is the menu loop"""
        """First Draw Call"""
        self.gameview.menuFirstDraw()

        playing = True

        """Menu View Loop"""
        while playing == True:
            try:
                mousepos = self.controlMouseMovement()
                keyreturned = self.controlInputsEvents('menu')
            except:
                pass
            sysconreturned = self.gameview.menuView(mousepos,keyreturned)
            if sysconreturned != ' ':
                playing = False

        return sysconreturned

    def workInProgress(self):
        """Function workInProgress, is a temporaly function which says that this part of the code is not finished yet"""
        self.gameview.workInProgressFirstDraw()
        
        playing = True

        """Menu View Loop"""
        while playing == True:
            try:
                mousepos = self.controlMouseMovement()
                keyreturned = self.controlInputsEvents('work')
            except:
                pass
            sysconreturned = self.gameview.workInProgressView(mousepos,keyreturned)
            if sysconreturned != ' ':
                playing = False

        return sysconreturned

    def exitUI(self,gamemode):
        """Function exitUI, ask if you want to exit"""
        self.gameview.exitUIFirstDraw()

        playing = True

        """Menu View Loop"""
        while playing == True:
            try:
                mousepos = self.controlMouseMovement()
                keyreturned = self.controlInputsEvents('exit')
            except:
                pass
            sysconreturned = self.gameview.exitUIView(mousepos,keyreturned)
            if sysconreturned == 'nonexit':
                playing = False
        
        if gamemode == 'random':
            sysconreturned = 'random'
        elif gamemode == 'created':
            sysconreturned = 'created'
        elif gamemode == 'menu':
            sysconreturned = 'menu'
        elif gamemode == 'credits':
            sysconreturned = 'credits'
        elif gamemode == 'instructions':
            sysconreturned = 'instructions'
        elif gamemode == 'mode':
            sysconreturned = 'mode'

        return sysconreturned

    def credits(self):
        """Function creditsOpen, put the credits on screen"""
        self.gameview.creditsFirstDraw()

        playing = True

        """Menu View Loop"""
        while playing == True:
            try:
                mousepos = self.controlMouseMovement()
                keyreturned = self.controlInputsEvents('credits')
            except:
                pass
            sysconreturned = self.gameview.creditsView(mousepos,keyreturned)
            if sysconreturned != ' ':
                playing = False

        return sysconreturned

    def instructions(self):
        """Function instructionsOpen, put the instructions on screen"""
        self.gameview.instructionsFirstDraw()

        playing = True

        """Menu View Loop"""
        while playing == True:
            try:
                mousepos = self.controlMouseMovement()
                keyreturned = self.controlInputsEvents('insts')
            except:
                pass
            sysconreturned = self.gameview.instructionsView(mousepos,keyreturned)
            if sysconreturned != ' ':
                playing = False

        return sysconreturned

    def gameMapSelector(self):
        """Function gameMapSelector, is the game map selector"""
        self.gameview.mapSelectorFirstDraw()
        
        playing = True

        """Menu View Loop"""
        while playing == True:
            try:
                mousepos = self.controlMouseMovement()
                keyreturned = self.controlInputsEvents('map')
            except:
                pass
            sysconreturned = self.gameview.mapSeclectorView(mousepos,keyreturned)
            if sysconreturned != ' ':
                playing = False

        if sysconreturned == 'random':
            self.world = GameBoard(100,80)
            self.world.randomWorld()
            self.map = self.read_Map("resources/maps/randomWorld.txt.txt")
        if sysconreturned == 'pre':
            self.map = self.read_Map("resources/maps/map1.txt")
            self.world = GameBoard(len(self.map), len(self.map[0]))

        return sysconreturned

    def movementPosible(self, posX, posY):
        """Obtiene el bioma de la celda y si es posible caminar sobre el devuelve True de lo contrario devuelve False"""
        if posX >= 0 and posY >= 0:
            try:
                biome = self.world.getBiome(posX, posY)
                ocupied = self.world.checkCell(posX, posY)
                if biome == "D" and ocupied == False:
                    return True
                else:
                    return False
            except:
                return False
        else:
            return False

    def setPositionRandom(self, width, height):
        # Selecciona de mandera aleatoria 2 posiciones para spawnear
        while True:
            positionX = random.randrange(0, width + 1)
            positionY = random.randrange(0, height + 1)
            if self.movementPosible(positionX, positionY) == True:
                break
        return positionX, positionY

    def createBoard(self, mapObj):
        """Crea el tablero de la clase board y le asigna el bioma a cada celda"""
        self.world.assignSize(len(mapObj))
        for x in range(len(mapObj)):
            for y in range(len(mapObj[0])):
                self.world.addCellAndBiome(x, y, mapObj[x][y])

    def loadMap(self):
        """ """
        M_width = len(self.map) * self.tile_size
        M_height = len(self.map[0]) * self.tile_size
        M_surf = pygame.Surface((M_width, M_height))

        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                self.world.cellOff(x, y)
        
        for unit in range(len(self.world.Unit)):            
            positionX, positionY = self.world.Unit[unit].getPosition() # Obtiene la posicion del personaje
            for x in range(len(self.map)):
                for y in range(len(self.map[x])):

                    if ((x - positionX)**2 + (y - positionY)**2)**(1/2) <= 5:
                        self.world.revealCell(x, y) 

        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                                
                if self.world.getVisibility(x, y) == (True, True):                
                    spaceRect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                    baseTile = self.biometiles[self.map[x][y]]

                 # Dibuja el la casilla con el bioma en la superficie
                    M_surf.blit(baseTile, spaceRect)
                else:
                    if self.world.getVisibility(x, y) == (False, True):
                        spaceRect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                        baseTile = self.biometiles[" " + self.map[x][y]]

                        # Dibuja el la casilla con el bioma en la superficie
                        M_surf.blit(baseTile, spaceRect)
                    else:
                        spaceRect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                        baseTile = self.biometiles[" "]

                        # Dibuja el la casilla con el bioma en la superficie
                        M_surf.blit(baseTile, spaceRect) 

        for x in range(self.units):
            positionX, positionY = self.world.Unit[x].getPosition()
            self.foundersprite = self.gameview.updateSprite((str(self.world.Unit[x].getSprite())))
            spaceRect = pygame.Rect(positionX * self.tile_size, positionY * self.tile_size, self.tile_size, self.tile_size)
            M_surf.blit(self.foundersprite, spaceRect)        
        return M_surf

    def gameLoop(self):
        M_width = len(self.map) * self.tile_size
        M_height = len(self.map[0]) * self.tile_size
        mapNeedRedraw = True # verdadero para qe llame a drawMap()
        saveGame = False
        half_winWIdth = self.screen_width/2
        half_winHeight = self.screen_height/2
        c_Move = 10
        self.world.eraseUnits()

        # Crea el tablero en la clase board
        self.createBoard(self.map)
        for x in range (self.units):
            posX, posY = self.setPositionRandom(len(self.map), len(self.map[0]))
            self.world.addUnit(posX, posY, x, "FD","Red")
            self.world.occupiedCell(posX, posY)
            self.world.Unit[x].setIndex(x)

        c_SetOffX = 0
        c_SetOffY = 0

        mousePressed = False

        self.passTurn()
        
        M_surf = self.loadMap()
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

        s_index = 0

        # Comienza el loop del juego hasta que el juegador cierre el juego
        loop = True
        while loop: 
            '''Mouse'''
            try:
                self.mousepos = self.controlMouseMovement()
                mousePos = self.mousepos
            except:
                pass

            # Registra y obtiene todos los eventos que realizo el usuario como un click o apretar una tecla
            self.event = self.controlInputsEvents('game')
            if self.event == 'exit':
                loop = False
            if self.event == 'nonexit':
                loop = False
            #arrows camera
            if self.event == 'K_LEFTT':
                c_Left = True
            if self.event == 'K_RIGHTT':
                c_Right = True
            if self.event == 'K_DOWNT':
                c_Down = True
            if self.event == 'K_UPT':
                c_Up = True
            if self.event == 'K_RETURN':
                self.passTurn()
            if self.event == 'K_LEFTF':
                c_Left = False
            if self.event == 'K_RIGHTF':
                c_Right = False
            if self.event == 'K_DOWNF':
                c_Down = False
            if self.event == 'K_UPF':
                c_Up = False
            if self.event == 'mouseon':
                mousePressed = True
            if self.event == 'K_G':
                mapNeedRedraw = True
                saveGame = True
            
            #WASD movement
            if self.event == 'K_W':
                posX, posY = self.world.Unit[s_index].getPosition()
                if self.world.Unit[s_index].movement > 0:
                    if self.movementPosible(posX, (posY - 1)):
                        self.world.unoccupiedCell(posX, posY)
                        self.world.occupiedCell(posX, posY - 1)
                        self.world.Unit[s_index].setPosition(posX, posY - 1)
                        posY -= 1
                        mapNeedRedraw = True
                        self.world.Unit[s_index].movement -= 1
            if self.event == 'K_S':
                posX, posY = self.world.Unit[s_index].getPosition()
                if self.world.Unit[s_index].movement > 0:
                    if self.movementPosible(posX, (posY + 1)):
                        self.world.unoccupiedCell(posX, posY)
                        self.world.occupiedCell(posX, posY + 1)
                        self.world.Unit[s_index].setPosition(posX, posY + 1)
                        posY += 1
                        mapNeedRedraw = True
                        self.world.Unit[s_index].movement -= 1
            if self.event == 'K_A':
                posX, posY = self.world.Unit[s_index].getPosition()
                if self.world.Unit[s_index].movement > 0:
                    if self.movementPosible((posX - 1), posY):
                        self.world.unoccupiedCell(posX, posY)
                        self.world.occupiedCell(posX - 1, posY)
                        self.world.Unit[s_index].setPosition(posX - 1, posY)
                        posX -= 1
                        mapNeedRedraw = True
                        self.world.Unit[s_index].movement -= 1
            if self.event == 'K_D':
                posX, posY = self.world.Unit[s_index].getPosition()
                if self.world.Unit[s_index].movement > 0:
                    if self.movementPosible((posX + 1), posY):
                        self.world.unoccupiedCell(posX, posY)
                        self.world.occupiedCell(posX + 1, posY)
                        self.world.Unit[s_index].setPosition(posX + 1, posY)
                        posX += 1
                        mapNeedRedraw = True
                        self.world.Unit[s_index].movement -= 1

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
                M_surf = self.loadMap()
                mapNeedRedraw = False
                if saveGame:
                    self.world.saveGame(self.map)
                    saveGame = False
            
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

            self.gameview.gameLoopView(M_surf,mapRect,self.mousepos,self.defaultcursor)

        return 'exit'

    def read_Map (self, file):
        """ """
        assert os.path.exists(file), 'Cannot find the level file: %s' % (file)
        M_File = open(file, "r")
        content = M_File.readlines() + ["\r\n"]
        M_File.close()

        M_TextLines = []
        mapObj = []

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
                    mapObj.append([])

                # Invierte el mapa para que quede al derecho en la matriz
                for y in range (len(M_TextLines)):
                    for x in range (maxWidth):
                        mapObj[x].append(M_TextLines[y][x])
        return mapObj   

    def passTurn (self):
        for x in range(self.units):
            self.world.Unit[x].movement = 4

"""Libraries"""
import random, sys, copy, os, pygame, time
from pygame.constants import QUIT
from pygame.locals import *
import gameresources as gameres
from gameboard import GameBoard
from character import Character

"""Pygame Init"""
pygame.init()

class GameMain():

    """Function __init__"""
    def __init__(self):
        self.screensx = 1280 #Is the width from the window
        self.screensy = 704 #Is the height from the window
        self.half_winWIdth = int(self.screensx / 2)
        self.half_winHeight = int(self.screensy / 2)
        self.screensize = (self.screensx,self.screensy) #Is the size from the window
        self.screen = pygame.display.set_mode(self.screensize, pygame.RESIZABLE) #Create the window
        self.windowicon,self.windowname,self.menufont,self.menufontlittle,self.menufontlittle2,self.buttonwoodtexture = gameres.systemLoads() #Uses the systemLoads function from gameresources
        self.clock = pygame.time.Clock() #Creates the clock function from the game
        self.mousepos = (0,0) #Records the position from the mouse
        self.playing = True #Establishes if a function is running or not
        self.keyup = False #Establishes if the up arrow is pressed or not
        self.keydown = False #Establishes if the down arrow is pressed or not
        self.keyleft = False #Establishes if the left arrow is pressed or not
        self.keyright = False #Establishes if the right arrow is pressed or not
        self.cameraup = False #Establishes if the camera is going up or not
        self.cameradown = False #Establishes if the camera is going down or not
        self.cameraleft = False #Establishes if the camera is going to the left or not
        self.cameraright = False #Establishes if the camera is going to the right or not
        self.cameraspeed = 5 #Establishes the speed from the camera
        self.mouseclicked = False #Establishes if the mouse is pressed or not
        self.tileWidth = 32 #Establishes the width from the tiles
        self.tileHeight = 32 #Establishes the height from the tiles
        self.width = 40
        self.height = 33
        self.screenlogo,self.screenlogocoll = gameres.screenLogo() #Uses the screenLogo function from gameresources
        self.nonreachables =[]
        self.M_Obj = None
        """Loads"""
        self.loadingtext,self.loadingtextcoll,self.loadingbar,self.loadingbarcoll = gameres.menuesLoads(9)
        self.loadingBarProgress(1)
        self.menumusic.play(loops = -1)
        self.mapObj = self.readMap("resources/maps/map1.txt")
        self.createBoard()
        self.character = None
        self.menuLoop() #Starts the program from the menuLoop function

    """Function loadingBarProgress, establishes the progress from the loading bar"""
    def loadingBarProgress(self,mode):
        loading = True
        loadingstep = 0
        loadingprogressvalue = 0
        while loading:
            loadingstep += 1

            """Background"""
            self.screen.fill([0,0,0])
            """Text"""
            self.screen.blit(self.loadingtext,self.loadingtextcoll)
            """Loading Bar"""
            self.screen.blit(self.loadingbar,self.loadingbarcoll)
            """Loading Bar Content Complete"""
            pygame.draw.rect(self.screen,[116,125,131],(250,542,loadingprogressvalue,20)) #97 == 8% progress

            """Loads"""
            """Menues Loads"""
            if mode == 1:
                if loadingstep == 1:
                    loadingprogressvalue += 130
                if loadingstep == 10:
                    """Menues All"""
                    self.defaultbackground,self.menumusic,self.defaultcursor,self.handcursor = gameres.menuesLoads(1) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 130
                elif loadingstep == 15:
                    """Work In Progress"""
                    self.workinprogressmessage,self.underconstruction = gameres.menuesLoads(2) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 130
                elif loadingstep == 20:
                    """Exit"""
                    self.exitbackground,self.exitbackgroundpos,self.exittext,self.exittextpos,self.exitbuttonyes,self.exitbuttonyescoll,self.exitbuttonyestext,self.exitbuttonyestextcoll,self.exitbuttonno,self.exitbuttonnocoll,self.exitbuttonnotext,self.exitbuttonnotextcoll = gameres.menuesLoads(3) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 130
                elif loadingstep == 25:
                    """Map Selector"""
                    self.mapselectorbutton,self.mapselectorbuttoncoll,self.mapselectorbuttontext,self.mapselectorbuttontextcoll= gameres.menuesLoads(4) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 130
                elif loadingstep == 30:
                    """Credits"""
                    self.menubuttoncredits,self.menubuttoncreditstext,self.menubuttoncreditscoll,self.menubuttoncreditstextcoll = gameres.menuesLoads(5) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 130
                elif loadingstep == 35:
                    """Instructions"""
                    self.menubuttoninstructions,self.menubuttoninstructionstext,self.menubuttoninstructionscoll,self.menubuttoninstructionstextcoll = gameres.menuesLoads(6) #Uses the menuLoads function from gameresources
                    loading = False
            """Game Loads"""
            if mode == 2:
                if loadingstep == 1:
                    loadingprogressvalue += 195
                if loadingstep == 10:
                    """Play Random"""
                    self.randomplaybutton,self.randomplaybuttoncoll,self.randomplaybuttontext,self.randomplaybuttontextcoll = gameres.menuesLoads(7) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 195
                elif loadingstep == 15:
                    """Play Pre-Created"""
                    self.createdplaybutton,self.createdplaybuttoncoll,self.createdplaybuttontext,self.createdplaybuttontextcoll = gameres.menuesLoads(8) #Uses the menuLoads function from gameresources
                    loadingprogressvalue += 195
                elif loadingstep == 30:
                    """Game"""
                    self.swordcursor,self.foundersprite,self.founderspriteposx,self.founderspriteposy,self.founderspritecoll,self.biometiles,self.hidden = gameres.gameLoads(1) #Uses the gameLoads function from gameresources
                    loadingprogressvalue += 195
                elif loadingstep == 35:
                    self.gamemusic1,self.gamemusic2 = gameres.gameLoads(2) #Uses the gameLoads function from gameresources
                    loading = False

            self.clock.tick(30)
            pygame.display.update()

    """Function menuLoop, is the menu loop"""
    def menuLoop(self):
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Game Logo"""
        self.screen.blit(self.screenlogo,self.screenlogocoll)
        """Buttons"""
        """Play"""
        self.screen.blit(self.mapselectorbutton,self.mapselectorbuttoncoll)
        self.screen.blit(self.mapselectorbuttontext,self.mapselectorbuttontextcoll)
        """Credits"""
        self.screen.blit(self.menubuttoncredits,self.menubuttoncreditscoll)
        self.screen.blit(self.menubuttoncreditstext,self.menubuttoncreditstextcoll)
        """Instructions"""
        self.screen.blit(self.menubuttoninstructions,self.menubuttoninstructionscoll)
        self.screen.blit(self.menubuttoninstructionstext,self.menubuttoninstructionstextcoll)
        
        while True:

            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            """Events Manager"""
            for event in pygame.event.get():
                """Exit Event"""
                if event.type == pygame.QUIT:
                    self.exitUI('menu')
                """Screen Resize"""
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)
                """Mouse Events"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseclicked = True
                else:
                    self.mouseclicked = False

            """Draw Calls"""
            try:
                if mouseoldpos != self.mousepos:
                    """Background"""
                    self.screen.blit(self.defaultbackground,(0,0))
                    """Game Logo"""
                    self.screen.blit(self.screenlogo,self.screenlogocoll)
                    """Buttons"""
                    """Play"""
                    self.screen.blit(self.mapselectorbutton,self.mapselectorbuttoncoll)
                    self.screen.blit(self.mapselectorbuttontext,self.mapselectorbuttontextcoll)
                    """Credits"""
                    self.screen.blit(self.menubuttoncredits,self.menubuttoncreditscoll)
                    self.screen.blit(self.menubuttoncreditstext,self.menubuttoncreditstextcoll)
                    """Instructions"""
                    self.screen.blit(self.menubuttoninstructions,self.menubuttoninstructionscoll)
                    self.screen.blit(self.menubuttoninstructionstext,self.menubuttoninstructionstextcoll)
            except:
                pass
            """Mouses"""
            if self.mapselectorbuttoncoll.collidepoint(self.mousepos) == True or self.menubuttoncreditscoll.collidepoint(self.mousepos) == True or self.menubuttoninstructionscoll.collidepoint(self.mousepos) == True:
                self.screen.blit(self.handcursor,self.mousepos)
            else:
                self.screen.blit(self.defaultcursor,self.mousepos)

            """Control"""
            """Mouse Passes Over the Buttons"""
            """Map Select"""
            if self.mapselectorbuttoncoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.mapselectorbuttoncoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.gameMapSelector(True)
            """Credits"""
            if self.menubuttoncreditscoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttoncreditscoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.workInProgress(True,None) #creditsOpen(True)
            """Instructions"""
            if self.menubuttoninstructionscoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.menubuttoninstructionscoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.workInProgress(True,None) #instructionsOpen(True)

            """System"""
            pygame.display.update()
            mouseoldpos = self.mousepos
            self.clock.tick(30)

    """Function workInProgress, is a temporaly function which says that this part of the code is not finished yet"""
    def workInProgress(self,playing,mode):        
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.defaultbackground,(0,0))
        """Under Construction"""
        self.screen.blit(self.workinprogressmessage,(275,300))
        self.screen.blit(self.underconstruction,(425,75))

        self.playing = playing
        if mode == 'map':
            self.gamemusic1.play(loops = -1)
            self.gamemusic1.set_volume(0.25)
        while self.playing == True:
            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            """Events Manager"""
            for event in pygame.event.get():
                """Exit Event"""
                if event.type == pygame.QUIT:
                    self.exitUI('credits')
                """Keyboard Events"""
                """Pressed"""
                if event.type == pygame.KEYDOWN:
                    """Escape"""
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                    """War Mode Test"""
                    if event.key == pygame.K_g:
                        self.gamemusic1.stop()
                        self.gamemusic2.play(loops = -1)
                        self.gamemusic2.set_volume(0.25)
            
            """Draw Calls"""
            try:
                if oldmousepos != self.mousepos:
                    """Background"""
                    self.screen.blit(self.defaultbackground,(0,0))
                    """Under Construction"""
                    self.screen.blit(self.workinprogressmessage,(275,300))
                    self.screen.blit(self.underconstruction,(425,75))
                    self.screen.blit(self.defaultcursor,self.mousepos)
            except:
                pass            

            """System"""
            pygame.display.update()
            self.clock.tick(30)
            oldmousepos = self.mousepos

        if mode == 'map':
            self.gamemusic1.stop()
            self.gamemusic2.stop()
            self.menumusic.play(loops = -1)
            self.gameMapSelector(True)
        else: 
            self.menuLoop()

    """Function exitUI, ask if you want to exit"""
    def exitUI(self,gamemode):
        """Draw Calls"""
        """Background"""
        self.screen.blit(self.exitbackground,self.exitbackgroundpos)
        """Question"""
        self.screen.blit(self.exittext,self.exittextpos)
        """Buttons"""
        """Yes"""
        self.screen.blit(self.exitbuttonyes,self.exitbuttonyescoll)
        self.screen.blit(self.exitbuttonyestext,self.exitbuttonyestextcoll)
        """No"""
        self.screen.blit(self.exitbuttonno,self.exitbuttonnocoll)
        self.screen.blit(self.exitbuttonnotext,self.exitbuttonnotextcoll)
        oldmousepos = (0,0)

        while True:
            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            """Events Manager"""
            for event in pygame.event.get():
                """Mouse Events"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseclicked = True
                else:
                    self.mouseclicked = False
            
            if oldmousepos != self.mousepos:
                """Draw Calls"""
                """Background"""
                self.screen.blit(self.exitbackground,self.exitbackgroundpos)
                """Question"""
                self.screen.blit(self.exittext,self.exittextpos)
                """Buttons"""
                """Yes"""
                self.screen.blit(self.exitbuttonyes,self.exitbuttonyescoll)
                self.screen.blit(self.exitbuttonyestext,self.exitbuttonyestextcoll)
                """No"""
                self.screen.blit(self.exitbuttonno,self.exitbuttonnocoll)
                self.screen.blit(self.exitbuttonnotext,self.exitbuttonnotextcoll)
                """Mouse"""
                self.screen.blit(self.defaultcursor,self.mousepos)

                """Control"""
                """Mouse Passes Over the Buttons"""
                """Yes"""
                if self.exitbuttonyescoll.collidepoint(self.mousepos) == True:
                    pygame.draw.rect(self.screen,[0,0,255],(self.exitbuttonyescoll))
                    self.screen.blit(self.handcursor,self.mousepos)
                    if self.mouseclicked == True:
                        self.mouseclicked = False
                        pygame.quit()
                        exit()
                """No"""
                if self.exitbuttonnocoll.collidepoint(self.mousepos) == True:
                    pygame.draw.rect(self.screen,[0,0,255],(self.exitbuttonnocoll))
                    self.screen.blit(self.handcursor,self.mousepos)
                    if self.mouseclicked == True:
                        self.mouseclicked = False
                        if gamemode == 'random':
                            self.randomMapMode(True)
                        elif gamemode == 'created':
                            self.preCreatedMapMode(True)
                        elif gamemode == 'menu':
                            self.menuLoop()
                        elif gamemode == 'credits':
                            self.creditsOpen(True)
                        elif gamemode == 'instructions':
                            self.instructionsOpen(True)
                        elif gamemode == 'mode':
                            self.gameMapSelector(True)
            
            """System"""
            pygame.display.update()
            self.clock.tick(30)
            oldmousepos = self.mousepos

    """Function creditsOpen, put the credits on screen"""
    def creditsOpen(self,playing):
        self.playing = playing
        while self.playing == True:
            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            """Events Manager"""
            for event in pygame.event.get():
                """Exit Event"""
                if event.type == pygame.QUIT:
                    self.exitUI('credits')
                """Keyboard Events"""
                """Pressed"""
                if event.type == pygame.KEYDOWN:
                    """Escape"""
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
            
            """Draw Calls"""
            """Background"""
            self.screen.blit(self.defaultbackground,(0,0))
            """Under Construction"""
            self.screen.blit(self.workinprogressmessage,(275,300))
            self.screen.blit(self.underconstruction,(425,75))
            self.screen.blit(self.defaultcursor,self.mousepos)

            """System"""
            pygame.display.update()
            self.clock.tick(30)

        self.menuLoop()

    """Function instructionsOpen, put the instructions on screen"""
    def instructionsOpen(self,playing):
        self.playing = playing
        while self.playing == True:
            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            """Events Manager"""
            for event in pygame.event.get():
                """Exit Event"""
                if event.type == pygame.QUIT:
                    self.exitUI('instructions')
                """Keyboard Events"""
                """Pressed"""
                if event.type == pygame.KEYDOWN:
                    """Escape"""
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
            
            """Background"""
            self.screen.blit(self.defaultbackground,(0,0))
            """Under Construction"""
            self.screen.blit(self.workinprogressmessage,(275,300))
            self.screen.blit(self.underconstruction,(425,75))
            self.screen.blit(self.defaultcursor,self.mousepos)

            """System"""
            pygame.display.update()
            self.clock.tick(30)

        self.menuLoop()
        
    """Function gameMapSelector, is the game map selector"""
    def gameMapSelector(self,playing):
        self.loadingBarProgress(2)
        self.playing = playing
        while self.playing == True:
            """Mouse"""
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            """Events Manager"""
            for event in pygame.event.get():
                """Exit Event"""
                if event.type == pygame.QUIT:
                    self.exitUI('mode')
                """Keyboard Events"""
                """Pressed"""
                if event.type == pygame.KEYDOWN:
                    """Escape"""
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                """Mouse Events"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseclicked = True
                else:
                    self.mouseclicked = False

            """Draw Calls"""
            """Background"""
            self.screen.blit(self.defaultbackground,(0,0))
            """Buttons"""
            """Play Random"""
            self.screen.blit(self.randomplaybutton,self.randomplaybuttoncoll)
            self.screen.blit(self.randomplaybuttontext,self.randomplaybuttontextcoll)
            """Play Pre-Created"""
            self.screen.blit(self.createdplaybutton,self.createdplaybuttoncoll)
            self.screen.blit(self.createdplaybuttontext,self.createdplaybuttontextcoll)
            """Mouses"""
            if self.createdplaybuttoncoll.collidepoint(self.mousepos) == True or self.randomplaybuttoncoll.collidepoint(self.mousepos) == True:
                self.screen.blit(self.handcursor,self.mousepos)
            else:
                self.screen.blit(self.defaultcursor,self.mousepos)

            """Control"""
            """Mouse Passes Over the Buttons"""
            """Random Map"""
            if self.randomplaybuttoncoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.randomplaybuttoncoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.menumusic.stop()
                    self.randomGameMode()
            """Pre-Created Map"""
            if self.createdplaybuttoncoll.collidepoint(self.mousepos) == True:
                pygame.draw.rect(self.screen,[0,0,255],(self.createdplaybuttoncoll))
                self.screen.blit(self.handcursor,self.mousepos)
                if self.mouseclicked == True:
                    self.mouseclicked = False
                    self.menumusic.stop()
                    self.preCreatedGameMode()

            """System"""
            pygame.display.update()
            self.clock.tick(30)

        self.menuLoop()

    """Function createBoard, creates the gameboard from the GameBoard class and assigns a biome to each cell"""
    def createBoard(self):
        self.board = GameBoard()
        self.board.assignSize(len(self.mapObj))
        for x in range(len(self.mapObj)):
            for y in range(len(self.mapObj[0])):
                self.board.addCellAndBiome(x,y,self.mapObj[x][y])

    """Function writeMap, creates a surface and draws on it the map tile by tile. After that, it returns the map updated on the game screen"""
    def writeMap(self):
        mapWidth = len(self.mapObj) * self.tileWidth
        mapHeight = len(self.mapObj[0]) * self.tileHeight
        
        # Crea una superficie donde dibujar el mapa
        mapSurf = pygame.Surface((mapWidth, mapHeight))

        # Obtiene la posicion del personaje
        positionX,positionY = self.character.getPosition()

        self.board.hideAllCells()

        # Dibuja todas las casillas del mapa generando una superficie nueva 
        for x in range(len(self.mapObj)):
            for y in range(len(self.mapObj[x])):

                if ((x - positionX)**2 + (y - positionY)**2)**(1/2) <= 3:
                    self.board.revealCell(x, y) 
                                    
                if self.board.getVisibility(x, y) == True:                
                    spaceRect = pygame.Rect(x*self.tileWidth, y*self.tileHeight, self.tileWidth, self.tileHeight)
                    baseTile = self.biometiles[self.board.checkBiome(x, y)]

                    # Dibuja el la casilla con el bioma en la superficie
                    mapSurf.blit(baseTile, spaceRect)
                else:
                    spaceRect = pygame.Rect(x*self.tileWidth, y*self.tileHeight, self.tileWidth, self.tileHeight)
                    baseTile = self.biometiles[' ']

                    # Dibuja el la casilla con el bioma en la superficie
                    mapSurf.blit(baseTile, spaceRect)

        # Dibuja al personaje 
        spaceRect = pygame.Rect(positionX * self.tileWidth, positionY * self.tileHeight, self.tileWidth, self.tileHeight)
        baseCharacter =self.foundersprite
        mapSurf.blit(baseCharacter, spaceRect)
        
        return mapSurf

    """Function readMap, searchs the txt file, reads it and gets the information from the text lines related with the game map. After that, transfers the information to a womb created on the function"""
    def readMap(self,file):
        # Verifica que exista el archivo y si existe abre el archivo
        assert os.path.exists(file), 'Cannot find the level file: %s' % (file)
        mapFile = open(file, "r")

        # Almacena la informacion de adentro y cierra el archivo
        content = mapFile.readlines() + ["\r\n"]
        mapFile.close()

        mapTextLines = []
        mapObject = []

        # Lee cada linea del archivo de texto
        for lineNum in range(len(content)):
            line = content[lineNum].rstrip('\r\n')

            # Si encuentra un ";" en la linea actual devuelve ""
            if ";" in line:
                line = line[:line.find(";")]

            # Si tiene algo lo añade a la lista con las lineas de texto del mapa
            if line != "":
                mapTextLines.append(line)
            elif line == "" and len(mapTextLines) > 0:
                maxWidth = -1
                # Busca la fila mas larga de todas
                for i in range(len(mapTextLines)):
                    if len(mapTextLines[i]) > maxWidth:
                        maxWidth = len(mapTextLines[i])
                # Las empareja llenando con espacios si es que hace falta
                for i in range (len(mapTextLines)):
                    mapTextLines[i] += " " * (maxWidth - len(mapTextLines[i]))
                # Añade una lista por cada linea de mapa
                for x in range (len(mapTextLines[0])):
                    mapObject.append([])
                # Invierte el mapa para que quede al derecho en la matriz
                for y in range (len(mapTextLines)):
                    for x in range (maxWidth):
                        mapObject[x].append(mapTextLines[y][x])

        return mapObject

    """Function movementPosible, gets the biome from the cell and, if is possible to walk on it, returns True, if not, returns False"""
    def movementPosible(self,posX,posY):
        if posX >= 0 and posY >= 0:
            try:
                biome = self.board.checkBiome(posX, posY)
                if biome == "X":
                    return True
                else:
                    return False
            except:
                return False
        else:
            return False
    
    """Function setPositionRandom, selects 2 random positions to spawn the player"""
    def setPositionRandom(self,width,height):
        while True:
            positionX = random.randrange(0, width + 1)
            positionY = random.randrange(0, height + 1)
            if self.movementPosible(positionX,positionY) == True:
                break
        return positionX,positionY

    """Function preCreatedGameMode"""
    def preCreatedGameMode(self):
        mapWidth = len(self.mapObj) * self.tileWidth
        mapHeight = len(self.mapObj[0]) * self.tileHeight
        mapNeedRedraw = True # verdadero para qe llame a drawMap()

        self.character = Character()
        posX, posY = self.setPositionRandom(len(self.mapObj), len(self.mapObj[0]))
        self.character.setPosition(posX, posY)

        # Registra cuanto se movio la camara de su punto original
        cameraSetOffX = 0
        cameraSetOffY = 0 

        # Establece el limite de hasta donde puede moverse la camara
        max_cam_move_X = abs(self.half_winWIdth - int(mapWidth/2))
        max_cam_move_Y = abs(self.half_winHeight - int(mapHeight/2))

        playing = True

        # Comienza el loop del juego hasta que el juegador cierre el juego
        while playing == True: 

            # Registra y obtiene todos los eventos que realizo el usuario como un click o apretar una tecla
            for event in pygame.event.get():
                if event.type == QUIT:
                    # El usuario presiono la "X" para cerrar la aplicacion
                    playing = False

                # Maneja las teclas que fueron presionadas
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        self.cameraleft = True
                    if event.key == K_d:
                        self.cameraright = True
                    if event.key == K_s:
                        self.cameradown = True
                    if event.key == K_w:
                        self.cameraup = True
                        
                    if event.key == K_UP:
                        posX, posY = self.character.getPosition()
                        if self.movementPosible(posX, posY - 1):
                            self.character.setPosition(posX, posY - 1)
                            mapNeedRedraw = True
                    elif event.key == K_DOWN:
                        posX, posY = self.character.getPosition()
                        if self.movementPosible(posX, posY + 1):
                            self.character.setPosition(posX, posY + 1)
                            mapNeedRedraw = True
                    if event.key == K_LEFT:
                        posX, posY = self.character.getPosition()
                        if self.movementPosible(posX - 1, posY):
                            self.character.setPosition(posX - 1, posY)
                            mapNeedRedraw = True
                    elif event.key == K_RIGHT:
                        posX, posY = self.character.getPosition()
                        if self.movementPosible(posX + 1, posY):
                            self.character.setPosition(posX + 1, posY)
                            mapNeedRedraw = True
                    
                # Maneja las teclas que fueron soltadas
                if event.type == KEYUP:
                    if event.key == K_a:
                        self.cameraleft = False                    
                    if event.key == K_d:
                        self.cameraright = False
                    if event.key == K_w:
                        self.cameraup = False
                    if event.key == K_s:
                        self.cameradown = False

            # Si mapNeedRedraw entonces se recarga el mapa
            if mapNeedRedraw:
                mapSurf = self.writeMap()
                mapNeedRedraw = False
            
            # Cambia la variable del movimiento de la camara si el usuario presiono la tecla y no supera el limite
            if self.cameraup and cameraSetOffY < max_cam_move_Y:
                cameraSetOffY += self.cameraspeed
            if self.cameradown and cameraSetOffY > -max_cam_move_Y:
                cameraSetOffY -= self.cameraspeed
            if self.cameraleft and cameraSetOffX < max_cam_move_X:
                cameraSetOffX += self.cameraspeed
            if self.cameraright and cameraSetOffX > -max_cam_move_X:
                cameraSetOffX -= self.cameraspeed

            # Ajusta el centro del mapa segun que tanto lo movio el usuario del centro
            mapRect = mapSurf.get_rect()
            mapRect.center = (self.half_winWIdth + cameraSetOffX, self.half_winHeight + cameraSetOffY)

            self.screen.fill((0,0,0))

            # Dibuja el mapa en la pantalla del display
            self.screen.blit(mapSurf, mapRect)

            pygame.display.update()
            self.clock.tick(60)

        self.gameMapSelector(True)
    
    """Function generateRandomWorld, creates the world randomly"""
    def generateRandomWorld(self, offset_pos_x, offset_pos_y):

        M_width = self.width * 32
        M_height = self.height * 32

        M_surf = pygame.Surface((M_width, M_height))
        for y in range(self.height):
            for x in range(self.width):
                spaceRect = pygame.Rect((x * 32) , (y * 32) , 32, 32)
                tile = pygame.image.load('resources/icons/map/floor/' + str(self.world.getTiles(y, x)) + '.png').convert()
                
                if ((x-(self.character_pos_x/32))**2 + (y-(self.character_pos_y/32))**2)**(1/2) <= 5:
                    self.world.cellsr[y][x].revealed = True
                    
                if self.world.cellsr[y][x].revealed == True:
                    M_surf.blit(tile, spaceRect)
                else:
                    M_surf.blit(self.hidden, spaceRect)
                
                if self.world.getTiles(y, x) == "Mountain" or self.world.getTiles(y, x) == "Water" or y == 0 or x == 0 or y == 220 or x == 390:
                    self.nonreachables.append(str(x * 32)+ " " +str(y * 32))
        return M_surf
    
    """Function checkCharacPos, checks the position of the character"""
    def checkCharacPos(self, mov_pos_x, mov_pos_y, offset_pos_x, offset_pos_y):
        #posicion previa
        prev_pos_x =self.character_pos_x
        prev_pos_y =self.character_pos_y
        #posicion nueva
        self.character_pos_x += mov_pos_x
        self.character_pos_y += mov_pos_y
        coord= str(self.character_pos_x)+ " " + str(self.character_pos_y)

        #revisar si la celda esta libre
        if not coord in self.nonreachables:
            self.screen.blit(self.foundersprite,(self.character_pos_x + offset_pos_x, self.character_pos_y + offset_pos_y))
            return True
        else:
            self.character_pos_x = prev_pos_x
            self.character_pos_y = prev_pos_y
            return False

    """Function randomGameMode"""
    def randomGameMode(self):
        self.world = GameBoard()
        self.world.randomWorld()
        self.character_pos_x = 576
        self.character_pos_y = 320
        offset_pos_y = 0
        offset_pos_x = 0
        mov_pos_y = 0
        mov_pos_x = 0
        loop = True
        Map_surf = self.generateRandomWorld(offset_pos_x, offset_pos_y)
        while loop == True:
            '''Mouse'''
            self.mousepos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            for event in pygame.event.get():
                mov_pos_y = 0
                mov_pos_x = 0
                
                #salir del juego con cruz
                if event.type == pygame.QUIT:
                    loop = False

                if event.type == pygame.KEYDOWN:

                    #movimiento del personaje
                    if event.key == K_w:
                        mov_pos_y = -32
                    if event.key == K_s:
                        mov_pos_y = 32
                    if event.key == K_a:
                        mov_pos_x = -32
                    if event.key == K_d:
                        mov_pos_x = 32
                    
                    #movimiento del mapa
                    if event.key == K_UP and offset_pos_y <= -(self.screensy/self.height):
                        offset_pos_y += 32
                    if event.key == K_DOWN and offset_pos_y >= -(self.screensy/self.height):
                        offset_pos_y -= 32
                    if event.key == K_LEFT and offset_pos_x <= -(self.screensx/self.width):
                        offset_pos_x += 32
                    if event.key == K_RIGHT and offset_pos_x >= -(self.screensx/self.width):
                        offset_pos_x -= 32
                    
                    if event.key == K_ESCAPE:
                        loop = False

                    Map_surf = self.generateRandomWorld(offset_pos_x, offset_pos_y)
            self.screen.blit(Map_surf,(0 + offset_pos_x,0 + offset_pos_y))        
            self.generateRandomWorld(offset_pos_x, offset_pos_y)  
            self.checkCharacPos(mov_pos_x, mov_pos_y, offset_pos_x, offset_pos_y)
 
            mov_pos_y = 0
            mov_pos_x = 0

            self.screen.blit(self.defaultcursor,self.mousepos)
            pygame.display.update()
            self.clock.tick(60)
            
        self.gameMapSelector(True)

"""Main"""
if __name__ == '__main__':
    startingame = GameMain()
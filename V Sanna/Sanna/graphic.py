import random, sys, copy, os, pygame
from pygame.locals import *

winWidth = 800 # Ancho de la ventana en pixeles
winHeight = 600 # Alto de la ventana
half_winWIdth = int(winWidth/2)
half_winHeight = int(winHeight/2)

pygame.init()
FPSCLOCK = pygame.time.Clock()

# El ancho y el alto de cada casilla en pixeles
tileWidth = 32
tileHeight = 32

# Genera la ventana donde se muestra el juego
screen = pygame.display.set_mode((winWidth, winHeight))

# Define la velocidad de movimiento de la camara
cameraMove = 0.5

# Diccionario con las imagenes a cargar en base al caracter escrito en el txt
biomeTiles = {"X": pygame.image.load("floor/Dirt.png"),
              "Y": pygame.image.load("floor/Mountain.png"),
              "M": pygame.image.load("floor/Water.png")}

def runGame(mapState):
    mapObj = mapState["mapObj"]
    mapWidth = mapState["width"]
    mapHeight = mapState["height"]
    mapNeedRedraw = True # verdadero para qe llame a drawMap()

    # Registra cuanto se movio la camara de su punto original
    cameraSetOffX = 0
    cameraSetOffY = 0 

    # Establece el limite de hasta donde puede moverse la camara
    max_cam_move_X = abs(half_winWIdth - int(mapWidth/2)) - tileWidth
    max_cam_move_Y = abs(half_winHeight - int(mapHeight/2)) - tileHeight

    # Rastrea si las teclas para mover la camara estan presionadas 
    cameraUp = False
    cameraDown = False
    cameraLeft = False
    cameraRight = False

    # Comienza el loop del juego hasta que el juegador cierre el juego
    while True: 

        # Registra y obtiene todos los eventos que realizo el usuario como un click o apretar una tecla
        for event in pygame.event.get():
            if event.type == QUIT:
                # El usuario presiono la "X" para cerrar la aplicacion
                terminate()

            # Maneja las teclas que fueron presionadas
            if event.type == KEYDOWN:
                if event.key == K_a:
                    cameraLeft = True
                if event.key == K_d:
                    cameraRight = True
                if event.key == K_s:
                    cameraDown = True
                if event.key == K_w:
                    cameraUp = True

            # Maneja las teclas que fueron soltadas
            if event.type == KEYUP:
                if event.key == K_a:
                    cameraLeft = False
                if event.key == K_d:
                    cameraRight = False
                if event.key == K_w:
                    cameraUp = False
                if event.key == K_s:
                    cameraDown = False

            # Si mapNeedRedraw entonces se recarga el mapa
        if mapNeedRedraw:
            mapSurf = writeMap(mapState)
            mapNeedRedraw = False
        
        if cameraUp and cameraSetOffY < max_cam_move_X:
            cameraSetOffY += cameraMove
        if cameraDown and cameraSetOffY > -max_cam_move_X:
            cameraSetOffY -= cameraMove
        if cameraLeft and cameraSetOffX < max_cam_move_Y:
            cameraSetOffX += cameraMove
        if cameraRight and cameraSetOffX > -max_cam_move_Y:
            cameraSetOffX -= cameraMove

        # Ajusta el centro del mapa segun que tanto lo movio el usuario del centro
        mapRect = mapSurf.get_rect()
        mapRect.center = (half_winWIdth + cameraSetOffX, half_winHeight + cameraSetOffY)

        screen.fill((0,0,0))

        # Dibuja el mapa en la pantalla del display
        screen.blit(mapSurf, mapRect)

        pygame.display.update()
        FPSCLOCK.tick()

def writeMap(mapState):
    """Crea una superficie y dibuja sobre ella el mapa ingresado 
       dibujando casillas por casilla para luego devolverlo e
       actualizarlo en la pantalla principal"""

    mapObj = mapState["mapObj"]
    mapWidth = mapState["width"] * tileWidth
    mapHeight = mapState["height"] * tileHeight
    
    # Crea una superficie donde dibujar el mapa
    mapSurf = pygame.Surface((mapWidth, mapHeight))

    # Dibuja todas las casillas del mapa generando una superficie nueva 
    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            spaceRect = pygame.Rect(x*tileWidth, y*tileHeight, tileWidth, tileHeight)
            baseTile = biomeTiles[mapObj[x][y]]

            # Dibuja el la casilla con el bioma en la superficie
            mapSurf.blit(baseTile, spaceRect)
    
    return mapSurf

def readMap(file):
    """Agarra el archivo de texto ingresado lo busca y si lo encuentra,
    lo lee y obtiene la informacion de las lineas de texto relacionadas con el mapa
    para luego tranferir los datos de las lineas a una matriz generada en la funcion."""
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

            mapState = {"width": len(mapObject[0]),
                        "height": len(mapObject),
                        "mapObj": mapObject}

    return mapState

def terminate():
    """Finaliza el programa y cierra todo"""
    pygame.quit()
    sys.exit()

mapState = readMap("maps/map1.txt")
runGame(mapState)
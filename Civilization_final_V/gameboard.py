import random,os
from cell import Cell
from character import Character

class GameBoard():

    def __init__(self,width,height):
        """Function __init__"""
        self.width = width
        self.height = height
        self.Unit = []
        self.mapObj = []
        self.mapToText = {"Barrier" : "B",
                            "Dirt" : "D",
                            "Water" : "W",
                            "Mountain" :"M",
                            "Revealed" :"R",
                            "Hidden" : "H"}
        self.numberToBiomes = {1 : "W",
                                2 : "D",
                                3 : "D", 
                                4: "D"}
        self.CrearTablero()

    def CrearTablero(self):
        """ crea un tablero de width por height """
        for columna in range (0, self.height):
            lista = []
            for fila in range (0, self.width):
                lista.append(Cell())
            self.mapObj.append(lista)                  

    def biomeRandom(self):
        """ genera biomas aleatoriamente """
        biome = self.numberToBiomes[random.randrange(1,5)]
        return biome

    def randomWorld(self):
        """ crea el mundo aleatoriamente y lo filtra """
        for Y in range(self.height):
            for x in range(self.width):
                ran = str(self.biomeRandom())
                self.mapObj[Y][x].setBiome(ran)

        for Y in range(self.height):
            for x in range(self.width):
                #bordes
                if x == 0 or Y == 0 or x == (self.width-1) or Y == (self.height-1):
                    continue
                
                #tierra firme
                if (self.mapObj[Y + 1 ][x].biome == "D" or self.mapObj[Y + 1 ][x].biome == "F" or self.mapObj[Y + 1 ][x].biome == "M") and (self.mapObj[Y][x + 1].biome == "D" or self.mapObj[Y][x + 1].biome == "F" or self.mapObj[Y][x + 1].biome == "M") and (self.mapObj[Y][x - 1].biome == "D" or self.mapObj[Y][x - 1].biome == "F" or self.mapObj[Y][x - 1].biome == "M"):
                    self.mapObj[Y][x].setBiome("D")
                    #montañas
                    mountain = random.randrange(1,16)
                    if mountain == 1:
                        mineral = random.randrange(1,11)
                        if mineral <= 5:
                            self.mapObj[Y][x].setBiome("I")
                        if mineral > 5 and mineral <= 7 :
                            self.mapObj[Y][x].setBiome("G")
                        if mineral > 7 and mineral <= 10 :
                            self.mapObj[Y][x].setBiome("M")
                    continue
                
                #rios
                if self.mapObj[Y + 1][x].biome == "W" and self.mapObj[Y - 1][x].biome == "W" and self.mapObj[Y][x - 1].biome == "W":
                    lake = random.randrange(1,6)
                    if lake == 1:
                        self.mapObj[Y][x].setBiome("W")        
                    else:
                        self.mapObj[Y][x].setBiome("D")
                
                #forests
                if self.mapObj[Y][x].biome == "D" :
                    forest = random.randrange(1,6)
                    if forest == 1:
                        self.mapObj[Y][x].setBiome("F")      
                    if self.mapObj[Y + 1 ][x].biome == "F" and self.mapObj[Y][x + 1].biome == "F" and self.mapObj[Y][x - 1].biome == "F":
                        self.mapObj[Y][x].setBiome("F")      
                    continue

        self.documentTxt("resources/maps/map2.txt")
        f = open("resources/maps/map2.txt", "a+")
        for y in range(self.height):
            f.write("\n")
            for x in range(self.width):
                tile = self.getTiles(y, x)
                f.write(tile)

    def saveGame(self, map):
        print("game saved")
        self.documentTxt("resources/maps/map2.txt")
        f = open("resources/maps/map2.txt", "a+")
        for y in range(len(map[0])):
            f.write("\n")
            for x in range(len(map)):
                f.write(self.getBiome(x, y)) 
    
    def getTiles(self, y, x):
        """ devuelve el bioma de una celda """
        biome = self.mapObj[y][x].biome
        return biome
            
    def setBiome(self, x, y, biome):
        """Añade un objeto Cell a la lista correspondiente y le establece el bioma"""
        self.mapObj[x][y].setBiome(biome)

    def getBiome(self, x, y):
        """  """
        biome = self.mapObj[x][y].getBiome()
        return biome
    
    def addCellAndBiome(self, x, y, biome):
        """Añade un objeto Cell a la lista correspondiente y le establece el bioma"""
        self.mapObj[x].append(Cell())
        self.mapObj[x][y].setBiome(biome)
    
    def assignSize(self, width):
        """Asigna el tamaño del tablero segun el tamaño del mapa"""
        self.mapObj = [] 
        for _ in range(width):
            self.mapObj.append([])
    
    def documentTxt(self,path):
        f = open(path, "w")
        f.write(";Map made by Santella Agustin")
        f.write("\n")
        f.write(";element index")
        f.write("\n")
        f.write(";  D : Diert")
        f.write("\n")
        f.write(";  M : Mountain")
        f.write("\n")
        f.write(";  W : Water")
        f.write("\n")
        f.write("\n")
        f.write("; starting the level:")

    def checkUnit(self, posX, posY):
        """  """
        for x in range(len(self.Unit)):
            pos = self.Unit[x].getPosition()
            if pos == (posX, posY):
                index = self.Unit[x].getIndex()
                return index
        
    def addUnit(self, posX, posY, index, type, team):
        self.Unit.append(Character(type, team))
        self.Unit[index].setPosition(posX, posY)

    def eraseUnits(self):
        self.Unit = []

    def cellOff(self, posX, posY):
            """Cambia la visibilidad de la celda especificada a True"""
            self.mapObj[posX][posY].cellOff()

    def getVisibility(self, posX, posY):
        """Consulta a la celda si esta visible o no"""
        return self.mapObj[posX][posY].getVisibility()
    
    def revealCell(self, posX, posY):
        """Cambia la visibilidad de la celda especificada a True"""
        self.mapObj[posX][posY].showCell()

    def checkCell(self, x, y):
        return self.mapObj[x][y].occupant

    def occupiedCell(self, x, y):
        self.mapObj[x][y].occupant = True
    
    def unoccupiedCell(self, x, y):
        self.mapObj[x][y].occupant = False
    
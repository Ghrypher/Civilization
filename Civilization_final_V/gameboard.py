import random,os
from cell import Cell
from character import Character

class GameBoard():

    def __init__(self,width,height):
        """Function __init__"""
        self.width = width
        self.height = height
        self.Unit = []
        self.M_obj = []
        self.non_reachables =[]
        self.map_to_text = {"Barrier" : "B",
                            "Dirt" : "D",
                            "Water" : "W",
                            "Mountain" :"M",
                            "Revealed" :"R",
                            "Hidden" : "H"}
        self.number_to_biomes = {1 : "W",
                                2 : "D",
                                3 : "D", 
                                4: "D"}
        self.crear_tablero()

    def crear_tablero(self):
        """ crea un tablero de width por height """
        for columna in range (0, self.height):
            lista = []
            for fila in range (0, self.width):
                lista.append(Cell())
            self.M_obj.append(lista)                  

    def biome_random(self):
        """ genera biomas aleatoriamente """
        biome = self.number_to_biomes[random.randrange(1,5)]
        return biome

    def random_world(self):
        """ crea el mundo aleatoriamente y lo filtra """
        for Y in range(self.height):
            for x in range(self.width):
                ran = str(self.biome_random())
                self.M_obj[Y][x].set_biome(ran)

        for Y in range(self.height):
            for x in range(self.width):
                #bordes
                if x == 0 or Y == 0 or x == (self.width-1) or Y == (self.height-1):
                    continue
                
                #tierra firme
                if (self.M_obj[Y + 1 ][x].biome == "D" or self.M_obj[Y + 1 ][x].biome == "F" or self.M_obj[Y + 1 ][x].biome == "M") and (self.M_obj[Y][x + 1].biome == "D" or self.M_obj[Y][x + 1].biome == "F" or self.M_obj[Y][x + 1].biome == "M") and (self.M_obj[Y][x - 1].biome == "D" or self.M_obj[Y][x - 1].biome == "F" or self.M_obj[Y][x - 1].biome == "M"):
                    self.M_obj[Y][x].set_biome("D")
                    #montañas
                    mountain = random.randrange(1,16)
                    if mountain == 1:
                        mineral = random.randrange(1,11)
                        if mineral <= 5:
                            self.M_obj[Y][x].set_biome("I")
                        if mineral > 5 and mineral <= 7 :
                            self.M_obj[Y][x].set_biome("G")
                        if mineral > 7 and mineral <= 10 :
                            self.M_obj[Y][x].set_biome("M")
                    continue
                
                #rios
                if self.M_obj[Y + 1][x].biome == "W" and self.M_obj[Y - 1][x].biome == "W" and self.M_obj[Y][x - 1].biome == "W":
                    lake = random.randrange(1,6)
                    if lake == 1:
                        self.M_obj[Y][x].set_biome("W")        
                    else:
                        self.M_obj[Y][x].set_biome("D")
                
                #forests
                if self.M_obj[Y][x].biome == "D" :
                    forest = random.randrange(1,6)
                    if forest == 1:
                        self.M_obj[Y][x].set_biome("F")      
                    if self.M_obj[Y + 1 ][x].biome == "F" and self.M_obj[Y][x + 1].biome == "F" and self.M_obj[Y][x - 1].biome == "F":
                        self.M_obj[Y][x].set_biome("F")      
                    continue

        self.document_txt("resources/maps/map2.txt")
        f = open("resources/maps/map2.txt", "a+")
        for y in range(self.height):
            f.write("\n")
            for x in range(self.width):
                tile = self.get_tiles(y, x)
                f.write(tile)

    def save_game(self, map):
        print("game saved")
        self.document_txt("resources/maps/map2.txt")
        f = open("resources/maps/map2.txt", "a+")
        for y in range(len(map[0])):
            f.write("\n")
            for x in range(len(map)):
                f.write(self.get_biome(x, y)) 
    
    def get_tiles(self, y, x):
        """ devuelve el bioma de una celda """
        biome = self.M_obj[y][x].biome
        return biome

    def limpiar_tablero(self):
        """ elimina todo bioma almacenado en una celda """
        for x in range (self.height):
            for y in range (self.width):
                self.M_obj[y][x].set_biome("")

    def checkSpace(self, x, y):
        """ revisa si una celda esta libre """
        biome = self.M_obj[x][y].checkSpace()
        return biome
            
    def set_biome(self, x, y, biome):
        """Añade un objeto Cell a la lista correspondiente y le establece el bioma"""
        self.M_obj[x][y].set_biome(biome)

    def get_biome(self, x, y):
        """ busca el bioma de una celda """
        biome = self.M_obj[x][y].get_biome()
        return biome
    
    def addCellAndBiome(self, x, y, biome):
        """Añade un objeto Cell a la lista correspondiente y le establece el bioma"""
        self.M_obj[x].append(Cell())
        self.M_obj[x][y].set_biome(biome)
    
    def assignSize(self, width):
        """Asigna el tamaño del tablero segun el tamaño del mapa"""
        self.M_obj = [] 
        for _ in range(width):
            self.M_obj.append([])
    
    def document_txt(self,path):
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

    def erase_Units(self):
        self.Unit = []

    def cellOff(self, posX, posY):
            """Cambia la visibilidad de la celda especificada a True"""
            self.M_obj[posX][posY].cellOff()

    def getVisibility(self, posX, posY):
        """Consulta a la celda si esta visible o no"""
        return self.M_obj[posX][posY].getVisibility()
    
    def revealCell(self, posX, posY):
        """Cambia la visibilidad de la celda especificada a True"""
        self.M_obj[posX][posY].showCell()

    def checkCell(self, x, y):
        return self.M_obj[x][y].occupant

    def occupiedCell(self, x, y):
        self.M_obj[x][y].occupant = True
    
    def unoccupiedCell(self, x, y):
        self.M_obj[x][y].occupant = False
    
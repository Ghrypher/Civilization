import random, os
from cell import Cell

class Tablero:
    def __init__(self, ancho, alto):
        """ constructor de la clase """
        self.ancho = ancho
        self.alto = alto
        self.M_obj = []
        self.non_reachables =[]
        self.map_to_text = {"Barrier" : "B",
                            "Dirt" : "D",
                            "Water" : "W",
                            "Mountain" :"M",
                            "Revealed" :"R",
                            "Hidden" : "H"}
        self.crear_tablero()


    def crear_tablero(self):
        """ crea un tablero de ancho por alto """
        for columna in range (0, self.alto):
            lista = []
            for fila in range (0, self.ancho):
                lista.append(Cell())
            self.M_obj.append(lista)                  

    def biome_random(self):
        """ genera biomas aleatoriamente """
        biome = number_to_biomes[random.randrange(1,4)]
        return biome

    def random_world(self):
        """ crea el mundo aleatoriamente y lo filtra """
        for Y in range(self.alto):
            for x in range(self.ancho):
                ran = str(self.biome_random())
                self.M_obj[Y][x].set_biome(ran)

        for Y in range(self.alto):
            for x in range(self.ancho):
                #bordes
                if x == 0 or Y == 0 or x == (self.ancho-1) or Y == (self.alto-1):
                    self.M_obj[Y][x].set_biome("B")
                    continue
                
                #tierra firme
                if self.M_obj[Y + 1 ][x].biome == "D" and self.M_obj[Y][x + 1].biome == "D" and self.M_obj[Y][x - 1].biome == "D":
                    self.M_obj[Y][x].set_biome("D")
                    #montañas
                    mountain = random.randrange(1,16)
                    if mountain == 1:
                        self.M_obj[Y][x].set_biome("M")
                        self.M_obj[Y][x].set_coordinates(Y, x)
                        continue

                #rios
                if self.M_obj[Y + 1][x].biome == "W" and self.M_obj[Y - 1][x].biome == "W" or self.M_obj[Y + 1][x].biome == "W" and self.M_obj[Y][x - 1].biome == "W":
                    lake = random.randrange(1,6)
                    if lake == 1:
                        self.M_obj[Y][x].set_biome("W")
                        self.M_obj[Y][x].set_coordinates(Y, x)
                    else:
                        self.M_obj[Y][x].set_biome("D")
                        self.M_obj[Y][x].set_coordinates(Y, x)
                
                #plantas
                if self.M_obj[Y][x].biome == "D":
                    plant = self.plants_random()
                    self.M_obj[Y][x].set_plants(plant)
                    continue

        self.document_txt("Maps/random_world.txt")
        f = open("Maps/random_world.txt", "a+")
        for y in range(self.alto):
            f.write("\n")
            for x in range(self.ancho):
                tile = self.get_tiles(y, x)
                f.write(tile)

    def save_game(self, map):
        print("game saved")
        self.document_txt("Maps/save.txt")
        f = open("maps/save.txt", "a+")
        for y in range(len(map[0])):
            f.write("\n")
            for x in range(len(map)):
                f.write(self.get_biome(x, y))


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
    
    def get_tiles(self, y, x):
        """ devuelve el bioma de una celda """
        self.M_obj[y][x].set_coordinates(x, y)
        biome = self.M_obj[y][x].biome
        return biome

    def limpiar_tablero(self):
        """ elimina todo bioma almacenado en una celda """
        for x in range (self.alto):
            for y in range (self.ancho):
                self.M_obj[y][x].set_biome("")
    
    def plants_random(self):
        """ genera plantas aleatoriamente """
        plants = number_to_plants[random.randrange(1,3)]
        return plants
    
    def check_space(self, coord):
        """ revisa si una celda esta libre """
        if coord in self.non_reachables:
            return False
        else:
            return True
            
    def set_biome(self, x, y, biome):
        """Añade un objeto Cell a la lista correspondiente y le establece el bioma"""
        self.M_obj[x][y].set_biome(biome)

    def get_biome(self, x, y):
        """  """
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

number_to_biomes = {
    1 : "W",
    2 : "D",
    3 : "D" 
    }
    
number_to_plants = {
    1 : "Grass",
    2 : "Tree",
    3 : "Flower"
    }
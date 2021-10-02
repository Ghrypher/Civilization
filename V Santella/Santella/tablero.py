import random
from cell import Cell

class Tablero:
    def __init__(self, ancho, alto):
        """ constructor de la clase """
        self.ancho = ancho
        self.alto = alto
        self.cells = []
        self.non_reachables =[]
        self.crear_tablero()


    def crear_tablero(self):
        """ crea un tablero de 40x23 """
        for columna in range (0, self.alto):
            lista = []
            for fila in range (0, self.ancho):
                lista.append(Cell())
            self.cells.append(lista)                  

    def biome_random(self):
        """ genera biomas aleatoriamente """
        biome = number_to_biomes[random.randrange(1,4)]
        return biome

    def random_world(self):
        """ crea el mundo aleatoriamente y lo filtra """
        for Y in range(self.alto):
            for x in range(self.ancho):
                ran = str(self.biome_random())
                self.cells[Y][x].set_biome(ran)

        for Y in range(self.alto):
            for x in range(self.ancho):
                #bordes
                if x == 0 or Y == 0 or x == (self.ancho-1) or Y == (self.alto-1):
                    self.cells[Y][x].set_biome("Barrier")
                    continue
                
                #rios
                if self.cells[Y + 1][x].biome == "Water" and self.cells[Y - 1][x].biome == "Water" or self.cells[Y + 1][x].biome == "Water" and self.cells[Y][x - 1].biome == "Water":
                    lake = random.randrange(1,6)
                    if lake == 1:
                        self.cells[Y][x].set_biome("Water")
                        self.cells[Y][x].set_coordinates(Y, x)
                
                #tierra firme
                if self.cells[Y + 1 ][x].biome == "Dirt" and self.cells[Y][x + 1].biome == "Dirt" and self.cells[Y][x - 1].biome == "Dirt":
                    self.cells[Y][x].set_biome("Dirt")
                    #montañas
                    mountain = random.randrange(1,11)
                    if mountain == 1:
                        self.cells[Y][x].set_biome("Mountain")
                        self.cells[Y][x].set_coordinates(Y, x)
                        continue
                
                #plantas
                if self.cells[Y][x].biome == "Dirt":
                    plant = self.plants_random()
                    self.cells[Y][x].set_plants(plant)
                    continue
    
    def background_world(self):
        """ crea el mundo aleatoriamente y lo filtra """
        for Y in range(23):
            for x in range(40):
                ran = str(self.biome_random())
                self.cells[Y][x].set_biome(ran)

        for Y in range(23):
            for x in range(40):
                #bordes
                if x == 0 or Y == 0 or x == 39 or Y == 22:
                    continue

                #rios
                if self.cells[Y + 1][x].biome == "Water" and self.cells[Y - 1][x].biome == "Water" or self.cells[Y + 1][x].biome == "Water" and self.cells[Y][x - 1].biome == "Water":
                    lake = random.randrange(1,6)
                    if lake == 1:
                        self.cells[Y][x].set_biome("Water")
                        self.cells[Y][x].set_coordinates(Y, x)
                
                #tierra firme
                if self.cells[Y + 1 ][x].biome == "Dirt" and self.cells[Y][x + 1].biome == "Dirt" and self.cells[Y][x - 1].biome == "Dirt":
                    self.cells[Y][x].set_biome("Dirt")
                    #montañas
                    mountain = random.randrange(1,11)
                    if mountain == 1:
                        self.cells[Y][x].set_biome("Mountain")
                        self.cells[Y][x].set_coordinates(Y, x)
                        continue
                
                #plantas
                if self.cells[Y][x].biome == "Dirt":
                    plant = self.plants_random()
                    self.cells[Y][x].set_plants(plant)
                    continue
    
    def get_tiles(self, y, x):
        """ devuelve el bioma de una celda """
        self.cells[y][x].set_coordinates(x, y)
        biome = self.cells[y][x].biome
        return biome

    def limpiar_tablero(self):
        """ elimina todo bioma almacenado en una celda """
        for x in range (self.alto):
            for y in range (self.ancho):
                self.cells[y][x].set_biome("")
    
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
            
    def addCellAndBiome(self, x, y, biome):
        """Añade un objeto Cell a la lista correspondiente y le establece el bioma"""
        self.cells[x].append(Cell())
        self.cells[x][y].set_biome(biome)

number_to_biomes = {
    1 : "Water",
    2 : "Dirt",
    3 : "Dirt" 
    }
    
number_to_plants = {
    1 : "Grass",
    2 : "Tree",
    3 : "Flower"
    }
import random
from cell import Cell

class Tablero:
    def __init__(self):
        """ constructor de la clase """
        self.ancho = 40
        self.alto = 23
        self.cells =[]
        self.crear_tablero()
        self.random_world() 

    def crear_tablero(self):
        for columna in range (0, self.alto):
            lista = []
            for fila in range (0, self.ancho):
                lista.append(Cell())
            self.cells.append(lista)                  

    def biome_random(self):
        biome = number_to_biomes[random.randrange(1,4)]
        return biome

    def random_world(self):
        """ coloca biomas en las zonas del tablero """
        for Y in range(23):
            for x in range(40):
                ran = str(self.biome_random())
                self.cells[Y][x].set_biome(ran)

        for Y in range(23):
            for x in range(40):
                #bordes
                if x == 0 or Y == 0 or x == 39 or Y == 22:
                    self.cells[Y][x].set_biome("Dirt")
                    continue
                
                #rios
                if self.cells[Y + 1][x].biome == "Water" and self.cells[Y - 1][x].biome == "Water" or self.cells[Y + 1][x].biome == "Water" and self.cells[Y][x - 1].biome == "Water":
                    self.cells[Y][x].set_biome("Water")
                    continue
                
                #tierra firme
                if self.cells[Y + 1 ][x].biome == "Dirt" and self.cells[Y][x + 1].biome == "Dirt" and self.cells[Y][x - 1].biome == "Dirt":
                    self.cells[Y][x].set_biome("Dirt")
                    #montañas
                    mountain = random.randrange(1,11)
                    if mountain == 1:
                        self.cells[Y][x].set_biome("Mountain")
                        continue
                
                #plants
                if self.cells[Y][x].biome == "Dirt":
                    plant = self.plants_random()
                    self.cells[Y][x].set_plants(plant)
                    continue
    
    def get_tiles(self, y, x):
        biome = self.cells[y][x].biome
        return biome

    def limpiar_tablero(self):
        """ elimina todo barco almacenado en una cell """
        for x in range (1, self.ancho + 1):
            for y in range (1, self.alto + 1):
                self.cells[y][x].set_biome("")
    
    def plants_random(self):
        plants = number_to_plants[random.randrange(1,4)]
        return plants

number_to_biomes = {
    1 : "Water",
    2 : "Mountain",
    3 : "Dirt"
    }
    
number_to_plants = {
    1 : "Grass",
    2 : "Tree",
    3 : "Flower"
    }
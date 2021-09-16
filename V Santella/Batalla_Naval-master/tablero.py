import random
from cell import Cell

class Tablero:
    def __init__(self, ancho, alto):
        """ constructor de la clase """
        self.ancho = 40
        self.alto = 23
        self.cells =[]
        self.establecer_tamaño(ancho, alto)
        self.crear_tablero()
        self.random_world() 

    def establecer_tamaño(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def crear_tablero(self):
        for columna in range (0, self.ancho):
            lista = []
            for fila in range (0, self.alto):
                lista.append(cell())
            self.cells.append(lista)
                  

    def randomworld(self):
        """ coloca biomas en las zonas del tablero """

        for Y in range(23):
            for x in range(40):
                #bordes
                if x == 1 or y == 1 or x == 40 or y == 23:
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
                    self.cells[2 + Y][2 + x].set_plants(plant)
                    continue
    

    def limpiar_tablero(self):
        """ elimina todo barco almacenado en una cell """
        for x in range (1, self.ancho + 1):
            for y in range (1, self.alto + 1):
                self.cells[Y][x].set_biome("")


    def biome_random(self):
        biome = number_to_biomes(random.randrange(1,4))
        return biome
    
    def plants_random(self):
        plants = number_to_plants(random.randrange(1,4))
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
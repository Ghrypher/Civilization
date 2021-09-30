from cell import Cell

class Board():

    def __init__(self):
        """El inicio de la clase, se crean las variables que pertenecen
           a la misma"""
        self.celdas = []

    def addCellAndBiome(self, x, y, biome):
        """Añade un objeto Cell a la lista correspondiente y le establece el bioma"""
        self.celdas[x].append(Cell())
        self.celdas[x][y].setBiome(biome)
    
    def assignSize(self, width):
        """Asigna el tamaño del tablero segun el tamaño del mapa"""
        for x in range(width):
            self.celdas.append([])

    def checkBiome(self, posX, posY):
        return self.celdas[posX][posY].readBiome()


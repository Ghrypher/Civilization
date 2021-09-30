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
        """Consulta y devuelve el bioma de la celda a consultar"""
        return self.celdas[posX][posY].readBiome()

    def hideAllCells(self):
        """Hace que la visibilidad de todas las celdas sea falsa"""
        for x in range(len(self.celdas)):
            for y in range(len(self.celdas[0])):
                self.celdas[x][y].hideCell()
    
    def revealCell(self, posX, posY):
        """Cambia la visibilidad de la celda especificada a True"""
        self.celdas[posX][posY].showCell()
    
    def getVisibility(self, posX, posY):
        """Consulta a la celda si esta visible o no"""
        return self.celdas[posX][posY].getVisibility()



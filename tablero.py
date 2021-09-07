import random
from celda import Celda

class Tablero:
    """ clase tablero almacena las celdas y barcos """

    def __init__(self, ancho, alto):
        """ constructor de la clase """
        self.ancho = None
        self.alto = None
        self.barcos = []
        self.celdas =[]
        self.establecer_tamaño(ancho, alto)
        self.crear_tablero() 

    def establecer_tamaño(self, ancho, alto):
        """ establece las dimensiones del tablero """
        self.ancho = ancho
        self.alto = alto

    def crear_tablero(self):
        """ crea el tablero mediante una matriz de celdas """
        for columna in range (0, self.ancho):
            lista = []
            for fila in range (0, self.alto):
                lista.append(Celda())
            self.celdas.append(lista)          

    def colocar_barco(self, posicion_x, posicion_y):
        """ coloca barcos en las celdas del tablero """
        verificador = self.celdas[posicion_y][posicion_x].verificar_celda()
        if not verificador:
            barco = self.celdas[posicion_y][posicion_x].posicionar_barco()
            self.barcos.append(barco)
            return True
        else:
            return False

    def lanzar(self, posicion_x, posicion_y):
        """ "ataca" y indica si se golpeo algo """
        resultado, barco = self.celdas[posicion_y][posicion_x].atacar()
        if resultado:
            print ("Hundido!!!")
            self.barcos.remove(barco)
            return True
        else:
            print ("Agua")
            return False
    
    def limpiar_tablero(self):
        """ elimina todo barco almacenado en una celda """
        for x in range (1, self.ancho + 1):
            for y in range (self.alto + 1):
                print(self.sacar_barco(x, y))
            
    def aleatorizar_barcos(self):
        """ coloca barcos en las celdas del tablero  """
        for x in range (8):
            verificador = True
            while verificador:
                posicion_x = random.randrange(0, self.alto)
                posicion_y = random.randrange(0, self.ancho)
                verificador = self.celdas[posicion_y][posicion_x].verificar_celda()
                if not verificador :
                    self.colocar_barco(posicion_x, posicion_y)
    
    def sacar_barco(self, posicion_x, posicion_y):
        """ remueve un barco de una celda especifica """
        verificador = self.celdas[posicion_y - 1][posicion_x - 1].verificar_celda()
        if verificador:
            barco = self.celdas[posicion_y - 1][posicion_x - 1].eliminar_barco()
            self.barcos.remove(barco)
            print ("barco eliminado exitosamente")
        else:
            print ("no hay un barco en la celda")
    
    def verificar_barcos(self):
        """ verifica si hay barcos en el tablero """
        if self.barcos == []:
            return False          
        else: 
            return True

    def revisar_ataque(self, posicion_x, posicion_y):
        """ revisa si ya se ha atacado la celda indicada """
        resultado = self.celdas[int(posicion_y)][int(posicion_x)].buscar_metralla()
        return resultado

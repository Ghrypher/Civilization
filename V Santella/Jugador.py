from tablero import Tablero

class Jugador: 
    """ clase jugador realiza las solicitudes de datos """

    def __init__(self, ancho, alto, orden):
        """ constructor de la clase """
        self.nombre = ""
        self.ancho_tablero = int(ancho)
        self.alto_tablero = int(alto)
        self.identificarse(orden)
        self.tablero = Tablero(ancho, alto)
    
    def barcos_randoms(self):
        """ lleva el mensaje, de colocar barcos al azar, a el tablero  """
        self.tablero.aleatorizar_barcos()

    def colocar_barcos(self):
        """ colocar barcos a peticion del jugador en el tablero  """
        for x in range(8):
            print("barco numero" + str(x + 1) + "/8") 
            verificador = False
            while not verificador:

                # solicita y verifica la columna
                try:
                    posicion_x = int(input("Ingrese la columna(1, 2, 3...): "))
                except:
                    print("ingrese un valor numerico")
                    continue
                
                # solicita y traduce la fila 
                posicion_y = input("Ingrese la fila(A, B, C...): ")
                try:
                    posicion_y = letras_a_numeros[posicion_y.upper()]
                except:
                    print ("La fila ingresada no existe.")
                    continue
                
                # revisa que las coordenadas no esten fuera de los limites
                if posicion_x <= self.ancho_tablero and posicion_x != 0 and posicion_y <= self.alto_tablero:
                    verificador = self.tablero.colocar_barco(posicion_y - 1, posicion_x - 1)
                    if not verificador:
                        print("La casilla esta ocupada")
                else:
                    print("La columna ingresada no existe")
                
        
    def atacar(self):
        """ solicita al jugador las coordenasa y "ataca" la celda solicitada """
        verificador = False
        while not verificador:

            # solicita y verifica la columna a atacar
            try:
                posicion_x = int(input("Ingrese la columna(1, 2, 3...): "))
            except:
                print("ingrese un valor numerico")
                continue
            
            # solicita y traduce la fila a atacar
            posicion_y = input("Ingrese la fila(A, B, C...): ")
            try:
                posicion_y = letras_a_numeros[posicion_y.upper()]
            except:
                print ("La fila ingresada no existe.")
                continue
            
            # revisa que las coordenadas no esten fuera de los limites
            if posicion_x <= self.ancho_tablero and posicion_x != 0 and posicion_y <= self.alto_tablero:
                if self.tablero.revisar_ataque(posicion_y - 1, posicion_x - 1):
                    punto = self.tablero.lanzar(posicion_y - 1, posicion_x - 1)
                    hay_barcos = self.tablero.verificar_barcos()
                    verificador = True
                    return hay_barcos, punto
                else:
                    verificador = False
                    print ("esta celda ya fue atacada")
            else:
                print("La columna ingresada no existe")

            # revisa que la celda no fue atacada previmente
            

    def identificarse(self, orden):
        """ define los nombres de los jugadores """
        if int(orden) == 1:
            self.nombre = input("ingresen el nombre del primer jugador   ")
        else:
            self.nombre = input("ingresen el nombre del segundo jugador   ")


letras_a_numeros = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "Ñ" : 15,
    "O" : 16,
    "P" : 17,
    "Q" : 18,
    "R" : 19,
    "S" : 20,
    "T" : 21,
    "U" : 22,
    "V" : 23,
    "W" : 24,
    "X" : 25,
    "Y" : 26,
    "Z" : 27
    }
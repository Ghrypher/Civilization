from barco import Barco

class Celda:
    """ clase Celda almacena barcos o no """

    def __init__(self):
        """ constructor de la clase """
        self.barco = None
        self.atacada = False

    def posicionar_barco(self):
        """ guarda un objeto barco en la celda """
        self.barco = Barco()
        return self.barco

    def atacar(self):
        """ revisa si hay un barco en la celda y devuelve el resultado del ataque """
        if self.barco != None:
            self.barco.hundir()
            barco = self.eliminar_barco()
            self.atacada = True
            return True, barco
        self.atacada = True
        return False, None

    def eliminar_barco(self):
        """ revisa si hay una barco en la celda y lo remueve """
        if self.barco != None:
            barco = self.barco
            self.barco = None
            return barco
        return None
    
    def verificar_celda(self):
        """ revisa si hay una barco en la celda """
        if self.barco == None:
            return False
        else:
            return True
    
    def buscar_metralla(self):
        """ revisa si la celda ya fue atacada """
        if self.atacada == True:
            return False
        else:
            return True
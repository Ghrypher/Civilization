class Unit():

    def __init__(self, type):
        """Inicio de la clase, crea las variables de la misma"""
        self.life = None
        self.team = None
        self.positionX = None
        self.positionY = None
        self.define(type)

    def define(self, type):
        """" """
    

    def setPosition(self, posX, posY):
        self.positionX = posX
        self.positionY = posY

    def getPosition(self):
        return self.positionX, self.positionY
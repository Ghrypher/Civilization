class Unit():

    def __init__(self):
        """Inicio de la clase, crea las variables de la misma"""
        self.life = None
        self.team = None
        self.positionX = None
        self.positionY = None

    def setPosition(self, posX, posY):
        self.positionX = posX
        self.positionY = posY

    def getPosition(self):
        return self.positionX, self.positionY
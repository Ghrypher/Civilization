class Unit():

    def __init__(self, type,team):
        """Inicio de la clase, crea las variables de la misma"""
        self.life = None
        self.dmg = None
        self.utility = None
        self.type = type
        self.team = team
        self.sprite = None
        self.positionX = None
        self.positionY = None
        self.unit_sorter = {"Wk": self.worker,
                  "WR": self.warrior,
                  "FD": self.founder}
        self.define(type)

    def define(self, type):
        """" """
        self.unit_sorter[type]()


    def setPosition(self, posX, posY):
        self.positionX = posX
        self.positionY = posY

    def worker(self):
        """  """
        self.life = 3
        self.dmg = 1 
        self.utility = "recolection"
        self.sprite = str(self.team) + "_worker.png"

    def founder(self):
        """ """
        self.life = 4
        self.dmg = 1 
        self.utility = "founding"
        self.sprite = str(self.team) + "_Founder.png"

    def warrior(self):
        """ """
        self.life = 5
        self.dmg = 3 
        self.utility = "battle"
        self.sprite = str(self.team) + "_Warriorr.png"

    def getPosition(self):
        return self.positionX, self.positionY
    
    def get_sprite(self):
        return self.sprite
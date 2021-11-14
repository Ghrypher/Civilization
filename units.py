class Unit():

    def __init__(self):
        """Inicio de la clase, crea las variables de la misma"""
        self.life = None
        self.dmg = None
        self.visibility = None
        self.type = None
        self.team = None
        self.positionX = None
        self.positionY = None
        self.positionToMoveX = None
        self.positionToMoveY = None

    def __str__(self):
        return self.type

    def setPosition(self, posX, posY):
        """Asign the position of the unit"""
        self.positionX = posX
        self.positionY = posY

    def getPosition(self):
        return self.positionX, self.positionY
    
    def revealMap(self, map):
        """Reveal all the cells in range of the unit"""
        for x in range(self.positionX - self.visibility, self.positionX + self.visibility + 1):
            if x < 0:
                continue
            for y in range(self.positionY - self.visibility, self.positionY + self.visibility + 1):
                if y < 0:
                    continue
                try:
                    if ((x - self.positionX)**2 + (y - self.positionY)**2)**(1/2) <= self.visibility:
                        map[x][y].revealCell()
                except:
                    continue

class Warrior(Unit):
    
    def __init__(self):
        super().__init__()
        self.type = "WR"
        self.visibility = 3
        self.life = 5
        self.dmg = 3
        self.armor = 1

class Founder(Unit):

    def __init__(self):
        super().__init__()
        self.type = "FD"
        self.visibility = 4
        self.life = 4
        self.dmg = 1

class Worker(Unit):

    def __init__(self):
        super().__init__()
        self.type = "WK"
        self.visibility = 3
        self.life = 3
        self.dmg = 1
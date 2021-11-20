class Structures:
    """ Una calse Asentamientos donde estan todos los edificios"""

    def __init__(self):
        """ constructor de la clase """
        self.maxLife = None
        self.life = None
        self.type = ""
        self.x = None
        self.y = None
        self.visibility = None
    
    def __str__(self):
        return self.type
    
    def getRepaired(self):
        """Repairs the structure, healing it"""
        self.life += 3
        if self.maxLife < self.life:
            self.life = self.maxLife
    
    def getHealthData(self):
        return self.life, self.maxLife

    def setPosition(self, posX, posY):
        """Sets the coordinates of the city"""
        self.x = posX
        self.y = posY
    
    def getPosition(self):
        """Gets the position of the structure"""
        return self.x, self.y

    def revealMap(self, map):
        """Reveal all the cells in range of the unit"""
        for x in range(self.x - self.visibility, self.x + self.visibility + 1):
            if x < 0:
                continue
            for y in range(self.y - self.visibility, self.y + self.visibility + 1):
                if y < 0:
                    continue
                try:
                    if ((x - self.x)**2 + (y - self.y)**2)**(1/2) <= self.visibility:
                        map[x][y].revealCell()
                except:
                    continue

class City(Structures):

    def __init__(self):
        super().__init__()
        self.maxLife = 30
        self.life = 30
        self.type = "CT"
        self.production = []
        self.visibility = 6

    def reciveAttack(self, dmg):
        """Reduces the life of the unit based on the damage received"""
        self.life -= dmg


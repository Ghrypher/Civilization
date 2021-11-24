class Resources():

    def __init__(self):
        """The start of the class, all in here is created and executed"""
        self.gold = 200
        self.silver = 100
        self.wood = 200
        self.food = 50
        self.hungerTurns = 0
    
    def modifyGold(self, quantity):
        """Adds or remove gold"""
        self.gold += quantity
        if self.gold < 0:
            self.gold = 0
    
    def modifySilver(self, quantity):
        """Adds or remove silver"""
        self.silver += quantity
        if self.silver < 0:
            self.silver = 0
    
    def modifyWood(self, quantity):
        """Adds or remove wood"""
        self.wood += quantity
        if self.wood < 0:
            self.wood = 0
    
    def modifyFood(self, quantity):
        """Adds or remove food"""
        self.food += quantity
        if self.food < 0:
            self.food = 0
    
    def getGold(self):
        """Returns the gold quantity"""
        return self.gold
    
    def getSilver(self):
        """Returns the silver quantity"""
        return self.silver
    
    def getWood(self):
        """Returns the wood quantity"""
        return self.wood
    
    def getFood(self):
        """Returns the food quantity"""
        return self.food

    def getHunger(self):
        """Gets the number of turns with hunger"""
        return self.hungerTurns

    def addCounter(self):
        """Adds a countes to the quantity of turns without food"""
        self.hungerTurns += 1

    def removeCounters(self):
        """Removes all the counters of hunger"""
        self.hungerTurns = 0
        
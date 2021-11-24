class Unit():

    def __init__(self):
        """Inicio de la clase, crea las variables de la misma"""
        self.maxLife = None
        self.life = None
        self.dmg = None
        self.attackRange = None
        self.visibility = None
        self.maxMovement = None
        self.movement = self.maxMovement
        self.actionPosible = True
        self.resting = False
        self.armor = None
        self.type = None
        self.team = None
        self.goldCost = None
        self.silverCost = None
        self.foodCost = None
        self.timeCreation = None
        self.resources = None
        self.positionX = None
        self.positionY = None
        self.positionToMoveX = None
        self.positionToMoveY = None
        self.route = []

    def __str__(self):
        return self.type

    def setResources(self, resource):
        """Assigns the resources to the unit"""
        self.resources = resource

    def setPosition(self, posX, posY):
        """Asign the position of the unit"""
        self.positionX = posX
        self.positionY = posY

    def getPosition(self):
        return self.positionX, self.positionY
    
    def setRoute(self, route):
        """Sets the route made by the path finding algorithm"""
        self.route = route

    def getRoute(self):
        """Return the route of the unit"""
        return self.route

    def getPositionToMove(self):
        """Gets the position to move of the unit"""
        return self.positionToMoveX, self.positionToMoveY

    def setPostionToMove(self, posX, posY):
        """Sets the position to move in X and Y"""
        self.positionToMoveX = posX
        self.positionToMoveY = posY

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

    def reduceMovement(self):
        """Reduce the movement of the unit by 1"""
        self.movement -= 1

    def restartActions(self):
        """Sets the movement to the max posible"""
        self.movement = self.maxMovement
        self.actionPosible = True

    def getMovement(self):
        return self.movement

    def getHealthData(self):
        """Returns the health data"""
        return self.life, self.maxLife

    def setHealth(self, value):
        """Sets the health of the unit"""
        self.life = value

    def getActionPosible(self):
        """Returns if the unit can make an action"""
        return self.actionPosible

    def reciveAttack(self, dmg):
        """Reduces the life of the unit based on the damage received"""
        if dmg - self.armor >= 0:
            self.setHealth(self.life - (dmg - self.armor))

    def meleeAttack(self, unit):
        """Attacks melee an enemy unit"""
        self.actionPosible = False
        self.rest = False
        unit.reciveAttack(self.dmg)
        if unit.counterAttack() - self.armor >= 0:
            self.life -= unit.counterAttack() - self.armor
    
    def counterAttack(self):
        """Returns the damage of the unit"""
        return self.dmg

    def getAttackRange(self):
        """Returns the attack range of the unit"""
        return self.attackRange

    def setRest(self, value):
        """Sets that the unit is resting or not"""
        self.resting = value
    
    def unitResting(self):
        """Sets that the unit is resting"""
        self.actionPosible = False
        self.setRest(True)

    def healUnit(self):
        """Checks if the unit is resting and if so, heal it"""
        if self.resting and self.maxLife > self.life:
            self.life += 1

    def getCreationData(self):
        """Gets all the information for the creation of the unit"""
        return self.goldCost, self.silverCost, self.timeCreation, self.foodCost

    def consumeFood(self):
        """Reduces the food of the resources"""
        self.resources.modifyFood(-self.foodCost)

class Warrior(Unit):
    
    def __init__(self):
        super().__init__()
        self.type = "WR"
        self.visibility = 3
        self.maxMovement = 4
        self.maxLife = 5
        self.life = 5
        self.dmg = 4
        self.armor = 1
        self.attackRange = 1
        self.goldCost = 20
        self.silverCost = 10
        self.timeCreation = 3
        self.foodCost = 3

class Founder(Unit):

    def __init__(self):
        super().__init__()
        self.type = "FD"
        self.visibility = 4
        self.maxMovement = 2
        self.maxLife = 4
        self.life = 4
        self.dmg = 1
        self.armor = 0
        self.attackRange = 1
        self.goldCost = 50
        self.silverCost = 20
        self.timeCreation = 5
        self.foodCost = 1
        

class Worker(Unit):

    def __init__(self):
        super().__init__()
        self.type = "WK"
        self.visibility = 3
        self.maxMovement = 3
        self.maxLife = 3
        self.life = 3
        self.dmg = 0
        self.armor = 0
        self.goldCost = 10
        self.silverCost = 5
        self.timeCreation = 2
        self.foodCost = 1

class Archer(Unit):

    def __init__(self):
        super().__init__()
        self.type = "AR"
        self.visibility = 4
        self.maxMovement = 3
        self.maxLife = 4
        self.life = 4
        self.dmg = 3
        self.armor = 0
        self.attackRange = 3
        self.goldCost = 15
        self.silverCost = 5
        self.timeCreation = 3
        self.foodCost = 2

    def counterAttack(self):
        """Returns the damage of the unit"""
        return 0

    def rangeAttack(self, unit):
        """Attacks from distances other unit"""
        self.actionPosible = False
        self.rest = False
        unit.reciveAttack(self.dmg)

class Catapult(Unit):

    def __init__(self):
        super().__init__()
        self.type = "CP"
        self.visibility = 2
        self.maxMovement = 1
        self.maxLife = 4
        self.life = 4
        self.dmg = 3
        self.armor = 0
        self.attackRange = 6
        self.goldCost = 30
        self.silverCost = 15
        self.timeCreation = 5
        self.foodCost = 4
    
    def counterAttack(self):
        """Returns the damage of the unit"""
        return 0

    def rangeAttack(self, unit):
        """Attacks from distances other unit"""
        self.actionPosible = False
        self.rest = False
        unit.reciveAttack(self.dmg)

class Explorer(Unit):

    def __init__(self):
        super().__init__()
        self.type = "EX"
        self.visibility = 6
        self.maxMovement = 6
        self.maxLife = 2
        self.life = 2
        self.dmg = 1
        self.armor = 0
        self.attackRange = 1
        self.goldCost = 10
        self.silverCost = 0
        self.timeCreation = 1
        self.foodCost = 2
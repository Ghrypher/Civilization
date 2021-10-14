class Character():

    """Function __init__"""
    def __init__(self):
        self.life = None
        self.team = None
        self.positionx = None
        self.positiony = None
        self.type : str
        self.ability : str
        self.attack : int
        self.defense : int
        self.speed : int
        self.resources : int

    """Function setPosition, establishes the position from the character"""
    def setPosition(self,posx,posy):
        self.positionx = posx
        self.positiony = posy

    """Function getPosition, returns the position from the character"""
    def getPosition(self):
        return self.positionx,self.positiony

    """Function speedDefining, establishes the speed from the character basing on the type of character and the ability from his empire"""
    def speedDefining(self):
        pass

    """Function attackDefining, establishes the attack from the character basing on the type of character and the ability from his empire"""
    def attackDefining(self):
        pass

    """Function defenseDefining, establishes the defense from the character basing on the type of character and the ability from his empire"""
    def defenseDefining(self):
        pass

    """Function resourcesDefining, establishes the resources that the character need basing on the type of character and the ability from his empire"""
    def resourcesDefining(self):
        pass

    """Function spriteSelect, establishes the sprite from the character basing on the type of character"""
    def spriteSelect(self):
        pass


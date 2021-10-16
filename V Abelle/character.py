class Character():

    def __init__(self):
        """Function __init__"""
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

    def setPosition(self,posx,posy):
        """Function setPosition, establishes the position from the character"""
        self.positionx = posx
        self.positiony = posy

    def getPosition(self):
        """Function getPosition, returns the position from the character"""
        return self.positionx,self.positiony

    def speedDefining(self):
        """Function speedDefining, establishes the speed from the character basing on the type of character and the ability from his empire"""
        pass

    def attackDefining(self):
        """Function attackDefining, establishes the attack from the character basing on the type of character and the ability from his empire"""
        pass

    def defenseDefining(self):
        """Function defenseDefining, establishes the defense from the character basing on the type of character and the ability from his empire"""
        pass

    def resourcesDefining(self):
        """Function resourcesDefining, establishes the resources that the character need basing on the type of character and the ability from his empire"""
        pass

    def spriteSelect(self):
        """Function spriteSelect, establishes the sprite from the character basing on the type of character"""
        pass


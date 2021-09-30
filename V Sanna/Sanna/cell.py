class Cell():

    def __init__(self):
        self.troop = None
        self.biome = None
        self.visible = False
    
    def setBiome(self, biome):
        self.biome = biome
    
    def readBiome(self):
        return self.biome
    
    def hideCell(self):
        self.visible = False
    
    def showCell(self):
        self.visible = True
    
    def getVisibility(self):
        return self.visible
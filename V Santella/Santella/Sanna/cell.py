class Cell():

    def __init__(self):
        self.troop = None
        self.biome = None
    
    def setBiome(self, biome):
        self.biome = biome
    
    def readBiome(self):
        return self.biome
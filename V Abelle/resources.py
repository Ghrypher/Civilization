class Resources():

    def __init__(self):
        """Function __init__"""
        self.type : str
        self.resourcetype = []
        self.chargeDatatoGame()

    def chargeDatatoGame(self):
        """Function chargeDatatoGame"""
        with open('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/data/resourcestypes.txt') as txt:
            self.resourcetype = txt.read()
            txt.close()
            print (self.resourcetype)


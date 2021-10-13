class Resources():

    """Function __init__"""
    def __init__(self):
        self.type : str
        self.resourcetype = []
        self.chargeDatatoGame()

    """Function chargeDatatoGame"""
    def chargeDatatoGame(self):
        with open('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/data/resourcestypes.txt') as txt:
            self.resourcetype = txt.read()
            txt.close()
            print (self.resourcetype)


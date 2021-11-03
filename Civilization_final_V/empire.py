from os import close
from gamemain import GameMain

class Empire():

    def __init__(self):
        """Function __init__"""
        self.name : str
        self.ability : str
        self.empireName = []
        self.empiReability = []
        self.chargeDatatoGame()

    def chargeDatatoGame(self):
        """Function chargeDatatoGame, reads the txt file that has the information from the empire"""
        with open('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/data/empiresnames.txt') as txt:
            self.empireName = txt.read()
            txt.close()
            print (self.empireName)
        with open('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/data/empiresabilities.txt') as txt:
            self.empireability = txt.read()
            txt.close()
            print (self.empiReability)


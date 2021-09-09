from os import close
from gamemain import GameMain

class Empire():

    '''Function __init__'''
    def __init__(self):
        self.name : str
        self.ability : str
        self.empirename = []
        self.empireability = []
        self.chargeDatatoGame()

    '''Function chargeDatatoGame, reads the txt file that has the information from the empire'''
    def chargeDatatoGame(self):
        with open('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/data/empiresnames.txt') as txt:
            self.empirename = txt.read()
            txt.close()
            print (self.empirename)
        with open('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/data/empiresabilities.txt') as txt:
            self.empireability = txt.read()
            txt.close()
            print (self.empireability)

if __name__ == "__main__":
    empiretry = Empire()
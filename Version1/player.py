class Player():

    '''Function __init__'''
    def __init__(self,name):
        self.name = name
        self.empire = 'Santiaguense'
        self.playerDataSaving()

    '''Function playerDataSaving, writes in a txt file the information from the player'''
    def playerDataSaving(self):
        with open('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/data/playerdata.txt','r+') as txt:
            txt.truncate(0)
            txt.close()
        with open('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/data/playerdata.txt','w') as txt:
            txt.writelines(self.name)
            txt.writelines('\n')
            txt.writelines(self.empire)
            txt.close()

if __name__ == '__main__':
    playertry = Player('Santi')
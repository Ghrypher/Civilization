class Player():

    def __init__(self,name,empire):
        """Function __init__"""
        self.name = name
        self.empire = empire
        self.playerDataSaving()

    def playerDataSaving(self):
        """Function playerDataSaving, writes in a txt file the information from the player and deletes the old data"""
        with open('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/data/playerdata.txt','r+') as txt:
            txt.truncate(0)
            txt.close()
        with open('C:/Users/santi/OneDrive/Escritorio/Santiago/Prog. Or. Obj/T-H-E/Civilization/Version1/data/playerdata.txt','w') as txt:
            txt.writelines(self.name)
            txt.writelines('\n')
            txt.writelines(self.empire)
            txt.close()


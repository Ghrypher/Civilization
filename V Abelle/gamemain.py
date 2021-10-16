"""Libraries"""
import random, sys, copy, os, time
from gameview import GameView
from gameboard import GameBoard
from character import Character

class GameMain():

    def __init__(self):
        """Function __init__"""
        self.playing = True #Establishes if a function is running or not
        self.cameraspeed = 5 #Establishes the speed from the camera
        self.tilesize = 32 #Establishes the size from the tiles
        self.character_pos_x = 576 #Establishes the position in x from the character
        self.character_pos_y = 320 #Establishes the position in y from the character
        self.max_cam_move_X = int #Establishes the max position the camera can move on the x axis
        self.max_cam_move_Y = int #Establishes the max position the camera can move on the y axis
        self.width = 70
        self.height = 40
        self.non_reachables = [] #List from non reachable cells
        self.non_reachables_load = []
        self.M_Obj = None
        self.Unit = None
        self.gameview = GameView()
        self.gameviewreturned = None
        """Loads"""
        self.loadingBarProgress(1)
        #createBoard and readMap
        self.character = None
        self.menuLoop() #Starts the program from the menuLoop function

    def loadingBarProgress(self,mode):
        """Function loadingBarProgress, establishes the progress from the loading bar"""
        self.gameview.loadBarView(mode)

    def menuLoop(self):
        """Function menuLoop, is the menu loop"""
        """First Draw Call"""
        self.gameview.menuFirstDraw()

        """Menu View Loop"""
        selectedmenu = self.gameview.menuView()

        if selectedmenu == 'exit':
            self.exitUI('menu')
        elif selectedmenu == 'map':
            self.gameMapSelector()
        elif selectedmenu == 'crets':
            self.creditsOpen()
        elif selectedmenu == 'insts':
            self.instructionsOpen()

    def workInProgress(self,mode):        
        """Function workInProgress, is a temporaly function which says that this part of the code is not finished yet"""
        self.gameview.workInProgressFirstDraw()
        
        self.gameviewreturned = self.gameview.workInProgressView()

        if self.gameviewreturned == 'exit':
            self.exitUI('work')
        else:
            if mode == 'random' or mode == 'pre':
                self.gameMapSelector()
            else:
                self.menuLoop()

    def exitUI(self,gamemode):
        """Function exitUI, ask if you want to exit"""
        self.gameview.exitUIFirstDraw()

        self.gameviewreturned = self.gameview.exitUIView(gamemode)

        if self.gameviewreturned == 'random':
            self.workInProgress('random') #self.randomMapMode(True)
        elif self.gameviewreturned == 'created':
            self.workInProgress('pre') #self.preCreatedMapMode(True)
        elif self.gameviewreturned == 'work':
            self.workInProgress('work')
        elif self.gameviewreturned == 'menu':
            self.menuLoop()
        elif self.gameviewreturned == 'credits':
            self.creditsOpen()
        elif self.gameviewreturned == 'insts':
            self.instructionsOpen()
        elif self.gameviewreturned == 'mode':
            self.gameMapSelector(True)

    def creditsOpen(self):
        """Function creditsOpen, put the credits on screen"""
        self.gameview.creditsFirstDraw()

        returnedvalue = ''

        returnedvalue = self.gameview.creditsView()

        if returnedvalue == 'exit':
            self.exitUI('credits')
        else:
            self.menuLoop()

    def instructionsOpen(self):
        """Function instructionsOpen, put the instructions on screen"""
        self.gameview.instructionsFirstDraw()

        returnedvalue = ''
        
        returnedvalue = self.gameview.instructionsView()

        if returnedvalue == 'exit':
            self.exitUI('insts')
        else:
            self.menuLoop()
        
    def gameMapSelector(self):
        """Function gameMapSelector, is the game map selector"""
        self.loadingBarProgress(2)

        self.gameview.mapSelectorFirstDraw()
        
        returnedvalue = ''

        returnedvalue = self.gameview.mapSeclectorView()
        print(returnedvalue)

        if returnedvalue == 'random':
            self.non_reachables = []
            self.workInProgress('random') #self.randomGameMode()
        elif returnedvalue == 'pre':
            self.non_reachables = []
            self.M_Obj = None #self.readMap("resources/maps/map1.txt")
            self.workInProgress('pre') #self.preCreatedGameMode()
        elif returnedvalue == 'exit':
            self.exitUI('mode')
        else:
            self.menuLoop()

"""Main"""
if __name__ == '__main__':
    startingame = GameMain()
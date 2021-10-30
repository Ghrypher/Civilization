"""Libraries"""
import random, sys, copy, os, time
from gameboard import GameBoard
from character import Character
from systemcontroller import SystemController

class GameMain():

    def __init__(self):
        """Function __init__"""
        self.syscon = SystemController()
        self.playing = True #Establishes if a function is running or not
        self.sysconreturned = None
        """Loads"""
        self.loadingBarProgress(1)
        #createBoard and readMap
        self.menuLoop() #Starts the program from the menuLoop function

    def loadingBarProgress(self,mode):
        """Function loadingBarProgress, establishes the progress from the loading bar"""
        self.syscon.progressBar(mode)

    def menuLoop(self):
        selectedmenu = self.syscon.menuLoop()

        if selectedmenu == 'exit':
            self.exitUI('menu')
        elif selectedmenu == 'map':
            self.gameMapSelector()
        elif selectedmenu == 'crets':
            self.creditsOpen()
        elif selectedmenu == 'insts':
            self.instructionsOpen()

    def workInProgress(self,mode):        
        self.sysconreturned = self.syscon.workInProgress()

        if self.sysconreturned == 'exit':
            self.exitUI('work')
        else:
            if mode == 'random' or mode == 'pre':
                self.gameMapSelector()
            else:
                self.menuLoop()

    def exitUI(self,gamemode):
        self.sysconreturned = self.syscon.exitUI(gamemode)

        if self.sysconreturned == 'random':
            self.workInProgress('random') #self.randomMapMode(True)
        elif self.sysconreturned == 'created':
            self.workInProgress('pre') #self.preCreatedMapMode(True)
        elif self.sysconreturned == 'work':
            self.workInProgress('work')
        elif self.sysconreturned == 'menu':
            self.menuLoop()
        elif self.sysconreturned == 'credits':
            self.creditsOpen()
        elif self.sysconreturned == 'insts':
            self.instructionsOpen()
        elif self.sysconreturned == 'mode':
            self.gameMapSelector()

    def creditsOpen(self):
        """Function creditsOpen, put the credits on screen"""
        returnedvalue = self.syscon.credits()

        if returnedvalue == 'exit':
            self.exitUI('credits')
        else:
            self.menuLoop()

    def instructionsOpen(self):
        returnedvalue = self.syscon.instructions()

        if returnedvalue == 'exit':
            self.exitUI('insts')
        else:
            self.menuLoop()
        
    def gameMapSelector(self):
        """Function gameMapSelector, is the game map selector"""
        self.loadingBarProgress(2)

        returnedvalue = self.syscon.gameMapSelector()

        if returnedvalue == 'random':
            self.non_reachables = []
            self.gameMain()
        elif returnedvalue == 'pre':
            self.non_reachables = []
            self.M_Obj = None
            self.gameMain()
        elif returnedvalue == 'exit':
            self.exitUI('mode')
        else:
            self.menuLoop()

    def gameMain(self):
        """Function gameMain, is the game main"""
        returnedvalue = self.syscon.gameLoop()

        if returnedvalue == 'exit':
            self.gameMapSelector()

"""Main"""
if __name__ == '__main__':
    startingame = GameMain()
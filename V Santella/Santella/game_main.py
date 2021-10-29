"""Libraries"""
import random, sys, copy, os, time
from game_view import GameView
from tablero import Tablero
from units import Unit

class GameMain():
    """"""
    def __init__(self):
        """Function __init__"""
        self.gameview = GameView()
        self.menu_loop()
    
    def menu_loop(self):
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
    

"""Main"""
if __name__ == '__main__':
    startingame = GameMain()
        
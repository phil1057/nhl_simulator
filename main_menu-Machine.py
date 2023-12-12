#!/usr/bin/python3
import pathlib
import pygubu
import tkinter as tk
from pygame import mixer
from game import *
from quick_game import *

#mixer.init()
#mixer.music.load("la_soiree_du_hockey_loop.mp3")

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "gui/main_menu.ui"


class MainMenu:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("root", master)
        builder.connect_callbacks(self)

    def run(self):
        #mixer.music.play()
        self.mainwindow.mainloop()

    def Quick_Game(self):
        self.mainwindow.grab_set()
        mainRoot = self.mainwindow.Element.get("root")
        mainRoot.
        quick_game = QuickGame()
        quick_game.run()

if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.run()
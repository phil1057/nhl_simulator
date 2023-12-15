from playsound import playsound
from game import *
from quick_game import *
from main_menu import *
import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer
from pygubu.widgets.scrolledframe import ScrolledFrame
from PIL import Image, ImageTk
from db import Database

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Create a container to hold different pages
        self.root = tk.Frame(self)
        self.root.grid(row=0, column=0, sticky="nsew")

        # Icone et titre
        self.title("NHL Simulator")
        self.img_tinynhllogo = tk.PhotoImage(file="img/main_menu/tiny-nhl-logo.png")
        self.iconphoto(True, self.img_tinynhllogo)

        # Musique 
        mixer.init()
        mixer.music.load("la_soiree_du_hockey_loop.mp3")

        # Librairie des pages
        self.pages = {}

        # Ajoute les pages dans la librairie
        for PageClass in (MainMenu, QuickGame, Game):
            page = PageClass(self.root, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        initial_variable = "Initial information"
        self.show_page(MainMenu, initial_variable)

    def show_page(self, page_to_show, info=None):
        page = self.pages[page_to_show]
        page.tkraise()
        if hasattr(page, "receive_info"):
            page.receive_info(info)

if __name__ == "__main__":
    game = Main()
    game.mainloop()

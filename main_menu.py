#!/usr/bin/python3
import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer
from quick_game import *


class MainMenu(tk.Frame): 
    def __init__(self, parent, controller):
        # build ui
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.frame_background = ttk.Frame(self)
        self.frame_background.configure(height=720, width=1290)
        self.background_image = ttk.Label(self.frame_background)
        self.img_3 = tk.PhotoImage(file="img/main_menu/3.png")
        self.background_image.configure(image=self.img_3, width=1280)
        self.background_image.pack()
        self.frame_background.grid(column=0, row=0)
        self.warning_frame = ttk.Frame(self)
        self.warning_frame.configure(height=200, width=200)
        self.warning_label = ttk.Label(self.warning_frame)
        self.warning_label.configure(
            background="#040404",
            font="{@Arial Unicode MS} 11 {}",
            foreground="#ffffff",
            text='The logos of the National Hockey League and the names of the National \nHockey League Players\' Association do not belong to the Cégep de la \nGaspésie et les Îles. Distribution outside of the course "420-CS5-GA \nSimulations Appliquées" is therefore prohibited and illegal.\n\nLes logos de la Ligue Nationale de Hockey et les noms de l\'Association \ndes joueurs de la Ligue Nationale de Hockey n\'appartiennent pas au \nCégep de la Gaspésie et les Îles. La distribution en dehors du \ncours "420-CS5-GA Simulations Appliquées" est donc interdite et illégale.')
        self.warning_label.pack(side="top")
        self.warning_frame.grid(column=0, padx=50, pady=50, row=0, sticky="sw")
        self.quick_game_button = tk.Button(self)
        self.quick_game_button.configure(
            font="{Yu Gothic UI} 12 {}",
            text='Match Immédiat',
            width=17)
        self.quick_game_button.grid(
            column=0,
            ipadx=100,
            ipady=15,
            padx=100,
            pady=200,
            row=0,
            sticky="se")
        self.quick_game_button.configure(command=self.GoToQuickGame)
        self.info_button = tk.Button(self)
        self.info_button.configure(
            font="{Yu Gothic UI} 12 {}",
            text='Afficher les équipes/joueurs',
            width=17)
        self.info_button.grid(
            column=0,
            ipadx=100,
            ipady=15,
            padx=100,
            pady=100,
            row=0,
            sticky="se")
        self.info_button.configure(command=self.GoToInfo)
        self.nhl_logo_label = tk.Label(self)
        self.img_iconnhllogo = tk.PhotoImage(file="img/main_menu/icon-nhl-logo.png")
        self.nhl_logo_label.configure(
            background="#000000",
            borderwidth=0,
            disabledforeground="#400040",
            image=self.img_iconnhllogo,
            text='label1')
        self.nhl_logo_label.grid(
            column=0, padx=150, pady=50, row=0, sticky="ne")

    def GoToQuickGame(self):
        self.controller.show_page(QuickGame)

    def GoToInfo(self):
        pass
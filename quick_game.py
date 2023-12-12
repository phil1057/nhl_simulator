#!/usr/bin/python3
import pathlib
import pygubu
import time
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from db import Database
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "gui/quick_game.ui"


class QuickGame:
    def __init__(self, master=None):

        db = Database()

        self.root = tk.Tk() if master is None else tk.Toplevel(master)

        db.cursor.execute("SELECT * FROM equipes")
        global equipes
        equipes = db.cursor.fetchall()

        global selected_home_team
        global selected_away_team
        global img_away_logo
        global img_home_logo

        selected_home_team = 1
        selected_away_team = 2
        self.img_away_logo = ImageTk.PhotoImage(file="img/team_logos/"+str(selected_away_team)+".png")
        self.img_home_logo = ImageTk.PhotoImage(file="img/team_logos/"+str(selected_home_team)+".png")

        home_team_name = tk.StringVar()
        home_team_city = tk.StringVar()
        away_team_name = tk.StringVar()
        away_team_city = tk.StringVar()

        home_team_name.set("Bruins")
        home_team_city.set("Boston")

        away_team_name.set("Red Wings")
        away_team_city.set("Detroit")

        def ChangeHomeTeamUp():
            global selected_home_team

            selected_home_team += 1
            if selected_home_team == 8:
                selected_home_team = 1

            home_team_city.set(equipes[selected_home_team][2])
            home_team_name.set(equipes[selected_home_team][1])

            self.img_home_logo = ImageTk.PhotoImage(file="img/team_logos/"+str(equipes[selected_home_team][0])+".png")
            self.logo_home.config(image=self.img_home_logo)
            

        def ChangeHomeTeamDown():
            global selected_home_team

            selected_home_team -= 1
            if selected_home_team == 0:
                selected_home_team = 7

            home_team_city.set(equipes[selected_home_team][2])
            home_team_name.set(equipes[selected_home_team][1])

            self.img_home_logo = ImageTk.PhotoImage(file="img/team_logos/"+str(equipes[selected_home_team][0])+".png")
            self.logo_home.config(image=self.img_home_logo)

        def ChangeAwayTeamUp():
            global selected_away_team
            

            selected_away_team += 1
            if selected_away_team == 8:
                selected_away_team = 1
            
            away_team_city.set(equipes[selected_away_team][2])
            away_team_name.set(equipes[selected_away_team][1])

            self.img_away_logo = ImageTk.PhotoImage(file="img/team_logos/"+str(equipes[selected_away_team][0])+".png")
            self.logo_away.config(image=self.img_away_logo)

        def ChangeAwayTeamDown():
            global selected_away_team

            selected_away_team -= 1
            if selected_away_team == 0:
                selected_away_team = 7
            
            away_team_city.set(equipes[selected_away_team][2])
            away_team_name.set(equipes[selected_away_team][1])
            
            self.img_away_logo = ImageTk.PhotoImage(file="img/team_logos/"+str(equipes[selected_away_team][0])+".png")
            self.logo_away.config(image=self.img_away_logo)


        def StartGame():
            away_team = equipes[selected_away_team]
            home_team = equipes[selected_home_team]

        self.img_tinynhllogo = ImageTk.PhotoImage(file="img/main_menu/tiny-nhl-logo.png")
        self.root.configure(height=720, width=1280)
        self.root.iconphoto(True, self.img_tinynhllogo)
        self.root.resizable(False, False)
        self.root.title("NHL Simulator")
        self.awayside_frame = ttk.Frame(self.root)
        self.awayside_frame.configure(height=720, width=426)
        self.separateur_away = ttk.Separator(self.awayside_frame)
        self.separateur_away.configure(orient="horizontal", takefocus=False)
        self.separateur_away.pack(
            expand="false",
            fill="both",
            pady=40,
            side="top")
        self.city_away = tk.Label(self.awayside_frame)
        self.city_away.configure(
            font="{Microsoft YaHei} 20 {}",
            textvariable=away_team_city)
        self.city_away.pack(side="top")
        self.name_away = tk.Label(self.awayside_frame)
        self.name_away.configure(
            font="{Microsoft YaHei} 20 {bold}",
            textvariable=away_team_name)
        self.name_away.pack(side="top")
        self.logo_away = tk.Label(self.awayside_frame)
        self.logo_away.configure(image=self.img_away_logo, text='label5')
        self.logo_away.pack(pady=50, side="top")
        self.team_ratings_away = ttk.Labelframe(self.awayside_frame)
        self.team_ratings_away.configure(
            height=200, text='Équipe visiteure', width=426)
        self.notebook_away = ttk.Notebook(self.team_ratings_away)
        self.notebook_away.configure(height=200, width=425)
        self.team_ratings_away_frame = ttk.Frame(self.notebook_away)
        self.team_ratings_away_frame.configure(height=200, width=200)
        self.forwards_label_away = tk.Label(self.team_ratings_away_frame)
        self.forwards_label_away.configure(
            font="{Yu Gothic UI Semilight} 12 {}", text='Attaque')
        self.forwards_label_away.grid(column=0, padx=100, pady=3, row=0)
        self.defense_label_away = tk.Label(self.team_ratings_away_frame)
        self.defense_label_away.configure(
            font="{Yu Gothic UI Semilight} 12 {}", text='Défense')
        self.defense_label_away.grid(column=0, pady=3, row=1)
        self.total_label_away = tk.Label(self.team_ratings_away_frame)
        self.total_label_away.configure(
            font="{Yu Gothic UI Semilight} 12 {}", text='Total')
        self.total_label_away.grid(column=0, pady=3, row=2)
        self.forwards_rating_away = tk.Label(self.team_ratings_away_frame)
        self.forwards_rating_away.configure(
            font="{Yu Gothic UI Semibold} 12 {}", text='90')
        self.forwards_rating_away.grid(column=1, row=0)
        self.defense_rating_away = tk.Label(self.team_ratings_away_frame)
        self.defense_rating_away.configure(
            font="{Yu Gothic UI Semibold} 12 {}", text='90')
        self.defense_rating_away.grid(column=1, row=1)
        self.total_rating_away = tk.Label(self.team_ratings_away_frame)
        self.total_rating_away.configure(
            font="{Yu Gothic UI Semibold} 12 {}", text='90')
        self.total_rating_away.grid(column=1, row=2)
        self.team_ratings_away_frame.pack(side="top")
        self.notebook_away.add(
            self.team_ratings_away_frame,
            state="normal",
            text='Groupe')
        self.player_ratings_away_frame = ttk.Frame(self.notebook_away)
        self.player_ratings_away_frame.configure(height=200, width=200)
        self.best_player_away = tk.Label(self.player_ratings_away_frame)
        self.best_player_away.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            text='Premier joueur')
        self.best_player_away.grid(column=0, padx=100, pady=3, row=0)
        self.second_player_away = tk.Label(self.player_ratings_away_frame)
        self.second_player_away.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            text='Deuxième Joueur')
        self.second_player_away.grid(column=0, pady=3, row=1)
        self.third_player_away = tk.Label(self.player_ratings_away_frame)
        self.third_player_away.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            text='Troisième Joueur')
        self.third_player_away.grid(column=0, pady=3, row=2)
        self.best_player_rating_away = tk.Label(
            self.player_ratings_away_frame)
        self.best_player_rating_away.configure(
            font="{Yu Gothic UI Semibold} 12 {}", text='90')
        self.best_player_rating_away.grid(column=1, row=0)
        self.second_player_rating_away = tk.Label(
            self.player_ratings_away_frame)
        self.second_player_rating_away.configure(
            font="{Yu Gothic UI Semibold} 12 {}", text='90')
        self.second_player_rating_away.grid(column=1, row=1)
        self.third_player_rating_away = tk.Label(
            self.player_ratings_away_frame)
        self.third_player_rating_away.configure(
            font="{Yu Gothic UI Semibold} 12 {}", text='90')
        self.third_player_rating_away.grid(column=1, row=2)
        self.player_ratings_away_frame.pack(side="top")
        self.notebook_away.add(self.player_ratings_away_frame, text='Joueurs')
        self.notebook_away.pack(side="top")
        self.team_ratings_away.pack(side="top")
        self.team_ratings_away.pack_propagate(0)
        self.awayside_frame.grid(column=0, row=0)
        self.awayside_frame.pack_propagate(0)
        self.center_frame = ttk.Frame(self.root)
        self.center_frame.configure(height=720, width=427)
        self.choix_des_equipes_label = tk.Label(self.center_frame)
        self.choix_des_equipes_label.configure(
            font="{Yu Gothic UI Semibold} 24 {}",
            text='Choix des équipes')
        self.choix_des_equipes_label.grid(column=1, row=1)
        self.page_description_label = tk.Label(self.center_frame)
        self.page_description_label.configure(
            font="{Yu Gothic UI Semilight} 14 {}",
            justify="center",
            text='En sélectionnant une option.\nLe match va débuter.')
        self.page_description_label.grid(column=1, row=2)
        self.both_teams_button = ttk.Button(self.center_frame)
        self.img_both_sides = ImageTk.PhotoImage(file="img/arrows/both_sides.png")
        self.both_teams_button.configure(
            image=self.img_both_sides,
            style="Toolbutton",
            text='button1',
            command=StartGame)
        self.both_teams_button.grid(column=1, row=3)
        self.away_team_button = ttk.Button(self.center_frame)
        self.img_left = ImageTk.PhotoImage(file="img/arrows/left.png")
        self.away_team_button.configure(
            image=self.img_left,
            style="Toolbutton",
            text='button2')
        self.away_team_button.grid(column=0, ipadx=9, row=3)
        self.home_team_button = ttk.Button(self.center_frame)
        self.img_right = ImageTk.PhotoImage(file="img/arrows/right.png")
        self.home_team_button.configure(
            image=self.img_right,
            style="Toolbutton",
            text='button3')
        self.home_team_button.grid(column=2, padx=30, row=3, sticky="e")
        self.none_button = ttk.Button(self.center_frame)
        self.img_none = ImageTk.PhotoImage(file="img/arrows/none.png")
        self.none_button.configure(image=self.img_none, style="Toolbutton")
        self.none_button.grid(column=1, pady=30, row=4)
        self.up_away_button = ttk.Button(self.center_frame)
        self.img_up = ImageTk.PhotoImage(file="img/arrows/up.png")
        self.up_away_button.configure(
            command = ChangeAwayTeamUp,
            image=self.img_up,
            style="Toolbutton",
            text='button5')
        self.up_away_button.grid(column=0, row=5)
        self.down_away_buttton = ttk.Button(self.center_frame)
        self.img_down = ImageTk.PhotoImage(file="img/arrows/down.png")
        self.down_away_buttton.configure(
            image=self.img_down,
            style="Toolbutton",
            text='button5',
            command=ChangeAwayTeamDown)
        self.down_away_buttton.grid(column=0, row=7)
        self.up_home_button = ttk.Button(self.center_frame)
        self.up_home_button.configure(
            image=self.img_up,
            style="Toolbutton",
            text='button5',
            command=ChangeHomeTeamUp)
        self.up_home_button.grid(column=2, row=5)
        self.down_home_button = ttk.Button(self.center_frame)
        self.down_home_button.configure(
            image=self.img_down,
            style="Toolbutton",
            text='button5',
            command=ChangeHomeTeamDown)
        self.down_home_button.grid(column=2, row=7)
        self.parcourir_equipes_label = tk.Label(self.center_frame)
        self.parcourir_equipes_label.configure(
            font="{Yu Gothic UI Semibold} 18 {}",
            text='Parcourir les équipes')
        self.parcourir_equipes_label.grid(column=1, row=6)
        self.nhl_logo = tk.Label(self.center_frame)
        self.nhl_logo.configure(image=self.img_tinynhllogo, text='label1')
        self.nhl_logo.grid(column=1, pady=20, row=0)
        self.central_separator = ttk.Separator(self.center_frame)
        self.central_separator.configure(
            cursor="no", orient="horizontal", takefocus=False)
        self.central_separator.grid(
            column=1, ipadx=100, pady=15, row=4, sticky="s")
        self.center_frame.grid(column=1, row=0)
        self.center_frame.grid_propagate(0)
        self.homeside_frame = ttk.Frame(self.root)
        self.homeside_frame.configure(height=720, width=426)
        self.separateur_home = ttk.Separator(self.homeside_frame)
        self.separateur_home.configure(orient="horizontal", takefocus=False)
        self.separateur_home.pack(
            expand="false",
            fill="both",
            pady=40,
            side="top")
        self.city_home = tk.Label(self.homeside_frame)
        self.city_home.configure(
            font="{Microsoft YaHei} 20 {}",
            textvariable=home_team_city)
        self.city_home.pack(side="top")
        self.name_home = tk.Label(self.homeside_frame)
        self.name_home.configure(
            font="{Microsoft YaHei} 20 {bold}",
            textvariable=home_team_name)
        self.name_home.pack(side="top")
        self.logo_home = tk.Label(self.homeside_frame)
        self.img_logo_home = ImageTk.PhotoImage(file="img/team_logos/1.png")
        self.logo_home.configure(image=self.img_logo_home, text='label5')
        self.logo_home.pack(pady=50, side="top")
        self.team_ratings_home = ttk.Labelframe(self.homeside_frame)
        self.team_ratings_home.configure(
            height=200,
            labelanchor="ne",
            text='Équipe à domicile',
            width=426)
        self.notebook_home = ttk.Notebook(self.team_ratings_home)
        self.notebook_home.configure(height=200, width=425)
        self.team_ratings_home_frame = ttk.Frame(self.notebook_home)
        self.team_ratings_home_frame.configure(height=200, width=200)
        self.forwards_label_home = tk.Label(self.team_ratings_home_frame)
        self.forwards_label_home.configure(
            font="{Yu Gothic UI Semilight} 12 {}", text='Attaque')
        self.forwards_label_home.grid(column=0, padx=100, pady=3, row=0)
        self.defense_label_home = tk.Label(self.team_ratings_home_frame)
        self.defense_label_home.configure(
            font="{Yu Gothic UI Semilight} 12 {}", text='Défense')
        self.defense_label_home.grid(column=0, pady=3, row=1)
        self.total_label_home = tk.Label(self.team_ratings_home_frame)
        self.total_label_home.configure(
            font="{Yu Gothic UI Semilight} 12 {}", text='Total')
        self.total_label_home.grid(column=0, pady=3, row=2)
        self.forwards_rating_home = tk.Label(self.team_ratings_home_frame)
        self.forwards_rating_home.configure(
            font="{Yu Gothic UI Semibold} 12 {}", text='90')
        self.forwards_rating_home.grid(column=1, row=0)
        self.defense_rating_home = tk.Label(self.team_ratings_home_frame)
        self.defense_rating_home.configure(
            font="{Yu Gothic UI Semibold} 12 {}", text='90')
        self.defense_rating_home.grid(column=1, row=1)
        self.total_rating_home = tk.Label(self.team_ratings_home_frame)
        self.total_rating_home.configure(
            font="{Yu Gothic UI Semibold} 12 {}", text='90')
        self.total_rating_home.grid(column=1, row=2)
        self.team_ratings_home_frame.pack(side="top")
        self.notebook_home.add(
            self.team_ratings_home_frame,
            state="normal",
            text='Groupe')
        self.player_ratings_home_frame = ttk.Frame(self.notebook_home)
        self.player_ratings_home_frame.configure(height=200, width=200)
        self.best_player_home = tk.Label(self.player_ratings_home_frame)
        self.best_player_home.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            text='Premier joueur')
        self.best_player_home.grid(column=0, padx=100, pady=3, row=0)
        self.second_player_home = tk.Label(self.player_ratings_home_frame)
        self.second_player_home.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            text='Deuxième Joueur')
        self.second_player_home.grid(column=0, pady=3, row=1)
        self.third_player_home = tk.Label(self.player_ratings_home_frame)
        self.third_player_home.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            text='Troisième Joueur')
        self.third_player_home.grid(column=0, pady=3, row=2)
        self.best_player_rating_home = tk.Label(
            self.player_ratings_home_frame)
        self.best_player_rating_home.configure(
            font="{Yu Gothic UI Semibold} 12 {}", text='90')
        self.best_player_rating_home.grid(column=1, row=0)
        self.second_player_rating_home = tk.Label(
            self.player_ratings_home_frame)
        self.second_player_rating_home.configure(
            font="{Yu Gothic UI Semibold} 12 {}", text='90')
        self.second_player_rating_home.grid(column=1, row=1)
        self.third_player_rating_home = tk.Label(
            self.player_ratings_home_frame)
        self.third_player_rating_home.configure(
            font="{Yu Gothic UI Semibold} 12 {}", text='90')
        self.third_player_rating_home.grid(column=1, row=2)
        self.player_ratings_home_frame.pack(side="top")
        self.notebook_home.add(
            self.player_ratings_home_frame,
            text='Joueurs')
        self.notebook_home.pack(side="top")
        self.team_ratings_home.pack(side="top")
        self.team_ratings_home.pack_propagate(0)
        self.homeside_frame.grid(column=2, row=0)
        self.homeside_frame.pack_propagate(0)
        self.root.grid_propagate(0)

        self.mainwindow = self.root

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = QuickGame()
    app.run()


#!/usr/bin/python3
import pathlib
import pygubu
import time
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from db import Database
import random
from game import *


class QuickGame(tk.Frame):
    def __init__(self, parent, controller):
        # build ui
        tk.Frame.__init__(self, parent)
        self.controller = controller

        db = Database()

        db.cursor.execute("SELECT * FROM equipes")
        global equipes
        equipes = db.cursor.fetchall()

        global logo_home

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

        global home_coach_name_text; home_coach_name_text = tk.StringVar()
        global home_arena_text; home_arena_text = tk.StringVar()
        global home_capacity_text; home_capacity_text = tk.StringVar()

        global away_coach_name_text; away_coach_name_text = tk.StringVar()
        global away_arena_text; away_arena_text = tk.StringVar()
        global away_capacity_text; away_capacity_text = tk.StringVar() 
        
        global total_rating_home_text; total_rating_home_text = tk.StringVar()
        global forwards_rating_home_text; forwards_rating_home_text = tk.StringVar()
        global defense_rating_home_text; defense_rating_home_text = tk.StringVar()

        global total_rating_away_text; total_rating_away_text = tk.StringVar()
        global forwards_rating_away_text; forwards_rating_away_text = tk.StringVar()
        global defense_rating_away_text; defense_rating_away_text = tk.StringVar()
        
        global home_top_rating; home_top_rating = tk.StringVar()
        global home_second_rating; home_second_rating = tk.StringVar()
        global home_third_rating; home_third_rating = tk.StringVar()

        global home_top_player; home_top_player = tk.StringVar()
        global home_second_player; home_second_player = tk.StringVar()
        global home_third_player; home_third_player = tk.StringVar()

        global away_top_rating; away_top_rating = tk.StringVar()
        global away_second_rating; away_second_rating = tk.StringVar()
        global away_third_rating; away_third_rating = tk.StringVar()

        global away_top_player; away_top_player = tk.StringVar()
        global away_second_player; away_second_player = tk.StringVar()
        global away_third_player; away_third_player = tk.StringVar()


        def ChangeHomeTeamUp():
            global selected_home_team

            selected_home_team += 1
            if selected_home_team == 9:
                selected_home_team = 1

            # Section Informations
            home_coach_name_text.set(equipes[selected_home_team][5])
            home_arena_text.set(equipes[selected_home_team][3])
            home_capacity_text.set(equipes[selected_home_team][4])

            # Section Général
            db.cursor.execute("SELECT CAST(ROUND(AVG(ovr)) AS INT), CAST(ROUND(AVG(off)) AS INT), CAST(ROUND(AVG(def)) AS INT) FROM player WHERE team='"+equipes[selected_home_team][6]+"' AND player.def < 100;")
            global global_rating
            global_rating = db.cursor.fetchall()

            total_rating_home_text.set(global_rating[0][0])
            forwards_rating_home_text.set(global_rating[0][1])
            defense_rating_home_text.set(global_rating[0][2])

            # Section Joueurs
            db.cursor.execute("SELECT * FROM player WHERE team='"+equipes[selected_home_team][6]+"' ORDER BY player.ovr DESC LIMIT 3")
            global home_top3_players
            home_top3_players = db.cursor.fetchall()

            home_top_rating.set(str(home_top3_players[0][11]))
            home_second_rating.set(str(home_top3_players[1][11]))
            home_third_rating.set(str(home_top3_players[2][11]))

            home_top_player.set(home_top3_players[0][1])
            home_second_player.set(home_top3_players[1][1])
            home_third_player.set(home_top3_players[2][1])

            home_team_city.set(equipes[selected_home_team][2])
            home_team_name.set(equipes[selected_home_team][1])

            self.img_home_logo = ImageTk.PhotoImage(file="img/team_logos/"+str(equipes[selected_home_team][0])+".png")
            self.logo_home.config(image=self.img_home_logo)
            

        def ChangeHomeTeamDown():
            global selected_home_team

            selected_home_team -= 1
            if selected_home_team == 0:
                selected_home_team = 8

            # Section Informations
            home_coach_name_text.set(equipes[selected_home_team][5])
            home_arena_text.set(equipes[selected_home_team][3])
            home_capacity_text.set(equipes[selected_home_team][4])

            # Section Joueurs
            db.cursor.execute("SELECT * FROM player WHERE team='"+equipes[selected_home_team][6]+"' ORDER BY player.ovr DESC LIMIT 3")
            global home_top3_players
            home_top3_players = db.cursor.fetchall()

            home_top_rating.set(str(home_top3_players[0][11]))
            home_second_rating.set(str(home_top3_players[1][11]))
            home_third_rating.set(str(home_top3_players[2][11]))

            home_top_player.set(home_top3_players[0][1])
            home_second_player.set(home_top3_players[1][1])
            home_third_player.set(home_top3_players[2][1])

            # Section Général
            db.cursor.execute("SELECT CAST(ROUND(AVG(ovr)) AS INT), CAST(ROUND(AVG(off)) AS INT), CAST(ROUND(AVG(def)) AS INT) FROM player WHERE team='"+equipes[selected_home_team][6]+"' AND player.def < 100;")
            global global_rating
            global_rating = db.cursor.fetchall()

            total_rating_home_text.set(global_rating[0][0])
            forwards_rating_home_text.set(global_rating[0][1])
            defense_rating_home_text.set(global_rating[0][2])

            

            home_team_city.set(equipes[selected_home_team][2])
            home_team_name.set(equipes[selected_home_team][1])

            self.img_home_logo = ImageTk.PhotoImage(file="img/team_logos/"+str(equipes[selected_home_team][0])+".png")
            self.logo_home.config(image=self.img_home_logo)

        def ChangeAwayTeamUp():
            global selected_away_team

            selected_away_team += 1
            if selected_away_team == 9:
                selected_away_team = 1

            # Section Informations
            away_coach_name_text.set(equipes[selected_away_team][5])
            away_arena_text.set(equipes[selected_away_team][3])
            away_capacity_text.set(equipes[selected_away_team][4])
            
            # Section Général
            db.cursor.execute("SELECT CAST(ROUND(AVG(ovr)) AS INT), CAST(ROUND(AVG(off)) AS INT), CAST(ROUND(AVG(def)) AS INT) FROM player WHERE team='"+equipes[selected_away_team][6]+"' AND player.def < 100;")
            global global_rating
            global_rating = db.cursor.fetchall()

            total_rating_away_text.set(global_rating[0][0])
            forwards_rating_away_text.set(global_rating[0][1])
            defense_rating_away_text.set(global_rating[0][2])

            # Section Joueurs
            db.cursor.execute("SELECT * FROM player WHERE team='"+equipes[selected_away_team][6]+"' ORDER BY player.ovr DESC LIMIT 3")
            global away_top3_players
            away_top3_players = db.cursor.fetchall()

            away_top_rating.set(str(away_top3_players[0][11]))
            away_second_rating.set(str(away_top3_players[1][11]))
            away_third_rating.set(str(away_top3_players[2][11]))

            away_top_player.set(away_top3_players[0][1])
            away_second_player.set(away_top3_players[1][1])
            away_third_player.set(away_top3_players[2][1])
            
            away_team_city.set(equipes[selected_away_team][2])
            away_team_name.set(equipes[selected_away_team][1])

            self.img_away_logo = ImageTk.PhotoImage(file="img/team_logos/"+str(equipes[selected_away_team][0])+".png")
            self.logo_away.config(image=self.img_away_logo)

        def ChangeAwayTeamDown():
            global selected_away_team

            selected_away_team -= 1
            if selected_away_team == 0:
                selected_away_team = 8

            # Section Informations
            away_coach_name_text.set(equipes[selected_away_team][5])
            away_arena_text.set(equipes[selected_away_team][3])
            away_capacity_text.set(equipes[selected_away_team][4])

            # Section Joueurs
            db.cursor.execute("SELECT * FROM player WHERE team='"+equipes[selected_away_team][6]+"' ORDER BY player.ovr DESC LIMIT 3")
            global away_top3_players
            away_top3_players = db.cursor.fetchall()

            away_top_rating.set(str(away_top3_players[0][11]))
            away_second_rating.set(str(away_top3_players[1][11]))
            away_third_rating.set(str(away_top3_players[2][11]))

            away_top_player.set(away_top3_players[0][1])
            away_second_player.set(away_top3_players[1][1])
            away_third_player.set(away_top3_players[2][1])

            # Section Général
            db.cursor.execute("SELECT CAST(ROUND(AVG(ovr)) AS INT), CAST(ROUND(AVG(off)) AS INT), CAST(ROUND(AVG(def)) AS INT) FROM player WHERE team='"+equipes[selected_away_team][6]+"' AND player.def < 100;")
            global global_rating
            global_rating = db.cursor.fetchall()

            total_rating_away_text.set(global_rating[0][0])
            forwards_rating_away_text.set(global_rating[0][1])
            defense_rating_away_text.set(global_rating[0][2])

            
            
            away_team_city.set(equipes[selected_away_team][2])
            away_team_name.set(equipes[selected_away_team][1])
            
            self.img_away_logo = ImageTk.PhotoImage(file="img/team_logos/"+str(equipes[selected_away_team][0])+".png")
            self.logo_away.config(image=self.img_away_logo)


        def StartGame():
            teams = (equipes[selected_away_team], equipes[selected_home_team])
            self.controller.show_page(Game, teams)

        self.img_tinynhllogo = tk.PhotoImage(file="img/main_menu/tiny-nhl-logo.png")

        self.awayside_frame = ttk.Frame(self)
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
            font="{Yu Gothic UI Semilight} 12 {}", text='Général')
        self.total_label_away.grid(column=0, pady=3, row=2)
        self.forwards_rating_away = tk.Label(self.team_ratings_away_frame)
        self.forwards_rating_away.configure(
            font="{Yu Gothic UI Semibold} 12 {}", textvariable=forwards_rating_away_text)
        self.forwards_rating_away.grid(column=1, row=0)
        self.defense_rating_away = tk.Label(self.team_ratings_away_frame)
        self.defense_rating_away.configure(
            font="{Yu Gothic UI Semibold} 12 {}", textvariable=defense_rating_away_text)
        self.defense_rating_away.grid(column=1, row=1)
        self.total_rating_away = tk.Label(self.team_ratings_away_frame)
        self.total_rating_away.configure(
            font="{Yu Gothic UI Semibold} 12 {}", textvariable=total_rating_away_text)
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
            textvariable=away_top_player)
        self.best_player_away.grid(column=0, padx=100, pady=3, row=0)
        self.second_player_away = tk.Label(self.player_ratings_away_frame)
        self.second_player_away.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            textvariable=away_second_player)
        self.second_player_away.grid(column=0, pady=3, row=1)
        self.third_player_away = tk.Label(self.player_ratings_away_frame)
        self.third_player_away.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            textvariable=away_third_player)
        self.third_player_away.grid(column=0, pady=3, row=2)
        self.best_player_rating_away = tk.Label(
            self.player_ratings_away_frame)
        self.best_player_rating_away.configure(
            font="{Yu Gothic UI Semibold} 12 {}", textvariable=away_top_rating)
        self.best_player_rating_away.grid(column=1, row=0)
        self.second_player_rating_away = tk.Label(
            self.player_ratings_away_frame)
        self.second_player_rating_away.configure(
            font="{Yu Gothic UI Semibold} 12 {}", textvariable=away_second_rating)
        self.second_player_rating_away.grid(column=1, row=1)
        self.third_player_rating_away = tk.Label(
            self.player_ratings_away_frame)
        self.third_player_rating_away.configure(
            font="{Yu Gothic UI Semibold} 12 {}", textvariable=away_third_rating)
        self.third_player_rating_away.grid(column=1, row=2)
        self.player_ratings_away_frame.pack(side="top")
        self.notebook_away.add(self.player_ratings_away_frame, text='Joueurs')
        self.info_away_frame = tk.Frame(self.notebook_away)
        self.info_away_frame.configure(height=200, width=200)
        self.away_coach_label = tk.Label(self.info_away_frame)
        self.away_coach_label.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            text='Entraîneur-chef')
        self.away_coach_label.grid(column=0, ipadx=50, row=0, sticky="s")
        self.away_coach_name = tk.Label(self.info_away_frame)
        self.away_coach_name.configure(
            font="{Yu Gothic UI Semibold} 12 {bold}",
            textvariable=away_coach_name_text)
        self.away_coach_name.grid(column=0, row=1)
        self.away_arena_label = tk.Label(self.info_away_frame)
        self.away_arena_label.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            text='Aréna/Capacité')
        self.away_arena_label.grid(column=1, ipadx=50, row=0)
        self.away_arena_name = tk.Label(self.info_away_frame)
        self.away_arena_name.configure(
            font="{Yu Gothic UI Semibold} 12 {bold}",
            textvariable=away_arena_text)
        self.away_arena_name.grid(column=1, row=1)
        self.away_capacity = tk.Label(self.info_away_frame)
        self.away_capacity.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            textvariable=away_capacity_text)
        self.away_capacity.grid(column=1, ipadx=50, row=2)
        self.info_away_frame.pack(side="top")
        self.notebook_away.add(self.info_away_frame, text='Informations')
        self.notebook_away.pack(side="top")
        self.team_ratings_away.pack(side="top")
        self.team_ratings_away.pack_propagate(0)
        self.awayside_frame.grid(column=0, row=0)
        self.awayside_frame.pack_propagate(0)
        self.center_frame = ttk.Frame(self)
        self.center_frame.configure(height=720, width=427)
        self.choix_des_equipes_label = tk.Label(self.center_frame)
        self.choix_des_equipes_label.configure(
            font="{Yu Gothic UI Semibold} 24 {}",
            text='Choix des équipes')
        self.choix_des_equipes_label.grid(column=1, row=1)
        self.both_teams_button = ttk.Button(self.center_frame)
        self.img_both_sides = ImageTk.PhotoImage(file="img/arrows/commencer_la_partie.png")
        self.both_teams_button.configure(
            image=self.img_both_sides,
            style="Toolbutton",
            text='button1',
            command=StartGame)
        self.both_teams_button.grid(column=1, row=3)
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
        self.homeside_frame = ttk.Frame(self)
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
        self.logo_home.configure(image=self.img_home_logo, text='label5')
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
            font="{Yu Gothic UI Semilight} 12 {}", text='Général')
        self.total_label_home.grid(column=0, pady=3, row=2)
        self.forwards_rating_home = tk.Label(self.team_ratings_home_frame)
        self.forwards_rating_home.configure(
            font="{Yu Gothic UI Semibold} 12 {}", textvariable=forwards_rating_home_text)
        self.forwards_rating_home.grid(column=1, row=0)
        self.defense_rating_home = tk.Label(self.team_ratings_home_frame)
        self.defense_rating_home.configure(
            font="{Yu Gothic UI Semibold} 12 {}", textvariable=defense_rating_home_text)
        self.defense_rating_home.grid(column=1, row=1)
        self.total_rating_home = tk.Label(self.team_ratings_home_frame)
        self.total_rating_home.configure(
            font="{Yu Gothic UI Semibold} 12 {}", textvariable=total_rating_home_text)
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
            textvariable=home_top_player)
        self.best_player_home.grid(column=0, padx=100, pady=3, row=0)
        self.second_player_home = tk.Label(self.player_ratings_home_frame)
        self.second_player_home.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            textvariable=home_second_player)
        self.second_player_home.grid(column=0, pady=3, row=1)
        self.third_player_home = tk.Label(self.player_ratings_home_frame)
        self.third_player_home.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            textvariable=home_third_player)
        self.third_player_home.grid(column=0, pady=3, row=2)
        self.best_player_rating_home = tk.Label(
            self.player_ratings_home_frame)
        self.best_player_rating_home.configure(
            font="{Yu Gothic UI Semibold} 12 {}", textvariable=home_top_rating)
        self.best_player_rating_home.grid(column=1, row=0)
        self.second_player_rating_home = tk.Label(
            self.player_ratings_home_frame)
        self.second_player_rating_home.configure(
            font="{Yu Gothic UI Semibold} 12 {}", textvariable=home_second_rating)
        self.second_player_rating_home.grid(column=1, row=1)
        self.third_player_rating_home = tk.Label(
            self.player_ratings_home_frame)
        self.third_player_rating_home.configure(
            font="{Yu Gothic UI Semibold} 12 {}", textvariable=home_third_rating)
        self.third_player_rating_home.grid(column=1, row=2)
        self.player_ratings_home_frame.pack(side="top")
        self.notebook_home.add(
            self.player_ratings_home_frame,
            text='Joueurs')
        self.home_info_frame = tk.Frame(self.notebook_home)
        self.home_info_frame.configure(height=200, width=200)
        self.home_coach_label = tk.Label(self.home_info_frame)
        self.home_coach_label.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            text='Entraîneur-chef')
        self.home_coach_label.grid(column=0, ipadx=50, row=0)
        self.home_coach_name = tk.Label(self.home_info_frame)
        self.home_coach_name.configure(
            font="{Yu Gothic UI Semibold} 12 {bold}",
            textvariable=home_coach_name_text)
        self.home_coach_name.grid(column=0, row=1)
        self.home_arena_label = tk.Label(self.home_info_frame)
        self.home_arena_label.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            text='Aréna/Capacité')
        self.home_arena_label.grid(column=1, ipadx=50, row=0)
        self.home_arena = tk.Label(self.home_info_frame)
        self.home_arena.configure(
            font="{Yu Gothic UI Semibold} 12 {bold}",
            textvariable=home_arena_text)
        self.home_arena.grid(column=1, row=1)
        self.home_capacity = tk.Label(self.home_info_frame)
        self.home_capacity.configure(
            font="{Yu Gothic UI Semilight} 12 {}",
            textvariable=home_capacity_text)
        self.home_capacity.grid(column=1, row=2)
        self.home_info_frame.grid(column=0, row=0)
        self.notebook_home.add(self.home_info_frame, text='Informations')
        self.notebook_home.pack(side="top")
        self.team_ratings_home.pack(side="top")
        self.team_ratings_home.pack_propagate(0)
        self.homeside_frame.grid(column=2, row=0)
        self.homeside_frame.pack_propagate(0)
        self.grid_propagate(0)
        self.grid(row=0, column=0, sticky="nsew")

        self.mainwindow = self

        # Première équipe à domicile
        selected_home_team = random.randint(0, len(equipes)-1)
        # Section Informations
        home_coach_name_text.set(equipes[selected_home_team][5])
        home_arena_text.set(equipes[selected_home_team][3])
        home_capacity_text.set(equipes[selected_home_team][4])

        # Section Général
        db.cursor.execute("SELECT CAST(ROUND(AVG(ovr)) AS INT), CAST(ROUND(AVG(off)) AS INT), CAST(ROUND(AVG(def)) AS INT) FROM player WHERE team='"+str(equipes[selected_home_team][6])+"' AND player.def < 100;")
        global_rating = db.cursor.fetchall()

        total_rating_home_text.set(global_rating[0][0])
        forwards_rating_home_text.set(global_rating[0][1])
        defense_rating_home_text.set(global_rating[0][2])
        
        # Section Joueurs
        db.cursor.execute("SELECT * FROM player WHERE team='"+str(equipes[selected_home_team][6])+"' ORDER BY player.ovr DESC LIMIT 3")
        global home_top3_players
        home_top3_players = db.cursor.fetchall()

        home_top_rating.set(str(home_top3_players[0][11]))
        home_second_rating.set(str(home_top3_players[1][11]))
        home_third_rating.set(str(home_top3_players[2][11]))

        home_top_player.set(home_top3_players[0][1])
        home_second_player.set(home_top3_players[1][1])
        home_third_player.set(home_top3_players[2][1])

        home_team_city.set(equipes[selected_home_team][2])
        home_team_name.set(equipes[selected_home_team][1])

        self.img_home_logo = ImageTk.PhotoImage(file="img/team_logos/"+str(equipes[selected_home_team][0])+".png")
        self.logo_home.config(image=self.img_home_logo)

        # Première équipe à l'étranger
        selected_away_team = random.randint(0, len(equipes)-1)
        # Section Informations
        away_coach_name_text.set(equipes[selected_away_team][5])
        away_arena_text.set(equipes[selected_away_team][3])
        away_capacity_text.set(equipes[selected_away_team][4])
        
        # Section Général
        db.cursor.execute("SELECT CAST(ROUND(AVG(ovr)) AS INT), CAST(ROUND(AVG(off)) AS INT), CAST(ROUND(AVG(def)) AS INT) FROM player WHERE team='"+str(equipes[selected_away_team][6])+"' AND player.def < 100;")
        global_rating = db.cursor.fetchall()

        total_rating_away_text.set(global_rating[0][0])
        forwards_rating_away_text.set(global_rating[0][1])
        defense_rating_away_text.set(global_rating[0][2])

        # Section Joueurs
        db.cursor.execute("SELECT * FROM player WHERE team='"+str(equipes[selected_away_team][6])+"' ORDER BY player.ovr DESC LIMIT 3")
        global away_top3_players
        away_top3_players = db.cursor.fetchall()

        away_top_rating.set(str(away_top3_players[0][11]))
        away_second_rating.set(str(away_top3_players[1][11]))
        away_third_rating.set(str(away_top3_players[2][11]))

        away_top_player.set(away_top3_players[0][1])
        away_second_player.set(away_top3_players[1][1])
        away_third_player.set(away_top3_players[2][1])
        
        away_team_city.set(equipes[selected_away_team][2])
        away_team_name.set(equipes[selected_away_team][1])

        self.img_away_logo = ImageTk.PhotoImage(file="img/team_logos/"+str(equipes[selected_away_team][0])+".png")
        self.logo_away.config(image=self.img_away_logo)

if __name__ == "__main__":
    app = QuickGame()
    app.run()


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
        self.root.pack(fill="both", expand=True)


        # Icone et titre
        self.title("NHL Simulator")
        self.img_tinynhllogo = tk.PhotoImage(file="img/main_menu/tiny-nhl-logo.png")
        self.iconphoto(True, self.img_tinynhllogo)

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



"""
class MainMenu:
    def __init__(self, parent, controller):
        # build ui
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.img_tinynhllogo = tk.PhotoImage(file="img/main_menu/tiny-nhl-logo.png")
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
        self.grid_propagate(0)

    def run(self):
        mixer.music.play()
        self.mainwindow.mainloop()

    def GoToQuickGame(self):
        self.controller.show_page(QuickGame)

    def GoToInfo(self):
        pass





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





class Game:
    def __init__(self, master=None):
        # build ui
        self.root = tk.Tk() if master is None else tk.Toplevel(master)
        self.img_tinynhllogo = tk.PhotoImage(file="img/main_menu/tiny-nhl-logo.png")
        self.root.configure(height=720, width=1280)
        self.root.iconphoto(True, self.img_tinynhllogo)
        self.root.resizable(False, False)
        self.root.title("NHL Simulator")
        self.top_frame = ttk.Frame(self.root)
        self.top_frame.configure(height=100, width=1280)
        self.score_frame = ttk.Frame(self.top_frame)
        self.score_frame.configure(height=70, takefocus=True, width=450)
        self.score_away = tk.Button(self.score_frame)
        self.score_away.configure(
            compound="top",
            disabledforeground="#400040",
            font="{@Microsoft JhengHei} 18 {}",
            justify="left",
            overrelief="raised",
            relief="ridge",
            state="disabled",
            textvariable='1',
            width=3)
        self.score_away.grid(column=1, padx=20, pady=10, row=1, sticky="n")
        self.score_home = tk.Button(self.score_frame)
        self.score_home.configure(
            disabledforeground="#400040",
            font="{@Microsoft JhengHei} 18 {}",
            relief="ridge",
            state="disabled",
            textvariable='1',
            width=3)
        self.score_home.grid(column=3, padx=20, pady=10, row=1, sticky="n")
        self.team_name_away = tk.Label(self.score_frame)
        self.team_name_away.configure(
            borderwidth=0,
            font="{Yu Gothic UI} 20 {}",
            textvariable='Visiteure')
        self.team_name_away.grid(column=0, ipady=0, row=1, sticky="se")
        self.city_name_away = tk.Label(self.score_frame)
        self.city_name_away.configure(
            borderwidth=0,
            font="{Yu Gothic UI} 20 {}",
            textvariable='Équipe')
        self.city_name_away.grid(row=1, sticky="ne")
        self.team_name_home = tk.Label(self.score_frame)
        self.team_name_home.configure(
            borderwidth=0,
            font="{Yu Gothic UI} 20 {}",
            textvariable='Domicile')
        self.team_name_home.grid(column=4, row=1, sticky="sw")
        self.city_name_home = tk.Label(self.score_frame)
        self.city_name_home.configure(
            borderwidth=0,
            font="{Yu Gothic UI} 20 {}",
            textvariable='Équipe')
        self.city_name_home.grid(column=4, row=1, sticky="nw")
        self.time = tk.Label(self.score_frame)
        self.time.configure(font="{Yu Gothic} 20 {bold}", textvariable='20:00')
        self.time.grid(column=2, pady=17, row=1, sticky="n")
        self.label3 = tk.Label(self.score_frame)
        self.label3.configure(font="{Microsoft YaHei} 12 {}", textvariable='1ière')
        self.label3.grid(column=2, row=0, rowspan=10, sticky="n")
        self.score_frame.grid(column=1, ipadx=20, row=0, sticky="w")
        self.score_frame.grid_propagate(0)
        self.penalty_frame_away = ttk.Frame(self.top_frame)
        self.penalty_frame_away.configure(height=100, width=400)
        self.pen_label_away = ttk.Label(self.penalty_frame_away)
        self.pen_label_away.configure(
            borderwidth=0,
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            padding=0,
            textvariable='Pénalités')
        self.pen_label_away.grid(column=2, pady=0, row=0)
        self.pen_num_away_1 = ttk.Label(self.penalty_frame_away)
        self.pen_num_away_1.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable='1.')
        self.pen_num_away_1.grid(column=0, padx=5, row=1)
        self.pen_num_away_2 = ttk.Label(self.penalty_frame_away)
        self.pen_num_away_2.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable='1.')
        self.pen_num_away_2.grid(column=0, padx=5, row=2)
        self.pen_name_away_1 = ttk.Label(self.penalty_frame_away)
        self.pen_name_away_1.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable='Nom du joueur')
        self.pen_name_away_1.grid(column=1, row=1)
        self.pen_name_away_2 = ttk.Label(self.penalty_frame_away)
        self.pen_name_away_2.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable='Nom du joueur')
        self.pen_name_away_2.grid(column=1, row=2)
        self.pen_time_away_1 = ttk.Label(self.penalty_frame_away)
        self.pen_time_away_1.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable='2:00')
        self.pen_time_away_1.grid(column=2, padx=50, row=1)
        self.pen_time_away_2 = ttk.Label(self.penalty_frame_away)
        self.pen_time_away_2.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable='2:00')
        self.pen_time_away_2.grid(column=2, padx=50, row=2)
        self.penalty_frame_away.grid(column=0, row=0, sticky="w")
        self.penalty_frame_away.grid_propagate(0)
        self.penalty_frame_home = ttk.Frame(self.top_frame)
        self.penalty_frame_home.configure(height=100, width=400)
        self.pen_label_home = ttk.Label(self.penalty_frame_home)
        self.pen_label_home.configure(
            borderwidth=0,
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            state="normal",
            textvariable='Pénalités')
        self.pen_label_home.grid(column=2, row=0)
        self.pen_num_home_1 = ttk.Label(self.penalty_frame_home)
        self.pen_num_home_1.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable='1.')
        self.pen_num_home_1.grid(column=0, padx=5, row=1)
        self.pen_num_home_2 = ttk.Label(self.penalty_frame_home)
        self.pen_num_home_2.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable='1.')
        self.pen_num_home_2.grid(column=0, padx=5, row=2)
        self.pen_name_home_1 = ttk.Label(self.penalty_frame_home)
        self.pen_name_home_1.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable='Nom du joueur')
        self.pen_name_home_1.grid(column=1, row=1)
        self.pen_name_home_2 = ttk.Label(self.penalty_frame_home)
        self.pen_name_home_2.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable='Nom du joueur')
        self.pen_name_home_2.grid(column=1, row=2)
        self.pen_time_home_1 = ttk.Label(self.penalty_frame_home)
        self.pen_time_home_1.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable='2:00')
        self.pen_time_home_1.grid(column=2, padx=50, row=1)
        self.pen_time_home_2 = ttk.Label(self.penalty_frame_home)
        self.pen_time_home_2.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable='2:00')
        self.pen_time_home_2.grid(column=2, padx=50, row=2)
        self.penalty_frame_home.grid(column=2, row=0, sticky="e")
        self.penalty_frame_home.grid_propagate(0)
        self.top_frame.grid(column=0, row=0)
        self.top_frame.grid_propagate(0)
        self.bottom_frame = ttk.Frame(self.root)
        self.bottom_frame.configure(height=620, width=1280)
        self.away_side_frame = ttk.Frame(self.bottom_frame)
        self.away_side_frame.configure(height=620, width=300)
        self.away_site_treeview = ttk.Treeview(self.away_side_frame)
        self.away_site_treeview.configure(
            height=30, selectmode="none", show="headings")
        self.away_site_treeview_cols = ['column1']
        self.away_site_treeview_dcols = ['column1']
        self.away_site_treeview.configure(
            columns=self.away_site_treeview_cols,
            displaycolumns=self.away_site_treeview_dcols)
        self.away_site_treeview.column(
            "column1",
            anchor="w",
            stretch="true",
            width=200,
            minwidth=20)
        self.away_site_treeview.heading("column1", anchor="w", textvariable='Joueurs')
        self.away_site_treeview.pack(expand="false", ipadx=50, side="top")
        self.away_side_frame.grid(column=0, row=0)
        self.away_side_frame.pack_propagate(0)
        self.home_side_frame = ttk.Frame(self.bottom_frame)
        self.home_side_frame.configure(height=620, width=300)
        self.home_players_treeview = ttk.Treeview(self.home_side_frame)
        self.home_players_treeview.configure(
            height=30, selectmode="extended", show="headings")
        self.home_players_treeview_cols = ['column2']
        self.home_players_treeview_dcols = ['column2']
        self.home_players_treeview.configure(
            columns=self.home_players_treeview_cols,
            displaycolumns=self.home_players_treeview_dcols)
        self.home_players_treeview.column(
            "column2",
            anchor="w",
            stretch="true",
            width=200,
            minwidth=20)
        self.home_players_treeview.heading(
            "column2", anchor="w", textvariable='Joueurs')
        self.home_players_treeview.pack(expand="false", ipadx=50, side="top")
        self.home_side_frame.grid(column=3, row=0)
        self.center_top_frame = ttk.Frame(self.bottom_frame)
        self.center_top_frame.configure(height=300, width=680)
        self.coach_label_away = ttk.Label(self.center_top_frame)
        self.coach_label_away.configure(
            font="{Yu Gothic UI} 12 {}",
            justify="center",
            textvariable='Entraîner-chef')
        self.coach_label_away.grid(column=0, padx=50, row=2)
        self.coach_name_away = ttk.Label(self.center_top_frame)
        self.coach_name_away.configure(
            font="{Yu Gothic UI} 12 {bold}",
            justify="center",
            textvariable='Coach Visiteur')
        self.coach_name_away.grid(column=0, row=3)
        self.coach_label_home = ttk.Label(self.center_top_frame)
        self.coach_label_home.configure(
            font="{Yu Gothic UI} 12 {}",
            justify="center",
            textvariable='Entraîner-chef')
        self.coach_label_home.grid(column=2, padx=50, row=2)
        self.coach_name_home = ttk.Label(self.center_top_frame)
        self.coach_name_home.configure(
            font="{Yu Gothic UI} 12 {bold}",
            justify="center",
            textvariable='Coach Visiteur')
        self.coach_name_home.grid(column=2, row=3)
        self.nhl_logo = ttk.Label(self.center_top_frame)
        self.img_tinynhllogo = tk.PhotoImage(
            file="img/main_menu/tiny-nhl-logo.png")
        self.nhl_logo.configure(image=self.img_tinynhllogo)
        self.nhl_logo.grid(column=1, padx=110, pady=10, row=1)
        self.arena_name = ttk.Label(self.center_top_frame)
        self.arena_name.configure(
            font="{Yu Gothic UI} 14 {}",
            justify="center",
            textvariable='Arena/Stade',
            width=0)
        self.arena_name.grid(column=1, row=5, sticky="n")
        self.logo_home = tk.Label(self.center_top_frame)
        self.img_montreal = tk.PhotoImage(file="img/ingame_logos/montreal.png")
        self.logo_home.configure(image=self.img_montreal)
        self.logo_home.grid(column=2, row=1)
        self.logo_away = tk.Label(self.center_top_frame)
        self.img_toronto = tk.PhotoImage(file="img/ingame_logos/toronto.png")
        self.logo_away.configure(image=self.img_toronto)
        self.logo_away.grid(column=0, row=1)
        self.away_strategy = tk.Button(self.center_top_frame)
        self.img_none = tk.PhotoImage(file="img/arrows/none.png")
        self.away_strategy.configure(image=self.img_none, textvariable='button1')
        self.away_strategy.grid(column=0, pady=20, row=4)
        self.away_strategy.configure(command=self.awayStrategy)
        self.home_strategy = tk.Button(self.center_top_frame)
        self.home_strategy.configure(image=self.img_none, textvariable='button2')
        self.home_strategy.grid(column=2, row=4)
        self.home_strategy.configure(command=self.homeStrategy)
        self.center_top_frame.grid(column=1, row=0, sticky="n")
        self.center_top_frame.grid_propagate(0)
        self.center_bottom_frame = ttk.Frame(self.bottom_frame)
        self.center_bottom_frame.configure(height=350, width=680)
        self.ice_photo = ttk.Label(self.center_bottom_frame)
        self.img_MTL = tk.PhotoImage(file="img/ice/MTL.png")
        self.ice_photo.configure(image=self.img_MTL)
        self.ice_photo.pack(fill="both", side="top")
        self.actions_frame = ScrolledFrame(
            self.center_bottom_frame, scrolltype="both")
        self.actions_frame.innerframe.configure(width=680)
        self.actions_frame.configure(usemousewheel=False)
        self.actions = ttk.Treeview(self.actions_frame.innerframe)
        self.actions.configure(selectmode="none", show="headings")
        self.actions_cols = ['column3']
        self.actions_dcols = ['column3']
        self.actions.configure(
            columns=self.actions_cols,
            displaycolumns=self.actions_dcols)
        self.actions.column(
            "column3",
            anchor="w",
            stretch="true",
            width=200,
            minwidth=20)
        self.actions.heading("column3", anchor="w", textvariable='Actions')
        self.actions.pack(ipadx=230, side="top")
        self.actions_frame.pack(expand="true", fill="x", side="top")
        self.center_bottom_frame.grid(column=1, row=0, sticky="s")
        self.center_bottom_frame.pack_propagate(0)
        self.bottom_frame.grid(column=0, row=1)
        self.bottom_frame.grid_propagate(0)
        self.root.grid_propagate(0)

        # Main widget
        self.mainwindow = self.root

    def run(self):
        self.mainwindow.mainloop()

    def awayStrategy(self):
        pass

    def homeStrategy(self):
        pass

"""
if __name__ == "__main__":
    game = Main()
    game.mainloop()

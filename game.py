#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.scrolledframe import ScrolledFrame


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


if __name__ == "__main__":
    app = Game()
    app.run()

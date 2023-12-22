#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.scrolledframe import ScrolledFrame
from db import Database
from tkinter import messagebox
import random
from db import Database



class Game(tk.Frame):

    global db
    db = Database()

    global overall; overall = []
    global overall_home; overall_home = []
    global overall_away; overall_away = []
    
    
    def receive_info(self, info):

        global away; away = info[0]
        global home; home = info[1]

        global score_away_int; score_away_int = 0
        global score_home_int; score_home_int = 0

        global away_shots_int
        global home_shots_int

        db.cursor.execute("SELECT name, ovr, off, team FROM player WHERE team='"+info[0][6]+"' AND position != 'G'")
        global away_players
        away_players = db.cursor.fetchall()

        

        global away_players_data;away_players_data = []
        global home_players_data;home_players_data = []

        for players in away_players:
            self.away_site_treeview.insert('', tk.END, values=(players[0], 0, 0, 0, 0))
            away_players_data.append({'name': players[0], 'tirs': 0, 'buts': 0, 'aide': 0, 'points': 0})

        for x in range(0, len(away_players)):
            for y in range(0, away_players[x][1]):
                overall.append([away_players[x][0], away_players[x][1], away_players[x][3]])
                overall_away.append([away_players[x][0], away_players[x][1], away_players[x][3]])

        db.cursor.execute("SELECT name, ovr, off, team FROM player WHERE team='"+info[1][6]+"' AND position != 'G'")
        global home_players
        home_players = db.cursor.fetchall()

        for players in home_players:
            self.home_players_treeview.insert('', tk.END, values=(players[0], 0, 0, 0, 0))
            home_players_data.append({'name': players[0], 'tirs': 0, 'buts': 0, 'aide': 0, 'points': 0})
        
        for x in range(0, len(home_players)):
            for y in range(0, home_players[x][1]):
                overall.append([home_players[x][0], home_players[x][1], home_players[x][3]])
                overall_home.append([home_players[x][0], home_players[x][1], home_players[x][3]])
        
        db.cursor.execute("SELECT AVG(def) FROM player WHERE team='"+info[0][6]+"'")
        global away_defense
        away_defense = db.cursor.fetchall()

        db.cursor.execute("SELECT AVG(def) FROM player WHERE team='"+info[1][6]+"'")
        global home_defense
        home_defense = db.cursor.fetchall()

        self.img_home = tk.PhotoImage(file="img/ingame_logos/"+info[1][2]+".png")
        self.img_away = tk.PhotoImage(file="img/ingame_logos/"+info[0][2]+".png")

        self.ice_img = tk.PhotoImage(file="img/ice/"+info[1][6]+".png")

        arena_name_text.set(info[1][3])

        score_away_text.set(0)
        score_home_text.set(0)

        team_name_away_text.set(info[0][2])
        city_name_away_text.set(info[0][1])

        team_name_home_text.set(info[1][2])
        city_name_home_text.set(info[1][1])

        coach_name_away_text.set(info[0][5])
        coach_name_home_text.set(info[1][5])

        pen_num_away_1_text.set("")
        pen_num_away_2_text .set("")
        pen_name_away_1_text.set("")
        pen_name_away_2_text.set("")
        pen_time_away_1_text.set("")
        pen_time_away_2_text.set("")
        pen_label_home_text.set("")
        pen_num_home_1_text.set("")
        pen_num_home_2_text.set("")
        pen_name_home_1_text.set("")
        pen_name_home_2_text.set("")
        pen_time_home_1_text.set("")
        pen_time_home_2_text.set("")

        self.game_period = 1

        away_shots_int = 0
        away_shots.set(away_shots_int)
        home_shots_int = 0
        home_shots.set(home_shots_int)
        
        self.ice_photo.configure(image=self.ice_img)
        
        self.arena_name = ttk.Label(self.center_top_frame)
        self.arena_name.configure(
            font="{Yu Gothic UI} 14 {}",
            justify="center",
            textvariable=arena_name_text,
            width=0)
        self.arena_name.grid(column=1, row=5, sticky="n")
        self.logo_home = tk.Label(self.center_top_frame)
        self.logo_home.configure(image=self.img_home)
        self.logo_home.grid(column=2, row=1)
        self.logo_away = tk.Label(self.center_top_frame)
        self.logo_away.configure(image=self.img_away)
        self.logo_away.grid(column=0, row=1)

        messagebox.showinfo("Début du match", "Le match est sur le point de commencer")
        self.GameLoop(1200)

    def period_string_update(self, period_in_param):
        if period_in_param == 1:
            period_text.set("1ère")
            period_str = "1ère"
        elif period_in_param == 2:
            period_text.set("2ième")
            period_str = "2ième"
        elif period_in_param == 3:
            period_text.set("3ième")
            period_str = "3ième"
        elif period_in_param == 4 and score_away_int == score_home_int:
            period_text.set("Prol.")
            period_str = "Prol."
            return
        elif period_in_param == 4 and score_away_int != score_home_int:
            messagebox.showinfo("Match terminé!", f"Marque Finale:\rAway:{score_away_text.get()}\rHome:{score_home_text.get()}")
            quit()
        return period_str
    
    def GameLoop(self, time_left):
        global away_shots_int
        global home_shots_int


        def update_selected_away(player_name, action):
            for item in self.away_site_treeview.get_children():
                if self.away_site_treeview.item(item, "text") == player_name:
                    self.away_site_treeview.focus(item)
                
                for row in away_players_data:
                    if row['name'] == player_name:
                        item_info = self.away_site_treeview.item(item)
                        if item_info['values'][0] == player_name:
                            if action == "tir":
                                row['tirs'] += 1
                            elif action == "but":
                                row['buts'] += 1
                                row['points'] += 1
                            elif action == "aide":
                                row['aide'] += 1
                                row['points'] += 1
                            self.away_site_treeview.item(item, values=(row['name'], row['tirs'], row['buts'], row['aide'], row['points']))
                            self.away_site_treeview.selection_set(item)

        def update_selected_home(player_name, action):
            for item in self.home_players_treeview.get_children():
                if self.home_players_treeview.item(item, "text") == player_name:
                    self.home_players_treeview.focus(item)

                for row in home_players_data:
                    if row['name'] == player_name:
                        item_info = self.home_players_treeview.item(item)
                        if item_info['values'][0] == player_name:
                            if action == "tir":
                                row['tirs'] += 1
                            elif action == "but":
                                row['buts'] += 1
                                row['points'] += 1
                            elif action == "aide":
                                row['aide'] += 1
                                row['points'] += 1
                            self.home_players_treeview.item(item, values=(row['name'], row['tirs'], row['buts'], row['aide'], row['points']))
                            self.home_players_treeview.selection_set(item)


        mins, secs = divmod(time_left, 60)
        self.timer.config(text=f"{mins:02d}:{secs:02d}")
        
        try:
            try:
                action = random.randint(0, 200000)
                if away[6] == overall[action][2]:
                    update_selected_away(overall[action][0], 'tir')
                    num_assists = 0
                    global score_away_int
                    away_shots_int += 1
                    away_shots.set(away_shots_int)
                    attack = overall[action][1] / 100
                    defense = home_defense[0][0] / 100
                    sog = random.uniform(0, 1.5)
                    goal_probability = attack * (1 - defense)
                    if sog <= goal_probability:
                        score_away_int += 1
                        score_away_text.set(score_away_int)
                        
                        self.actions.insert('', 0, values=(f"But",away[1], overall[action][0], f'{mins:02d}:{secs:02d}', period_text.get()))

                        num_assists = random.randint(0, 2)
                        
                        assists = []
                        if num_assists > 0:
                            for i in range(num_assists):
                                away_assists = random.randint(0, len(overall_away))
                                assists.append(overall_away[away_assists][0])
                        print(assists)

                        if num_assists == 1:
                            update_selected_away(assists[0], 'aide')
                            messagebox.showinfo(f"ET LE BUUUUT DES {home[1].upper()} !",
                            f"Marqué par :\n\n{overall[action][0]}\n\nAssisté par: {assists[0]}")
                        elif num_assists == 2:
                            update_selected_away(assists[0], 'aide')
                            update_selected_away(assists[1], 'aide')
                            messagebox.showinfo(f"ET LE BUUUUT DES {home[1].upper()} !",
                            f"Marqué par :\n\n{overall[action][0]}\n\nAssisté par:\n{assists[0]}\n{assists[1]}")
                        else:
                            messagebox.showinfo(f"ET LE BUUUUT DES {home[1].upper()} !",
                            f"Marqué par :\n\n{overall[action][0]}\n\nSans aides")
                        update_selected_away(overall[action][0], 'but')
                    else:
                        self.actions.insert('', 0, values=(f"Tir",away[1], overall[action][0], f'{mins:02d}:{secs:02d}', period_text.get()))


                elif home[6] == overall[action][2]:
                    update_selected_home(overall[action][0], 'tir')
                    global score_home_int
                    home_shots_int += 1
                    home_shots.set(home_shots_int)
                    attack = overall[action][1] / 100
                    defense = away_defense[0][0] / 100
                    sog = random.uniform(0, 1.5)
                    goal_probability = attack * (1 - defense)
                    if sog <= goal_probability:
                        score_home_int += 1
                        score_home_text.set(score_home_int)
                        self.actions.insert('', 0, values=(f"But",home[1], overall[action][0], f'{mins:02d}:{secs:02d}', period_text.get()))

                        num_assists = random.randint(0, 2)
                        assists = []
                        if num_assists > 0:
                            for i in range(num_assists):
                                home_assists = random.randint(0, len(overall_home))
                                assists.append(overall_home[home_assists][0])

                        if num_assists == 1:
                            update_selected_home(assists[0], 'aide')
                            messagebox.showinfo(f"ET LE BUUUUT DES {home[1].upper()} !",
                            f"Marqué par :\n\n{overall[action][0]}\n\nAssisté par: {assists[0]}")
                        elif num_assists == 2:
                            update_selected_home(assists[0], 'aide')
                            update_selected_home(assists[1], 'aide')
                            messagebox.showinfo(f"ET LE BUUUUT DES {home[1].upper()} !",
                            f"Marqué par :\n\n{overall[action][0]}\n\nAssisté par: {assists[0]}\n{assists[1]}")
                        else:
                            messagebox.showinfo(f"ET LE BUUUUT DES {home[1].upper()} !",
                            f"Marqué par :\n\n{overall[action][0]}\nSans aides")
                        update_selected_home(overall[action][0], 'but')
                    else:
                        self.actions.insert('', 0, values=(f"Tir",home[1], overall[action][0], f'{mins:02d}:{secs:02d}', period_text.get()))
            
            except TypeError:
                pass
        except IndexError:
            pass
        
        self.period_string_update(self.game_period)

        if self.game_period <= 3:
            if time_left > 0:  # Continue countdown until time_left becomes 0
                self.after(50, self.GameLoop, time_left - 1)
            else:
                self.actions.insert('', 0, values=('','', '', '', ''))
                self.actions.insert('', 0, values=('----------','----------', f'FIN DE LA {period_text.get().upper()} PÉRIODE', '----------', '----------'))
                self.actions.insert('', 0, values=('','', '', '', ''))
                self.game_period += 1
                messagebox.showinfo("Fin de la période", f"Débuter la {self.period_string_update(self.game_period)} période")
                if self.game_period == 4 and score_away_int == score_home_int:
                    self.GameLoop(300)
                else:
                    self.GameLoop(1200)

    def __init__(self, parent, controller):

        # Text Variables
        global score_away_text;score_away_text = tk.StringVar()
        global score_home_text;score_home_text = tk.StringVar()
        global team_name_away_text;team_name_away_text = tk.StringVar()
        global city_name_away_text;city_name_away_text = tk.StringVar()
        global team_name_home_text;team_name_home_text = tk.StringVar()
        global city_name_home_text;city_name_home_text = tk.StringVar()
        global timer_text;timer_text = tk.StringVar()
        global period_text;period_text = tk.StringVar()
        global pen_label_away;pen_label_away = tk.StringVar()
        global pen_num_away_1_text;pen_num_away_1_text = tk.StringVar()
        global pen_num_away_2_text;pen_num_away_2_text = tk.StringVar()
        global pen_name_away_1_text;pen_name_away_1_text = tk.StringVar()
        global pen_name_away_2_text;pen_name_away_2_text = tk.StringVar()
        global pen_time_away_1_text;pen_time_away_1_text = tk.StringVar()
        global pen_time_away_2_text;pen_time_away_2_text = tk.StringVar()
        global pen_label_home_text;pen_label_home_text = tk.StringVar()
        global pen_num_home_1_text;pen_num_home_1_text = tk.StringVar()
        global pen_num_home_2_text;pen_num_home_2_text = tk.StringVar()
        global pen_name_home_1_text;pen_name_home_1_text = tk.StringVar()
        global pen_name_home_2_text;pen_name_home_2_text = tk.StringVar()
        global pen_time_home_1_text;pen_time_home_1_text = tk.StringVar()
        global pen_time_home_2_text;pen_time_home_2_text = tk.StringVar()
        global coach_name_away_text;coach_name_away_text = tk.StringVar()
        global coach_name_home_text;coach_name_home_text = tk.StringVar()
        global arena_name_text;arena_name_text = tk.StringVar()
        global away_shots;away_shots = tk.StringVar()
        global home_shots;home_shots = tk.StringVar()


        # build ui
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.img_tinynhllogo = tk.PhotoImage(file="img/main_menu/tiny-nhl-logo.png")
        self.top_frame = ttk.Frame(self)
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
            textvariable=str(score_away_text),
            width=3)
        self.score_away.grid(column=1, padx=20, pady=10, row=1, sticky="n")
        self.score_home = tk.Button(self.score_frame)
        self.score_home.configure(
            disabledforeground="#400040",
            font="{@Microsoft JhengHei} 18 {}",
            relief="ridge",
            state="disabled",
            textvariable=str(score_home_text),
            width=3)
        self.score_home.grid(column=3, padx=20, pady=10, row=1, sticky="n")
        self.team_name_away = tk.Label(self.score_frame)
        self.team_name_away.configure(
            borderwidth=0,
            font="{Yu Gothic UI} 20 {}",
            textvariable=team_name_away_text)
        self.team_name_away.grid(column=0, ipady=0, row=1, sticky="se")
        self.city_name_away = tk.Label(self.score_frame)
        self.city_name_away.configure(
            borderwidth=0,
            font="{Yu Gothic UI} 20 {}",
            textvariable=city_name_away_text)
        self.city_name_away.grid(row=1, sticky="ne")
        self.team_name_home = tk.Label(self.score_frame)
        self.team_name_home.configure(
            borderwidth=0,
            font="{Yu Gothic UI} 20 {}",
            textvariable=team_name_home_text)
        self.team_name_home.grid(column=4, row=1, sticky="sw")
        self.city_name_home = tk.Label(self.score_frame)
        self.city_name_home.configure(
            borderwidth=0,
            font="{Yu Gothic UI} 20 {}",
            textvariable=city_name_home_text)
        self.city_name_home.grid(column=4, row=1, sticky="nw")
        self.timer = tk.Label(self.score_frame)
        self.timer.configure(font="{Yu Gothic} 20 {bold}", text="20:00")
        self.timer.grid(column=2, pady=17, row=1, sticky="n")
        self.period = tk.Label(self.score_frame)
        self.period.configure(font="{Microsoft YaHei} 12 {}", textvariable=period_text)
        self.period.grid(column=2, row=0, rowspan=10, sticky="n")
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
            textvariable=pen_label_away)
        self.pen_label_away.grid(column=2, pady=0, row=0)
        self.pen_num_away_1 = ttk.Label(self.penalty_frame_away)
        self.pen_num_away_1.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable=pen_num_away_1_text)
        self.pen_num_away_1.grid(column=0, padx=5, row=1)
        self.pen_num_away_2 = ttk.Label(self.penalty_frame_away)
        self.pen_num_away_2.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable=pen_num_away_2_text)
        self.pen_num_away_2.grid(column=0, padx=5, row=2)
        self.pen_name_away_1 = ttk.Label(self.penalty_frame_away)
        self.pen_name_away_1.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable=pen_name_away_1_text)
        self.pen_name_away_1.grid(column=1, row=1)
        self.pen_name_away_2 = ttk.Label(self.penalty_frame_away)
        self.pen_name_away_2.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable=pen_name_away_2_text)
        self.pen_name_away_2.grid(column=1, row=2)
        self.pen_time_away_1 = ttk.Label(self.penalty_frame_away)
        self.pen_time_away_1.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable=pen_time_away_1_text)
        self.pen_time_away_1.grid(column=2, padx=50, row=1)
        self.pen_time_away_2 = ttk.Label(self.penalty_frame_away)
        self.pen_time_away_2.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable=pen_time_away_2_text)
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
            textvariable=pen_label_home_text)
        self.pen_label_home.grid(column=2, row=0)
        self.pen_num_home_1 = ttk.Label(self.penalty_frame_home)
        self.pen_num_home_1.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable=pen_num_home_1_text)
        self.pen_num_home_1.grid(column=0, padx=5, row=1)
        self.pen_num_home_2 = ttk.Label(self.penalty_frame_home)
        self.pen_num_home_2.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable=pen_num_home_2_text)
        self.pen_num_home_2.grid(column=0, padx=5, row=2)
        self.pen_name_home_1 = ttk.Label(self.penalty_frame_home)
        self.pen_name_home_1.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable=pen_name_home_1_text)
        self.pen_name_home_1.grid(column=1, row=1)
        self.pen_name_home_2 = ttk.Label(self.penalty_frame_home)
        self.pen_name_home_2.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable=pen_name_home_2_text)
        self.pen_name_home_2.grid(column=1, row=2)
        self.pen_time_home_1 = ttk.Label(self.penalty_frame_home)
        self.pen_time_home_1.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable=pen_time_home_1_text)
        self.pen_time_home_1.grid(column=2, padx=50, row=1)
        self.pen_time_home_2 = ttk.Label(self.penalty_frame_home)
        self.pen_time_home_2.configure(
            font="{Yu Gothic UI} 16 {}",
            foreground="#ff0000",
            textvariable=pen_time_home_2_text)
        self.pen_time_home_2.grid(column=2, padx=50, row=2)
        self.penalty_frame_home.grid(column=2, row=0, sticky="e")
        self.penalty_frame_home.grid_propagate(0)
        self.top_frame.grid(column=0, row=0)
        self.top_frame.grid_propagate(0)
        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.configure(height=620, width=1280)
        self.away_side_frame = ttk.Frame(self.bottom_frame)
        self.away_side_frame.configure(height=620, width=300)
        self.away_site_treeview = ttk.Treeview(self.away_side_frame)
        self.away_site_treeview.configure(
            height=30, selectmode="none", show="headings")
        self.away_site_treeview_cols = ['joueurs', 'tirs', 'buts', 'aide', 'points']
        self.away_site_treeview_dcols = ['joueurs', 'tirs', 'buts', 'aide', 'points']
        self.away_site_treeview.configure(
            columns=self.away_site_treeview_cols,
            displaycolumns=self.away_site_treeview_dcols)
        self.away_site_treeview.column(
            "joueurs",
            anchor="w",
            stretch="true",
            width=120,
            minwidth=50)
        self.away_site_treeview.column(
            "tirs",
            anchor="w",
            stretch="true",
            width=5,
            minwidth=5)
        self.away_site_treeview.column(
            "buts",
            anchor="w",
            stretch="true",
            width=5,
            minwidth=5)
        self.away_site_treeview.column(
            "aide",
            anchor="w",
            stretch="true",
            width=5,
            minwidth=5)
        self.away_site_treeview.column(
            "points",
            anchor="w",
            stretch="true",
            width=5,
            minwidth=5)
        self.away_site_treeview.heading("joueurs", anchor="w", text='Joueurs')
        self.away_site_treeview.heading("tirs", anchor="w", text='T')
        self.away_site_treeview.heading("buts", anchor="w", text='B')
        self.away_site_treeview.heading("aide", anchor="w", text='A')
        self.away_site_treeview.heading("points", anchor="w", text='P')
        self.away_site_treeview.pack(expand="false", ipadx=50, side="top")
        self.away_side_frame.grid(column=0, row=0)
        self.away_side_frame.pack_propagate(0)
        self.home_side_frame = ttk.Frame(self.bottom_frame)
        self.home_side_frame.configure(height=620, width=300)
        self.home_players_treeview = ttk.Treeview(self.home_side_frame)
        self.home_players_treeview.configure(
            height=30, selectmode="extended", show="headings")
        self.home_players_treeview_cols = ['joueurs', 'tirs', 'buts', 'aide', 'points']
        self.home_players_treeview_dcols = ['joueurs', 'tirs', 'buts', 'aide', 'points']
        self.home_players_treeview.configure(
            columns=self.home_players_treeview_cols,
            displaycolumns=self.home_players_treeview_dcols)
        self.home_players_treeview.column(
            "joueurs",
            anchor="w",
            stretch="true",
            width=120,
            minwidth=50)
        self.home_players_treeview.column(
            "tirs",
            anchor="w",
            stretch="true",
            width=10,
            minwidth=10)
        self.home_players_treeview.column(
            "buts",
            anchor="w",
            stretch="true",
            width=10,
            minwidth=10)
        self.home_players_treeview.column(
            "aide",
            anchor="w",
            stretch="true",
            width=10,
            minwidth=10)
        self.home_players_treeview.column(
            "points",
            anchor="w",
            stretch="true",
            width=10,
            minwidth=10)
        self.home_players_treeview.heading("joueurs", anchor="w", text='Joueurs')
        self.home_players_treeview.heading("tirs", anchor="w", text='T')
        self.home_players_treeview.heading("buts", anchor="w", text='B')
        self.home_players_treeview.heading("aide", anchor="w", text='A')
        self.home_players_treeview.heading("points", anchor="w", text='P')
        self.home_players_treeview.pack(expand="false", ipadx=50, side="top")
        self.home_side_frame.grid(column=3, row=0)
        self.center_top_frame = ttk.Frame(self.bottom_frame)
        self.center_top_frame.configure(height=300, width=680)
        self.coach_label_away = ttk.Label(self.center_top_frame)
        self.coach_label_away.configure(
            font="{Yu Gothic UI} 12 {}",
            justify="center",
            text='Entraîneur-chef')
        self.coach_label_away.grid(column=0, padx=50, row=2)
        self.coach_name_away = ttk.Label(self.center_top_frame)
        self.coach_name_away.configure(
            font="{Yu Gothic UI} 12 {bold}",
            justify="center",
            textvariable=coach_name_away_text)
        self.coach_name_away.grid(column=0, row=3)
        self.coach_label_home = ttk.Label(self.center_top_frame)
        self.coach_label_home.configure(
            font="{Yu Gothic UI} 12 {}",
            justify="center",
            text='Entraîneur-chef')
        self.coach_label_home.grid(column=2, padx=50, row=2)
        self.coach_name_home = ttk.Label(self.center_top_frame)
        self.coach_name_home.configure(
            font="{Yu Gothic UI} 12 {bold}",
            justify="center",
            textvariable=coach_name_home_text)
        self.coach_name_home.grid(column=2, row=3)
        self.nhl_logo = ttk.Label(self.center_top_frame)
        self.img_tinynhllogo = tk.PhotoImage(
            file="img/main_menu/tiny-nhl-logo.png")
        self.nhl_logo.configure(image=self.img_tinynhllogo)
        self.nhl_logo.grid(column=1, padx=110, pady=10, row=1)
        self.away_sog = tk.Button(self.center_top_frame)
        self.img_none = tk.PhotoImage(file="img/arrows/none.png")
        self.away_sog.configure(textvariable=away_shots,
                                font="{Yu Gothic UI} 13 {}",
                                justify="center",
                                width=2)
        self.away_sog.grid(column=0, pady=20, row=4)
        self.home_sog = tk.Button(self.center_top_frame)
        self.home_sog.configure(textvariable=home_shots,
                                font="{Yu Gothic UI} 13 {}",
                                justify="center",
                                width=2)
        self.home_sog.grid(column=2, row=4)
        self.sog_label = tk.Label(self.center_top_frame)
        self.sog_label.configure(text="<- Tirs au but ->",
                                 font="{Yu Gothic UI} 13 {}",
                                 justify="center")
        self.sog_label.grid(column=1, row=4)
        self.center_top_frame.grid(column=1, row=0, sticky="n")
        self.center_top_frame.grid_propagate(0)
        self.center_bottom_frame = ttk.Frame(self.bottom_frame)
        self.center_bottom_frame.configure(height=350, width=680)
        self.ice_photo = ttk.Label(self.center_bottom_frame)
        self.ice_photo.pack(fill="both", side="top")
        self.actions_frame = ScrolledFrame(
            self.center_bottom_frame, scrolltype="both")
        self.actions_frame.innerframe.configure(width=680)
        self.actions_frame.configure(usemousewheel=True)
        self.actions = ttk.Treeview(self.actions_frame.innerframe)
        self.actions.configure(selectmode="none", show="headings")
        self.actions_cols = ['action', 'equipe', 'joueur', 'temps', 'period']
        self.actions_dcols = ['action', 'equipe', 'joueur', 'temps', 'period']
        self.actions.configure(
            columns=self.actions_cols,
            displaycolumns=self.actions_dcols)
        self.actions.column(
            "action",
            anchor="e",
            stretch="true",
            width=1,
            minwidth=20)
        self.actions.column(
            "equipe",
            anchor="w",
            stretch="true",
            width=1,
            minwidth=20)
        self.actions.column(
            "joueur",
            anchor="w",
            stretch="true",
            width=190,
            minwidth=20)
        self.actions.column(
            "temps",
            anchor="w",
            stretch="true",
            width=1,
            minwidth=20)
        self.actions.column(
            "period",
            anchor="w",
            stretch="true",
            width=1,
            minwidth=20)
        self.actions.heading("action", anchor="w", text='Action')
        self.actions.heading("equipe", anchor="w", text='Équipe')
        self.actions.heading("joueur", anchor="w", text='Joueur')
        self.actions.heading("temps", anchor="w", text='Temps')
        self.actions.heading("period", anchor="w", text='Période')
        self.actions.pack(ipadx=230, side="top")
        self.actions_frame.pack(expand="true", fill="x", side="top")
        self.center_bottom_frame.grid(column=1, row=0, sticky="s")
        self.center_bottom_frame.pack_propagate(0)
        self.bottom_frame.grid(column=0, row=1)
        self.bottom_frame.grid_propagate(0)
        self.grid_propagate(0)
        self.grid(row=0, column=0, sticky="nsew")

        # Main widget
        self.mainwindow = self


    
        
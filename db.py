import sqlite3

class Database:
    con = sqlite3.connect("nhl_simulator.db")
    cursor = con.cursor()
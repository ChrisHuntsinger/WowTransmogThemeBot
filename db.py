import sqlite3


#define connection

connection = sqlite3.connect('transmogCompetition.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
    player_competition
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        player_name TEXT,
        user_id TEXT,
        display_name TEXT,
        theme TEXT,
         )"""

cursor.execute(command1)

cursor.execute("INSERT INTO player_competition VALUES(1, 'Ziarcane', 'ChrisHuntsing', 'Christian', 'Pirates'")

cursor.execute("SELECT * FROM player_competition ")

results = cursor.fetchall()
print(results)
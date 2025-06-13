import sqlite3


#define connection


def insert_theme(player_name, user_id, display_name, theme):

    connection = sqlite3.connect('transmogCompetition.db')

    cursor = connection.cursor()

    command1 = """CREATE TABLE IF NOT EXISTS
        player_competition
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            player_name TEXT,
            user_id TEXT,
            display_name TEXT,
            theme TEXT
            )"""

    cursor.execute(command1)

    cursor.execute("INSERT INTO player_competition VALUES(NULL, ?, ?, ?, ?)", (player_name, user_id, display_name, theme))

    connection.commit()
    connection.close()
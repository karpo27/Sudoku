import sqlite3


def create_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    query = '''CREATE TABLE IF NOT EXISTS Score(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(80) UNIQUE,
        EASY_WINS INT DEFAULT 0,
        MEDIUM_WINS INT DEFAULT 0,
        HARD_WINS INT DEFAULT 0
        );'''
    cursor.execute(query)

    cursor.close()
    connection.close()


def insert_player_name(p_name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    query = f'''INSERT OR IGNORE INTO Score(NAME) VALUES ('{p_name}');'''
    cursor.execute(query)
    connection.commit()

    cursor.close()
    connection.close()


def show_data(p_name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    query_select = f'''SELECT * FROM Score WHERE NAME = '{p_name}';'''
    cursor.execute(query_select)
    data = cursor.fetchall()
    connection.commit()

    print("\n"
          f"Statistics - Player: {p_name}\n"
          "\n"
          f"Easy Wins {data[0][2]}\n"
          f"Medium Wins {data[0][3]}\n"
          f"Hard Wins {data[0][4]}\n"
          "")

    cursor.close()
    connection.close()


def update_player_score(p_name, g_mode):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    category = {
        "1": 'EASY_WINS',
        "2": 'MEDIUM_WINS',
        "3": 'HARD_WINS'
    }

    query_update = f'''UPDATE Score SET {category[g_mode]} = {category[g_mode]} + 1 WHERE NAME = '{p_name}';'''
    cursor.execute(query_update)
    connection.commit()

    cursor.close()
    connection.close()
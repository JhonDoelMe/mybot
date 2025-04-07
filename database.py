import sqlite3
from contextlib import closing

DB_NAME = 'bot.db'

def init_db():
    with closing(sqlite3.connect(DB_NAME)) as conn:
        with open('database.sql') as f:
            conn.executescript(f.read())
        conn.commit()

def add_user(user_id, username, first_name, last_name):
    with closing(sqlite3.connect(DB_NAME)) as conn:
        conn.execute('''
            INSERT OR IGNORE INTO users (user_id, username, first_name, last_name)
            VALUES (?, ?, ?, ?)
        ''', (user_id, username, first_name, last_name))
        conn.commit()
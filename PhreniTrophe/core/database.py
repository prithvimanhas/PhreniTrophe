import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        with self._connect() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS meals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    food TEXT,
                    calories REAL,
                    method TEXT
                )
            ''')

    def add_meal(self, food, calories, method):
        with self._connect() as conn:
            conn.execute("INSERT INTO meals (date, food, calories, method) VALUES (?, ?, ?, ?)",
                         (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), food, calories, method))

    def get_today_total(self):
        today = datetime.now().strftime("%Y-%m-%d")
        with self._connect() as conn:
            cur = conn.execute("SELECT SUM(calories) FROM meals WHERE date LIKE ?", (today + "%",))
            total = cur.fetchone()[0]
        return total or 0

    def get_recent(self, limit=5):
        with self._connect() as conn:
            cur = conn.execute("SELECT date, food, calories, method FROM meals ORDER BY id DESC LIMIT ?", (limit,))
            return cur.fetchall()

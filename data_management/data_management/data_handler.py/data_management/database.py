import pandas as pd

class DataHandler:
    def __init__(self, config):
        self.data_path = config.get("data_path", "data/trade_data.csv")

    def store(self, data):
        df = pd.DataFrame(data)
        df.to_csv(self.data_path, mode='a', header=False, index=False)

    def log_trade(self, trade):
        df = pd.DataFrame([trade])
        df.to_csv(self.data_path, mode='a', header=False, index=False)


import sqlite3

class Database:
    def __init__(self, config):
        self.db_path = config.get("db_path", "data/syntherra.db")
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS trades (
                id INTEGER PRIMARY KEY,
                pair TEXT,
                signal TEXT,
                profit REAL,
                timestamp TEXT
            )
        """)
        self.connection.commit()

    def insert_trade(self, pair, signal, profit):
        self.cursor.execute("""
            INSERT INTO trades (pair, signal, profit, timestamp)
            VALUES (?, ?, ?, datetime('now'))
        """, (pair, signal, profit))
        self.connection.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM trades")
        return self.cursor.fetchall()

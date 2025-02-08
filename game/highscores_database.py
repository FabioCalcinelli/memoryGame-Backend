import sqlite3
from game.models import Highscore

class HighscoresDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS highscores (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def add_highscore(self, highscore):
        self.cursor.execute("""
            INSERT INTO highscores (name, score) VALUES (?, ?)
        """, (highscore.name, highscore.score))
        self.conn.commit()
        self._limit_to_top_10()

    def _limit_to_top_10(self):
        self.cursor.execute("""
            DELETE FROM highscores
            WHERE id IN (
                SELECT id
                FROM (
                    SELECT id,
                    ROW_NUMBER() OVER (ORDER BY score ASC) as row_num
                    FROM highscores
                ) AS subquery
                WHERE row_num > 10
            )
        """)
        self.conn.commit()

    def get_highscores(self):
        self.cursor.execute("""
            SELECT name, score FROM highscores ORDER BY score DESC
        """)
        highscores = self.cursor.fetchall()
        return [Highscore(name, score) for name, score in highscores]

    def close(self):
        self.conn.close()
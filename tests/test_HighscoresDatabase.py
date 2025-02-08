import pytest

from game.highscores_database import HighscoresDatabase
from game.models import Highscore
import sqlite3
import os

@pytest.fixture
def db():
    db_name = 'test_database.db'
    db = HighscoresDatabase(db_name)
    yield db
    db.close()
    os.remove(db_name)

def test_add_highscore(db):
    highscore = Highscore('Test Player', 100)
    db.add_highscore(highscore)
    assert len(db.get_highscores()) == 1

def test_add_multiple_highscores(db):
    for i in range(15):
        highscore = Highscore(f'Player {i}', 100 - i)
        db.add_highscore(highscore)
    assert len(db.get_highscores()) == 10

def test_get_highscores(db):
    for i in range(15):
        highscore = Highscore(f'Player {i}', 100 - i)
        db.add_highscore(highscore)
    highscores = db.get_highscores()
    for i, highscore in enumerate(highscores):
        assert highscore.name == f'Player {i+5}'
        assert highscore.score == 95 - i

def test_close(db):
    db.close()
    with pytest.raises(sqlite3.ProgrammingError):
        db.cursor.execute("SELECT * FROM highscores")
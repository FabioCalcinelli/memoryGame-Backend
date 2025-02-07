import pytest
from game.models import HighscoreBoard

def test_highscore_init():
    highscore = HighscoreBoard.Highscore('John', 100)
    assert highscore.name == 'John'
    assert highscore.score == 100

def test_highscore_identical():
    highscore1 = HighscoreBoard.Highscore('John', 100)
    highscore2 = HighscoreBoard.Highscore('John', 100)
    assert highscore1 == highscore2

def test_highscore_equivalent():
    highscore1 = HighscoreBoard.Highscore('John', 100)
    highscore2 = HighscoreBoard.Highscore('Jane', 100)
    assert highscore1 != highscore2

def test_highscore_lt():
    highscore1 = HighscoreBoard.Highscore('John', 100)
    highscore2 = HighscoreBoard.Highscore('Jane', 50)
    assert highscore2 > highscore1

def test_highscore_gt():
    highscore1 = HighscoreBoard.Highscore('John', 100)
    highscore2 = HighscoreBoard.Highscore('Jane', 50)
    assert highscore1 < highscore2

def test_highscoreboard_init():
    highscoreboard = HighscoreBoard()
    assert highscoreboard.highscores == []

def test_add_highscore():
    highscoreboard = HighscoreBoard()
    highscore = HighscoreBoard.Highscore('John', 100)
    highscoreboard.add_highscore(highscore)
    assert len(highscoreboard.highscores) == 1
    assert highscoreboard.highscores[0] == highscore

def test_get_highscores_in_order():
    highscoreboard = HighscoreBoard()
    highscore1 = HighscoreBoard.Highscore('John', 100)
    highscore2 = HighscoreBoard.Highscore('Jane', 50)
    highscore3 = HighscoreBoard.Highscore('Bob', 200)
    highscoreboard.add_highscore(highscore1)
    highscoreboard.add_highscore(highscore2)
    highscoreboard.add_highscore(highscore3)
    highscores = highscoreboard.get_highscores_in_order()
    assert len(highscores) == 3
    assert highscores[0].score == highscore2.score
    assert highscores[1].score == highscore1.score
    assert highscores[2].score == highscore3.score

def test_get_highscores_in_order_empty():
    highscoreboard = HighscoreBoard()
    highscores = highscoreboard.get_highscores_in_order()
    assert len(highscores) == 0
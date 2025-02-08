import pytest
from game.models import Highscore

def test_highscore_init():
    highscore = Highscore('John', 100)
    assert highscore.name == 'John'
    assert highscore.score == 100

def test_highscore_identical():
    highscore1 = Highscore('John', 100)
    highscore2 = Highscore('John', 100)
    assert highscore1 == highscore2

def test_highscore_equivalent():
    highscore1 = Highscore('John', 100)
    highscore2 = Highscore('Jane', 100)
    assert highscore1 != highscore2

def test_highscore_lt():
    highscore1 = Highscore('John', 100)
    highscore2 = Highscore('Jane', 50)
    assert highscore2 > highscore1

def test_highscore_gt():
    highscore1 = Highscore('John', 100)
    highscore2 = Highscore('Jane', 50)
    assert highscore1 < highscore2
import pytest
from game.logic import Game

@pytest.fixture
def game():
    return Game(5)

def test_init(game):
    assert game.nr_of_pairs == 5
    assert game.nr_of_moves == 0
    assert not game.game_over
    assert len(game.flipped) == 10
    assert len(game.found) == 10
    assert len(game.card_numbers) == 10

def test_reset(game):
    game.nr_of_moves = 10
    game.game_over = True
    game.flipped = [True] * 10
    game.found = [True] * 10
    game.reset()
    assert game.nr_of_moves == 0
    assert not game.game_over
    assert len(game.flipped) == 10
    assert len(game.found) == 10
    assert len(game.card_numbers) == 10

def test_reset_flipped(game):
    game.flipped = [True] * 10
    game.reset_flipped()
    assert game.flipped == [False] * 10

def test_manage_new_flipped_card_no_match(game):
    game.flipped = [True, True] + [False] * 8
    game.card_numbers = [1, 2] + [3] * 8
    game.nr_of_moves = 0
    game.manage_new_flipped_card()
    assert game.nr_of_moves == 1

def test_manage_new_flipped_card_match(game):
    game.flipped = [True, True] + [False] * 8
    game.card_numbers = [1, 1] + [3] * 8
    game.found = [False] * 10
    game.nr_of_moves = 0
    game.manage_new_flipped_card()
    assert game.nr_of_moves == 1
    assert game.found == [True, True] + [False] * 8

def test_find_new_pair(game):
    game.found = [False] * 10
    game.flipped = [True, True] + [False] * 8
    game.find_new_pair(0, 1)
    assert game.found == [True, True] + [False] * 8
    assert game.flipped == [False, False] + [False] * 8

def test_check_game_over(game):
    game.found = [True] * 10
    game.check_game_over()
    assert game.game_over

def test_update_no_effect(game):
    game.flipped = [True] + [False] * 9
    game.found = [True] + [False] * 9
    game.update(0)
    assert game.flipped == [True] + [False] * 9
    assert game.found == [True] + [False] * 9

def test_update_third_card_click(game):
    game.flipped = [True, True] + [False] * 8
    game.update(2)
    assert game.flipped == [False] * 10

def test_update_new_card(game):
    game.flipped = [False] * 10
    game.update(0)
    assert game.flipped == [True] + [False] * 9

def test_get_state(game):
    state = game.get_state()
    assert state is not None

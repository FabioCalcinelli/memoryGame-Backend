from game.models import GameState
from utils import get_random_pairs


class Game:
    def __init__(self, nr_of_pairs: int):
        self.nr_of_moves = None
        self.game_over = None
        self.found = None
        self.flipped = None
        self.card_numbers = None
        self.nr_of_pairs = nr_of_pairs
        self.reset()

    def reset_flipped(self):
        self.flipped = [False for n in range(self.nr_of_pairs*2)]

    def manage_new_flipped_card(self):
        flipped_indexes = [i for i, x in enumerate(self.flipped) if x]
        if len(flipped_indexes) == 2:
            self.nr_of_moves += 1
            if self.card_numbers[flipped_indexes[0]] == self.card_numbers[flipped_indexes[1]]:
                self.find_new_pair(flipped_indexes[0],flipped_indexes[1])

    def find_new_pair(self, index1: int, index2: int):
        self.found[index1] = True
        self.found[index2] = True
        self.flipped[index1] = False
        self.flipped[index2] = False
        self.check_game_over()

    def check_game_over(self):
        if all(self.found):
            self.game_over = True

    def update(self, clicked_card_index: int):
        # clicking on a found or flipped card never has any effect
        if self.flipped[clicked_card_index] or self.found[clicked_card_index]:
            return
        # third card click, covers all cards
        if self.flipped.count(True)==2:
            self.reset_flipped()
        else:
            self.flipped[clicked_card_index] = True
            self.manage_new_flipped_card()

    def reset(self):
        self.card_numbers = get_random_pairs(self.nr_of_pairs)
        self.flipped = [False for _ in range(self.nr_of_pairs*2)]
        self.found = [False for _ in range(self.nr_of_pairs*2)]
        self.game_over = False
        self.nr_of_moves = 0

    def get_state(self):
        return GameState(self.card_numbers, self.flipped, self.found, self.game_over, self.nr_of_moves)


class HighscoreBoard:
    class Highscore:
        name: str = None
        score: int = None
        def __init__(self, name: str, score: int):
            self.name = name
            self.score = score

        def __lt__(self, other: 'Highscore') -> bool:
            return self.score > other.score

        def __gt__(self, other: 'Highscore') -> bool:
            return self.score < other.score

        def __eq__(self, other: 'Highscore') -> bool:
            return self.score == other.score and self.name == other.name


    highscores: list[Highscore] = []

    def __init__(self, highscores: list[Highscore] = None):
        if highscores is None:
            highscores = []
        self.highscores = highscores

    def add_highscore(self, highscore: Highscore):
        self.highscores.append(highscore)

    def get_highscores_in_order(self):
        scores = self.highscores.copy()
        scores.sort(key=lambda x: x, reverse=True)
        return scores







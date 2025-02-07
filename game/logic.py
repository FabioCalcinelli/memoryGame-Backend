from game.models import GameState


class Game:
    def __init__(self, nr_of_cards: int):
        self.flipped = [False for n in range(nr_of_cards)]
        self.found = [False for n in range(nr_of_cards)]
        self.game_over = False
        self.nr_of_moves = 0

    def update(self, clicked_card_index):
        pass

    def get_state(self):
        return GameState(self.flipped, self.found, self.game_over, self.nr_of_moves)

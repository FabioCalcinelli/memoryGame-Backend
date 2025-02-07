

class GameState:
    flipped: list[bool] = []
    found: list[bool] = []
    game_over: bool = False
    nr_of_moves: int = 0
    def __init__(self, flipped, found, game_over, nr_of_moves):
        self.flipped = flipped
        self.found = found
        self.game_over = game_over
        self.nr_of_moves = nr_of_moves
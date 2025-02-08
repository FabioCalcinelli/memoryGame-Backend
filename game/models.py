class GameState:
    card_numbers: list[int]
    flipped: list[bool] = []
    found: list[bool] = []
    game_over: bool = False
    nr_of_moves: int = 0

    def __init__(self, card_numbers, flipped, found, game_over, nr_of_moves):
        self.card_numbers = card_numbers
        self.flipped = flipped
        self.found = found
        self.game_over = game_over
        self.nr_of_moves = nr_of_moves


class HighscoreBoard:
    class Highscore:
        name: str = None
        score: int = None

        def __init__(self, name: str, score: int):
            self.name = name
            self.score = score

        def __repr__(self):
            return f'Highscore(name={self.name}, score={self.score})'

        def __str__(self):
            return f'{self.name} scored {self.score}'

        def __lt__(self, other: 'Highscore') -> bool:
            return self.score > other.score

        def __gt__(self, other: 'Highscore') -> bool:
            return self.score < other.score

        def __eq__(self, other: 'Highscore') -> bool:
            return self.score == other.score and self.name == other.name

    highscores: list[Highscore] = []
    size: int = 10
    def __init__(self, size: int = 10, highscores: list[Highscore] = None):
        self.size = size
        if highscores is None:
            highscores = []
        self.highscores = highscores

    def add_highscore(self, highscore: Highscore):
        self.highscores.append(highscore)
        self.highscores.sort(key=lambda x: x, reverse=True)
        self.highscores = self.highscores[:self.size]

    def get_highscores_in_order(self):
        return self.highscores

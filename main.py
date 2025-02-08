from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from game.logic import Game
from game.models import HighscoreBoard

app = FastAPI()
nr_of_pairs = 3

highscore_board = HighscoreBoard()
game = Game(nr_of_pairs)

class CardClickRequest(BaseModel):
    card_id: int

class GetHighscoresRequest(BaseModel):
    pass

class AddHighscoreRequest(BaseModel):
    highscore_name: str
    highscore_score: int

origins = [
    "http://localhost:5172",
    "http://localhost:5173",  # Frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "This is a memoryGame backend"}

@app.get("/start_game")
async def start_game():
    game.reset()
    return {"message": "Game started successfully", "game_state": game.get_state()}

@app.patch("/card_click")
async def handle_card_click(request: CardClickRequest):
    game.update(request.card_id)
    return {"message": "Card clicked and game updated", "game_state": game.get_state()}

@app.get("/get_highscores")
async def get_highscores(request: GetHighscoresRequest):
    return {"message": "Highscores", "highscores": highscore_board.get_highscores_in_order()}

@app.patch("/add_highscore")
async def add_highscore(request: AddHighscoreRequest):
    if not request.highscore_name or len(request.highscore_name) > 20:
        return {"error": "Invalid highscore name"}
    if request.highscore_score < 0:
        return {"error": "Invalid highscore score"}
    highscore = HighscoreBoard.Highscore(request.highscore_name, request.highscore_score)
    highscore_board.add_highscore(highscore)
    return {"message": "Highscore added"}





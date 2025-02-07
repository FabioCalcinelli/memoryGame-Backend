from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from game.logic import Game

app = FastAPI()
nr_of_pairs = 3

game = Game(nr_of_pairs)

class CardClickRequest(BaseModel):
    card_id: int

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
    return {"game_state": game.get_state()}



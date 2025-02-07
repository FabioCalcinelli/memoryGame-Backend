from fastapi import FastAPI, Request
from pydantic import BaseModel

from game.logic import Game

app = FastAPI()

game = Game()

class CardClickRequest(BaseModel):
    card_id: int


@app.get("/")
async def root():
    return {"message": "This is a memoryGame backend"}


@app.post("/card_click")
async def handle_card_click(request: CardClickRequest):
    game_update = {"clicked_card": request.card_id}
    game.update(game_update)
    return {"updated_card": request.card_id, "game_state": game.get_state()}



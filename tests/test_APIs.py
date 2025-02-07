import pytest
from starlette.testclient import TestClient
from main import game, app  # Replace 'your_app' with the actual name of your module

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_root(client):
    """Test the root API"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data == {"message": "This is a memoryGame backend"}

def test_start_game(client):
    """Test the start game API"""
    response = client.get("/start_game")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Game started successfully"
    assert "game_state" in data

def test_card_click(client, mocker):
    """Test the card click API"""
    # Mock the CardClickRequest object
    class CardClickRequest:
        def __init__(self, card_id):
            self.card_id = card_id

    # Mock the game.update and game.get_state methods
    mocker.patch("main.game.update")
    mocker.patch("main.game.get_state")

    # Create a CardClickRequest object
    request = CardClickRequest(1)

    response = client.patch("/card_click", json={"card_id": request.card_id})
    assert response.status_code == 200
    data = response.json()
    assert "game_state" in data

    # Check if the game.update and game.get_state methods were called
    game.update.assert_called_once_with(request.card_id)
    game.get_state.assert_called_once()

def test_card_click_invalid_request(client):
    """Test the card click API with an invalid request"""
    response = client.patch("/card_click", json={})
    assert response.status_code == 422  # Assuming 422 is the status code for invalid request

from fastapi.testclient import TestClient
from main import api

client = TestClient(api)


def test_get_pokemons():
    result = client.get("/pokemons")
    json_data = result.json()

    assert result.status_code == 200
    assert len(json_data) == 2
    assert {"number": 1, "name": "Pikachu"} in json_data
    assert {"number": 2, "name": "Ditto"} in json_data


def test_get_pokemon_by_number():
    result = client.get("/pokemons/1")
    json_data = result.json()

    assert result.status_code == 200
    assert json_data["number"] == 1
    assert json_data["name"] == "Pikachu"


def test_get_pokemon_by_number_error_404():
    result = client.get("/pokemons/99999")
    json_data = result.json()

    assert result.status_code == 404
    assert "detail" in json_data


def test_get_pokemon_by_number_error_incorrect_param():
    result = client.get("/pokemons/0")
    json_data = result.json()

    assert result.status_code == 422
    assert "detail" in json_data


def test_post_pokemon():
    json_post = {"number": 3, "name": "Mew"}
    result = client.post("/pokemons", json=json_post)
    json_data = result.json()

    assert result.status_code == 201
    assert json_data["number"] == 3
    assert json_data["name"] == "Mew"


def test_post_pokemon_error_400():
    json_post = {"number": 2, "name": "Ditto"}
    result = client.post("/pokemons", json=json_post)
    json_data = result.json()

    assert result.status_code == 400
    assert "detail" in json_data

def test_post_pokemon_error_incorret_input():
    json_post = {"number": 0, "name": "Ditto"}
    result = client.post("/pokemons", json=json_post)
    json_data = result.json()

    assert result.status_code == 422
    assert "detail" in json_data
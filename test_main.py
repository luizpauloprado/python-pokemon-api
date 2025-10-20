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


def test_get_pokemon_by_number_error_not_found():
    result = client.get("/pokemons/99999")
    json_data = result.json()

    assert result.status_code == 404
    assert "detail" in json_data


def test_get_pokemon_by_number_error_incorrect_param():
    result = client.get("/pokemons/0")
    json_data = result.json()

    assert result.status_code == 422
    assert "detail" in json_data

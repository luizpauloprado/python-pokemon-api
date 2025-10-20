from fastapi import FastAPI, HTTPException, Query, Path, status
from pydantic import BaseModel, Field
from typing import Annotated
import httpx


# wire out
class PokemonOut(BaseModel):
    number: int
    name: str


class PokemonIn(BaseModel):
    number: int = Field(gt=0)
    name: str = Field(min_length=3)


# db
db: dict[int, PokemonOut] = {
    1: PokemonOut(number=1, name="Pikachu"),
    2: PokemonOut(number=2, name="Ditto"),
}

# api
api = FastAPI()


@api.get("/pokemons", response_model=list[PokemonOut])
def get_pokemons(skip: int = 0, limit: int = 10):
    try:
        response = httpx.get(
            f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={skip}"
        )

        response.raise_for_status()
        data = response.json()
        pokemons: list[PokemonOut] = [
            PokemonOut(number=number, name=item["name"])
            for number, item in enumerate(data["results"], start=1)
        ]

        return pokemons
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex)


@api.get("/pokemons/{number}", response_model=PokemonOut)
def get_pokemon(number: Annotated[int, Path(gt=0)]):
    if not db.get(number):
        raise HTTPException(status_code=404, detail="Not found!")

    return db.get(number)


@api.post("/pokemons", response_model=PokemonOut, status_code=status.HTTP_201_CREATED)
def post_pokemon(pokemon_in: PokemonIn):
    if pokemon_in.number in db.keys():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Pokemon number already in use!",
        )

    db[pokemon_in.number] = PokemonOut(number=pokemon_in.number, name=pokemon_in.name)
    return db[pokemon_in.number]

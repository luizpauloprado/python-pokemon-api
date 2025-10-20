from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel
from typing import Annotated


class PokemonOut(BaseModel):
    number: int
    name: str


db: dict[int, PokemonOut] = {
    1: PokemonOut(number=1, name="Pikachu"),
    2: PokemonOut(number=2, name="Ditto"),
}

api = FastAPI()


@api.get("/pokemons", response_model=list[PokemonOut])
def get_pokemons(skip: int = 0, limit: int = 10):
    data = list(db.values())
    return data[skip : skip + limit]


@api.get("/pokemons/{number}", response_model=PokemonOut)
def get_pokemon(number: Annotated[int, Path(gt=0)]):
    if not db.get(number):
        raise HTTPException(status_code=404, detail="Not found!")

    return db.get(number)

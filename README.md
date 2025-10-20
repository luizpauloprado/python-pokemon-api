# Python Pokemon API 

Python FastAPI project to call PokéAPI

## Run

```
pip install -r requirements.txt
fastapi dev main.py
```

## Virtual environment

Install deps:

```
pip install -r requirements.txt
```

Create .venv:
```
python -m venv .venv
```

Activate:

```
source .venv/bin/activate
```

Deactivate:

```
deactivate
```

Generate requirements.txt:
```
pip freeze > requirements.txt
```

## Deps

```
"fastapi[standard]"
pytest
pytest-httpx
```

## Test

```
pytest test_app.py
```
https://pokeapi.co/
## Utils

[PokeAPI](https://pokeapi.co/)

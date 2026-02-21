# faker_pokemon

Faker community provider for Pokemon data.

## Installation

```bash
uv add faker_pokemon
```

## Usage

```python
from faker import Faker
from faker_pokemon import PokemonProvider

fake = Faker()
fake.add_provider(PokemonProvider)

fake.pokemon_name()   # "Pikachu"
fake.pokemon_type()   # "Fire"
fake.pokemon_move()   # "Thunderbolt"
fake.pokemon()        # {"name": "Charizard", "type": "Dragon", "move": "Flamethrower"}
```

## Available methods

| Method           | Returns                              |
|------------------|--------------------------------------|
| `pokemon_name()` | A random Pokemon name (`str`)        |
| `pokemon_type()` | A random Pokemon type (`str`)        |
| `pokemon_move()` | A random Pokemon move (`str`)        |
| `pokemon()`      | A dict with `name`, `type`, `move`   |

## Updating data

Fetch the latest data from [PokeAPI](https://pokeapi.co/):

```bash
uv run scripts/update_data.py
```

PokeAPI is a free, open API with no authentication required.
Please respect their [fair use policy](https://pokeapi.co/docs/v2):

- Do not make excessive requests — the update script only needs 3 calls
- Cache locally (which is exactly what this package does by committing the data)
- Do not abuse the service — it is primarily an educational tool

## Disclaimer

Pokemon names, types, and moves are trademarks of Nintendo/The Pokemon Company.
This package is not affiliated with or endorsed by Nintendo or The Pokemon Company.
Data sourced from [PokeAPI](https://pokeapi.co/).

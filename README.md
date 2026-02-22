# faker_pokemon

Faker community provider that overrides standard Faker methods with Pokemon-themed data.

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

# Standard Faker methods, now Pokemon-themed
fake.company()          # "Silph Co."
fake.city()             # "Cerulean City"
fake.country()          # "Kanto"
fake.first_name()       # "Pikachu"
fake.full_name()        # "Charizard Fire"
fake.product_name()     # "Ultra Ball"

# Pokemon-specific methods
fake.pokemon_name()     # "Bulbasaur"
fake.pokemon_type()     # "Water"
fake.pokemon_move()     # "Thunderbolt"
fake.pokemon_ability()  # "Levitate"
fake.pokemon_nature()   # "Jolly"
fake.pokemon_berry()    # "Oran"
```

## Available methods

### Standard Faker overrides

| Method             | Returns                                    |
|--------------------|--------------------------------------------|
| `company()`        | A Pokemon world company (`str`)            |
| `company_suffix()` | A company suffix (`str`)                   |
| `city()`           | A Pokemon location (`str`)                 |
| `country()`        | A Pokemon region (`str`)                   |
| `street_name()`    | A Pokemon-themed street name (`str`)       |
| `first_name()`     | A Pokemon name (`str`)                     |
| `last_name()`      | A Pokemon type (`str`)                     |
| `full_name()`      | A Pokemon name + type (`str`)              |
| `product_name()`   | A Pokemon item (`str`)                     |
| `product_category()`| A Pokemon item category (`str`)           |

### Pokemon-specific methods

| Method              | Returns                              |
|---------------------|--------------------------------------|
| `pokemon_name()`    | A random Pokemon name (`str`)        |
| `pokemon_type()`    | A random Pokemon type (`str`)        |
| `pokemon_move()`    | A random Pokemon move (`str`)        |
| `pokemon_ability()` | A random Pokemon ability (`str`)     |
| `pokemon_nature()`  | A random Pokemon nature (`str`)      |
| `pokemon_berry()`   | A random Pokemon berry (`str`)       |

## Updating data

Fetch the latest data from [PokeAPI](https://pokeapi.co/):

```bash
uv run scripts/update_data.py
```

PokeAPI is a free, open API with no authentication required.
Please respect their [fair use policy](https://pokeapi.co/docs/v2):

- Do not make excessive requests — the update script only needs ~10 calls
- Cache locally (which is exactly what this package does by committing the data)
- Do not abuse the service — it is primarily an educational tool

## Disclaimer

Pokemon names, types, and moves are trademarks of Nintendo/The Pokemon Company.
This package is not affiliated with or endorsed by Nintendo or The Pokemon Company.
Data sourced from [PokeAPI](https://pokeapi.co/).

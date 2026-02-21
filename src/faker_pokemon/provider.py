from faker.providers import BaseProvider

from .pokemon_data import POKEMON_MOVES, POKEMON_NAMES, POKEMON_TYPES


class PokemonProvider(BaseProvider):
    """A Faker provider for Pokemon-related fake data."""

    def pokemon_name(self) -> str:
        """Return a random Pokemon name."""
        return self.random_element(POKEMON_NAMES)

    def pokemon_type(self) -> str:
        """Return a random Pokemon type."""
        return self.random_element(POKEMON_TYPES)

    def pokemon_move(self) -> str:
        """Return a random Pokemon move name."""
        return self.random_element(POKEMON_MOVES)

    def pokemon(self) -> dict:
        """Return a random Pokemon with name, type, and move."""
        return {
            "name": self.pokemon_name(),
            "type": self.pokemon_type(),
            "move": self.pokemon_move(),
        }

from faker.providers import BaseProvider

from faker_pokemon.pokemon_data import (
    POKEMON_ABILITIES,
    POKEMON_BERRIES,
    POKEMON_COMPANIES,
    POKEMON_COMPANY_SUFFIXES,
    POKEMON_ITEM_CATEGORIES,
    POKEMON_ITEMS,
    POKEMON_LOCATIONS,
    POKEMON_MOVES,
    POKEMON_NAMES,
    POKEMON_NATURES,
    POKEMON_REGIONS,
    POKEMON_STREET_SUFFIXES,
    POKEMON_TYPES,
)


class PokemonProvider(BaseProvider):
    """A Faker provider that overrides standard methods with Pokemon-themed data."""

    def pokemon_name(self) -> str:
        """Return a random Pokemon name."""
        return self.random_element(POKEMON_NAMES)

    def pokemon_type(self) -> str:
        """Return a random Pokemon type."""
        return self.random_element(POKEMON_TYPES)

    def pokemon_move(self) -> str:
        """Return a random Pokemon move name."""
        return self.random_element(POKEMON_MOVES)

    def pokemon_ability(self) -> str:
        """Return a random Pokemon ability."""
        return self.random_element(POKEMON_ABILITIES)

    def pokemon_nature(self) -> str:
        """Return a random Pokemon nature."""
        return self.random_element(POKEMON_NATURES)

    def pokemon_berry(self) -> str:
        """Return a random Pokemon berry."""
        return self.random_element(POKEMON_BERRIES)

    def company(self) -> str:
        """Return a random Pokemon world company name."""
        return self.random_element(POKEMON_COMPANIES)

    def company_suffix(self) -> str:
        """Return a random Pokemon company suffix."""
        return self.random_element(POKEMON_COMPANY_SUFFIXES)

    def city(self) -> str:
        """Return a random Pokemon location as city."""
        return self.random_element(POKEMON_LOCATIONS)

    def country(self) -> str:
        """Return a random Pokemon region as country."""
        return self.random_element(POKEMON_REGIONS)

    def street_name(self) -> str:
        """Return a Pokemon-themed street name."""
        return (
            f"{self.random_element(POKEMON_NAMES)} "
            f"{self.random_element(POKEMON_STREET_SUFFIXES)}"
        )

    def first_name(self) -> str:
        """Return a random Pokemon name as first name."""
        return self.random_element(POKEMON_NAMES)

    def last_name(self) -> str:
        """Return a random Pokemon type as last name."""
        return self.random_element(POKEMON_TYPES)

    def full_name(self) -> str:
        """Return a Pokemon-themed full name."""
        return f"{self.first_name()} {self.last_name()}"

    def product_name(self) -> str:
        """Return a random Pokemon item as product name."""
        return self.random_element(POKEMON_ITEMS)

    def product_category(self) -> str:
        """Return a random Pokemon item category."""
        return self.random_element(POKEMON_ITEM_CATEGORIES)

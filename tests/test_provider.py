import pytest
from faker import Faker

from faker_pokemon import PokemonProvider
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


@pytest.fixture
def fake():
    fake = Faker()
    fake.add_provider(PokemonProvider)
    return fake


class TestPokemonName:
    def test_returns_string(self, fake):
        assert isinstance(fake.pokemon_name(), str)

    def test_returns_valid_pokemon(self, fake):
        assert fake.pokemon_name() in POKEMON_NAMES

    def test_seed_reproducibility(self):
        fake1 = Faker()
        fake1.add_provider(PokemonProvider)
        fake1.seed_instance(12345)

        fake2 = Faker()
        fake2.add_provider(PokemonProvider)
        fake2.seed_instance(12345)

        assert fake1.pokemon_name() == fake2.pokemon_name()


class TestPokemonType:
    def test_returns_string(self, fake):
        assert isinstance(fake.pokemon_type(), str)

    def test_returns_valid_type(self, fake):
        assert fake.pokemon_type() in POKEMON_TYPES


class TestPokemonMove:
    def test_returns_string(self, fake):
        assert isinstance(fake.pokemon_move(), str)

    def test_returns_valid_move(self, fake):
        assert fake.pokemon_move() in POKEMON_MOVES


class TestPokemonAbility:
    def test_returns_string(self, fake):
        assert isinstance(fake.pokemon_ability(), str)

    def test_returns_valid_ability(self, fake):
        assert fake.pokemon_ability() in POKEMON_ABILITIES


class TestPokemonNature:
    def test_returns_string(self, fake):
        assert isinstance(fake.pokemon_nature(), str)

    def test_returns_valid_nature(self, fake):
        assert fake.pokemon_nature() in POKEMON_NATURES


class TestPokemonBerry:
    def test_returns_string(self, fake):
        assert isinstance(fake.pokemon_berry(), str)

    def test_returns_valid_berry(self, fake):
        assert fake.pokemon_berry() in POKEMON_BERRIES


class TestCompany:
    def test_company(self, fake):
        assert fake.company() in POKEMON_COMPANIES

    def test_company_suffix(self, fake):
        assert fake.company_suffix() in POKEMON_COMPANY_SUFFIXES


class TestAddress:
    def test_city(self, fake):
        assert fake.city() in POKEMON_LOCATIONS

    def test_country(self, fake):
        assert fake.country() in POKEMON_REGIONS

    def test_street_name(self, fake):
        street = fake.street_name()
        parts = street.rsplit(" ", 1)
        assert len(parts) == 2
        assert parts[0] in POKEMON_NAMES
        assert parts[1] in POKEMON_STREET_SUFFIXES


class TestPerson:
    def test_first_name(self, fake):
        assert fake.first_name() in POKEMON_NAMES

    def test_last_name(self, fake):
        assert fake.last_name() in POKEMON_TYPES

    def test_full_name(self, fake):
        name = fake.full_name()
        parts = name.split(" ", 1)
        assert parts[0] in POKEMON_NAMES
        assert parts[1] in POKEMON_TYPES


class TestCommerce:
    def test_product_name(self, fake):
        assert fake.product_name() in POKEMON_ITEMS

    def test_product_category(self, fake):
        assert fake.product_category() in POKEMON_ITEM_CATEGORIES

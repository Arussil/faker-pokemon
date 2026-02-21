import pytest
from faker import Faker

from faker_pokemon import PokemonProvider
from faker_pokemon.pokemon_data import POKEMON_MOVES, POKEMON_NAMES, POKEMON_TYPES


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


class TestPokemon:
    def test_returns_dict(self, fake):
        result = fake.pokemon()
        assert isinstance(result, dict)

    def test_dict_keys(self, fake):
        result = fake.pokemon()
        assert set(result.keys()) == {"name", "type", "move"}

    def test_dict_values_valid(self, fake):
        result = fake.pokemon()
        assert result["name"] in POKEMON_NAMES
        assert result["type"] in POKEMON_TYPES
        assert result["move"] in POKEMON_MOVES

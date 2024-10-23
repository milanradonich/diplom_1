import pytest

from .bun import Bun
from .burger import Burger
from .database import Database
from .ingredient import Ingredient


@pytest.fixture
def bun_instance():
    """фикстура создание экземпляра класса Bun"""
    return Bun(name='Вкусная булочка', price=100.50)


@pytest.fixture
def burger_instance():
    """фикстура создание экземпляра класса Burger"""
    return Burger()


@pytest.fixture
def ingredient_instance():
    """фикстура создание экземпляра класса Ingredient"""
    return Ingredient(ingredient_type='Соусы', name='Соус фирменный Space Sauce', price=80.0)


@pytest.fixture
def database_instance():
    """фикстура создание экземпляра класса Database"""
    return Database()


import pytest

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    # Фикстура для создания Burger

    # setup
    return Burger()

@pytest.fixture
def bun():
    # Фикстура для создания Bun

    # setup
    return Bun("Булочка",10)

@pytest.fixture
def sauce():
    # Фикстура для создания Соуса

    # setup
    return Ingredient(INGREDIENT_TYPE_SAUCE,"Кетчуп",1)

@pytest.fixture
def filling():
    # Фикстура для создания Начинки

    # setup
    return Ingredient(INGREDIENT_TYPE_FILLING,"Сыр",2)
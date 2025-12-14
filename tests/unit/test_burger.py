import allure
import pytest


@allure.feature("Тесты burger")
class TestBurger:

    @allure.title("Создание burger")
    def test_init(self, burger):
        # Arrange

        # Act

        # Assert
        assert burger is not None
        assert burger.bun is None
        assert burger.ingredients == []

    @allure.title("Добавление булочки в burger")
    def test_set_bun(self, burger, bun):
        # Arrange

        # Act
        burger.set_buns(bun)

        # Assert
        assert burger.bun == bun

    @allure.title("Добавление ингредиента в burger")
    def test_add_ingredient(self, burger, sauce):
        # Arrange

        # Act
        burger.add_ingredient(sauce)

        # Assert
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == sauce

    @allure.title("Удаление ингредиента из burger")
    def test_remove_ingredient(self, burger, sauce, filling):
        # Arrange
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        # Act
        burger.remove_ingredient(0)

        # Assert
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == filling

    @allure.title("Изменение порядка ингредиентов в burger")
    def test_move_ingredient(self, burger, sauce, filling):
        # Arrange
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        # Act
        burger.move_ingredient(0,1)

        # Assert
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == filling
        assert burger.ingredients[1] == sauce

    @allure.title("Получение итоговой цены burger")
    def test_get_price(self, burger, bun, sauce, filling):
        # Arrange
        burger.set_buns(bun) # 10
        burger.add_ingredient(sauce) # 1
        burger.add_ingredient(filling) # 2

        # Act
        total = burger.get_price()

        # Assert
        assert total == 23 # (20*2)+(1+2)

    @allure.title("Получение рецепта burger")
    def test_get_receipt(self, burger, bun, sauce, filling):
        # Arrange
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        # Act
        receipt = burger.get_receipt()

        # Assert
        expected = (
            f"(==== {bun.get_name()} ====)\n"
            f"= {sauce.get_type().lower()} {sauce.get_name()} =\n"
            f"= {filling.get_type().lower()} {filling.get_name()} =\n"
            f"(==== {bun.get_name()} ====)\n\n"
            f"Price: {burger.get_price()}"
        )

        assert receipt == expected

    @allure.title("Удаление ингредиента по неверному индексу приводит к ошибке")
    @pytest.mark.parametrize("index", [1, 100])
    def test_remove_ingredient_invalid_index(self, burger, sauce, index):
        # Arrange
        burger.add_ingredient(sauce)

        # Act / Assert
        with pytest.raises(IndexError):
            burger.remove_ingredient(index)

    @allure.title("Перемещение ингредиентов с неверными индексуами приводит к ошибке")
    def test_move_ingredient_invalid_indexes(self,burger, sauce):
        burger.add_ingredient(sauce)

        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)

    @allure.title("Нельзя получить цену burger без булочки")
    def test_get_price_without_bun_raises_error(self, burger):
        # Act / Assert
        with pytest.raises(AttributeError):
            burger.get_price()

    @allure.title("Нельзя получить рецепт burger без булочки")
    def test_get_receipt_without_bun_raises_error(self, burger):
        # Act / Assert
        with pytest.raises(AttributeError):
            burger.get_receipt()



import pytest
from unittest.mock import Mock

from ..burger import Burger


class TestBurger:
    def test_init_bun_true(self, burger_instance):
        assert burger_instance.bun is None

    def test_init_ingredients_list_true(self, burger_instance):
        assert burger_instance.ingredients == []
        assert isinstance(burger_instance.ingredients, list)

    def test_set_buns_success(self, burger_instance, bun_instance):
        bun_instance.name = 'Кислая булочка'
        bun_instance.price = 80.50
        burger_instance.set_buns(bun_instance)
        assert burger_instance.bun == bun_instance
        assert burger_instance.bun.name == 'Кислая булочка'
        assert burger_instance.bun.price == 80.50

    @pytest.mark.parametrize("new_ingredients", [
        [],
        ['Соус Spicy-X'],
        ['Соус Spicy-X', 'Говяжий метеорит', 'Соус традиционный галактический']
    ])
    def test_add_ingredient_not_empty_list(self, new_ingredients, burger_instance):
        burger_instance.ingredients = new_ingredients
        assert len(burger_instance.ingredients) == len(new_ingredients)

    def test_remove_ingredient_delete_ingredient(self):
        mock_ingredients = Mock()
        mock_ingredients.ingredients = ['Соус Spicy-X', 'Говяжий метеорит', 'Соус традиционный галактический']
        new_burger = Burger()
        new_burger.ingredients = mock_ingredients.ingredients
        initial_count = len(new_burger.ingredients)
        new_burger.remove_ingredient(1)
        assert len(new_burger.ingredients) == initial_count - 1
        assert 'Говяжий метеорит' not in new_burger.ingredients

    def test_move_ingredient_move_done(self, burger_instance):
        mock_ingredients = Mock()
        mock_ingredients.ingredients = ['Соус Spicy-X', 'Говяжий метеорит', 'Соус традиционный галактический']
        new_burger = burger_instance
        new_burger.ingredients = mock_ingredients.ingredients
        new_burger.move_ingredient(0, 2)
        assert new_burger.ingredients[-1] == 'Соус Spicy-X'

    def test_get_price_correct_price(self, burger_instance):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 20.0

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 30.0

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = 120.0

        mock_ingredient_3 = Mock()
        mock_ingredient_3.get_price.return_value = 40.0

        new_burger = burger_instance
        new_burger.bun = mock_bun
        new_burger.ingredients = [mock_ingredient_1, mock_ingredient_2, mock_ingredient_3]
        total_price = new_burger.get_price()
        expected_price = ((mock_bun.get_price() * 2) + mock_ingredient_1.get_price() + mock_ingredient_2.get_price() +
                          mock_ingredient_3.get_price())
        assert total_price == expected_price

    def test_get_receipt_correct_receipt(self, burger_instance):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Кислая булочка"
        mock_bun.get_price.return_value = 20.0

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_type.return_value = "Соусы"
        mock_ingredient_1.get_name.return_value = "Соус Spicy-X"
        mock_ingredient_1.get_price.return_value = 30.0

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_type.return_value = "Начинки"
        mock_ingredient_2.get_name.return_value = "Говяжий метеорит"
        mock_ingredient_2.get_price.return_value = 120.0

        burger_instance.bun = mock_bun
        burger_instance.ingredients = [mock_ingredient_1, mock_ingredient_2]
        receipt = burger_instance.get_receipt()
        expected_receipt = (
            "(==== Кислая булочка ====)\n"
            "= соусы Соус Spicy-X =\n"
            "= начинки Говяжий метеорит =\n"
            "(==== Кислая булочка ====)\n\n"
            f"Price: {burger_instance.get_price()}"
        )
        assert receipt == expected_receipt

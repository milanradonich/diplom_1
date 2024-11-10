class TestIngredient:
    def test_type_of_ingredient_set_success(self, ingredient_instance):
        ingredient_instance.type = 'Соусы'
        assert ingredient_instance.type == 'Соусы'

    def test_name_of_ingredient_set_success(self, ingredient_instance):
        ingredient_instance.name = 'Соус фирменный Space Sauce'
        assert ingredient_instance.name == 'Соус фирменный Space Sauce'

    def test_price_of_ingredient_set_success(self, ingredient_instance):
        ingredient_instance.price = 80.0
        assert ingredient_instance.price == 80.0

    def test_get_price(self, ingredient_instance):
        assert ingredient_instance.get_price() == 80.0

    def test_get_name(self, ingredient_instance):
        assert ingredient_instance.get_name() == 'Соус фирменный Space Sauce'

    def test_get_type(self, ingredient_instance):
        assert ingredient_instance.type == 'Соусы'

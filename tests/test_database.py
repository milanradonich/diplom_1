class TestDatabase:
    def test_init_bun_list(self, database_instance):
        assert len(database_instance.buns) > 0
        assert isinstance(database_instance.buns, list)

    def test_init_ingredients_list(self, database_instance):
        assert len(database_instance.ingredients) > 0
        assert isinstance(database_instance.ingredients, list)




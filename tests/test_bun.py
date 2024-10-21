class TestBunModel:

    def test_name_of_bun_set_success(self, bun_instance):
        bun_instance.name = 'Флюоресцентная булка R2-D3'
        assert bun_instance.name == 'Флюоресцентная булка R2-D3'

    def test_price_of_bun_set_success(self, bun_instance):
        bun_instance.price = 100
        assert bun_instance.price == 100

    def test_get_name_bun_get_name(self, bun_instance):
        assert bun_instance.get_name() == 'Вкусная булочка'

    def test_get_price_bun_get_price(self, bun_instance):
        assert bun_instance.get_price() == 100.50





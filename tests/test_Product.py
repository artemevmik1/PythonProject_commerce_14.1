def test_product(sample_product):
    assert sample_product.name == "Тестовый товар"
    assert sample_product.description == "Тестовое описание"
    assert sample_product.price == 1000.00
    assert sample_product.quantity == 10

from src.Product import Product


def test_product(sample_product):
    """Создание тестового продукта"""
    assert sample_product.name == "Ноутбук"
    assert sample_product.description == "Мощный игровой ноутбук"
    assert sample_product.price == 150000.5
    assert sample_product.quantity == 5


def test_product_with_zero_quantity():
    """Создание продукта с нулевым количеством"""
    product = Product("Телефон", "Смартфон", 50000.00, 0)

    assert product.name == "Телефон"
    assert product.quantity == 0


def test_product_with_negative_price():
    """Создание продукта с отрицательной ценой"""
    product = Product("Товар", "Описание", -100.00, 10)

    # Проверяем, что отрицательная цена сохраняется
    # (если валидации нет, то это ожидаемое поведение)
    assert product.price == -100.00


def test_product_with_float_price():
    """Создание продукта с дробной ценой"""
    product = Product("Товар", "Описание", 99.99, 10)

    assert isinstance(product.price, float)
    assert product.price == 99.99


def test_product_with_int_price():
    """Создание продукта с целой ценой"""
    product = Product("Товар", "Описание", 100, 10)

    assert product.price == 100


def test_product_with_empty_description():
    """Тест 6: Создание продукта с пустым описанием"""
    product = Product("Товар", "", 1000.00, 3)

    assert product.name == "Товар"
    assert product.description == ""

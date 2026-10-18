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


def test_product_creation(product_data):
    p = Product.new_product(product_data)
    assert p.name == "Смартфон"
    assert p.description == "Флагман"
    assert p.price == 80
    assert p.quantity == 15


def test_price_getter(product):
    assert product.price == 80

def test_price_setter_valid(product):
    product.price = 100
    assert product.price == 100


def test_price_setter_negative(product, capsys):
    product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 80


def test_new_product_without_list(product_data):
    p = Product.new_product(product_data)
    assert isinstance(p, Product)
    assert p.name == "Смартфон"



def test_new_product_no_duplicates(product_data):
    products = []
    p1 = Product.new_product(
        {"name": "Смартфон", "description": "Флагман", "price": 80, "quantity": 15},
        products,
    )
    products.append(p1)

    p2 = Product.new_product(
        {"name": "Наушники", "description": "Беспроводные", "price": 199, "quantity": 25},
        products,
    )

    assert p1 is not p2
    assert len(products) == 1



def test_str_format(sample_product):
    """Строка содержит имя, цену и остаток в нужном формате."""
    assert str(sample_product) == "Ноутбук, 150000.5 руб. Остаток: 5 шт."


def test_add_returns_number(sample_product, smartphone_product):
    """Результат сложения"""
    result = sample_product + smartphone_product
    assert isinstance(result, (int, float))
    assert not isinstance(result, Product)


def test_add_is_commutative(sample_product, smartphone_product):
    assert sample_product + smartphone_product == 1650002.5
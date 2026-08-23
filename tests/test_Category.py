import pytest
from src.Category import Category
from src.Product import Product



def test_category(first_category, second_category):
    assert first_category.name == "Чайники"
    assert second_category.description == "Многофункциональные духовые шкафы"
    assert len(second_category.products) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_creation_without_products(reset_counters):
    """Тест 2: Создание категории без продуктов"""
    category = Category("Книги", "Художественная литература")

    assert category.name == "Книги"
    assert category.description == "Художественная литература"
    assert len(category.products) == 0
    assert category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_creation_with_empty_list(reset_counters):
    """Тест 3: Создание категории с пустым списком продуктов"""
    category = Category("Игрушки", "Детские игрушки", [])

    assert category.name == "Игрушки"
    assert len(category.products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_count_increment(reset_counters):
    """Тест 4: Проверка увеличения счетчика категорий"""
    Category.category_count = 0

    category1 = Category("Категория 1", "Описание 1")
    category2 = Category("Категория 2", "Описание 2")
    category3 = Category("Категория 3", "Описание 3")

    assert Category.category_count == 3


def test_product_count_increment(reset_counters):
    """Тест 5: Проверка увеличения счетчика продуктов"""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Товар 1", "Описание 1", 100, 5)
    product2 = Product("Товар 2", "Описание 2", 200, 3)
    product3 = Product("Товар 3", "Описание 3", 300, 2)

    category = Category("Категория", "Описание", [product1, product2, product3])

    assert Category.product_count == 3


def test_product_count_with_empty_category(reset_counters):
    """Тест 6: Проверка счетчика продуктов при пустой категории"""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Пустая категория", "Без продуктов")

    assert Category.product_count == 0


def test_product_count_with_multiple_categories(reset_counters):
    """Тест 7: Проверка счетчика продуктов с несколькими категориями"""
    Category.category_count = 0
    Category.product_count = 0

    products1 = [Product("Товар 1", "", 100, 1), Product("Товар 2", "", 200, 1)]
    products2 = [Product("Товар 3", "", 300, 1)]

    category1 = Category("Категория 1", "Описание 1", products1)
    category2 = Category("Категория 2", "Описание 2", products2)

    assert Category.product_count == 3


def test_category_count_and_product_count_independence(reset_counters):
    """Тест 8: Проверка независимости счетчиков"""
    Category.category_count = 0
    Category.product_count = 0


    product = Product("Товар", "Описание", 100, 1)
    category = Category("Категория", "Описание", [product])

    assert Category.category_count == 1
    assert Category.product_count == 1

    # Создаем еще одну категорию без продуктов
    category2 = Category("Категория 2", "Описание 2")

    assert Category.category_count == 2
    assert Category.product_count == 1


def test_category_counters_reset(reset_counters):
    """Тест 12: Проверка сброса счетчиков"""
    Category.category_count = 0
    Category.product_count = 0

    assert Category.category_count == 0
    assert Category.product_count == 0

    category = Category("Категория", "Описание")
    assert Category.category_count == 1


def test_category_products_are_objects(reset_counters):
    """Тест 13: Проверка что продукты являются объектами Product"""
    product = Product("Товар", "Описание", 100.0, 5)
    category = Category("Категория", "Описание", [product])

    assert isinstance(category.products[0], Product)
    assert category.products[0].name == "Товар"
import pytest

from src.Category import Category
from src.Product import Product
from src.utils import creat_objects_from_json


@pytest.mark.parametrize("product_count", [0, 1, 3, 5, 10])
def test_create_objects_with_different_product_counts(product_count, reset_counters):
    """Тест 13: Создание категорий с разным количеством продуктов"""
    Category.category_count = 0
    Category.product_count = 0

    products = [
        {"name": f"Товар {i}", "description": f"Описание {i}", "price": 100.0 * i, "quantity": i}
        for i in range(1, product_count + 1)
    ]

    test_data = [{"name": "Категория", "description": "Описание категории", "products": products}]

    categories = creat_objects_from_json(test_data)

    assert len(categories[0].products) == product_count
    assert Category.product_count == product_count


@pytest.mark.parametrize("category_count", [1, 2, 3, 5])
def test_create_objects_with_multiple_categories(category_count, reset_counters):
    """Тест 14: Создание нескольких категорий"""
    Category.category_count = 0
    Category.product_count = 0

    test_data = []
    for i in range(category_count):
        test_data.append(
            {
                "name": f"Категория {i}",
                "description": f"Описание {i}",
                "products": [{"name": f"Товар {i}", "description": f"Описание {i}", "price": 100.0, "quantity": 1}],
            }
        )


def test_with_sample_product(sample_product):
    """Тест: Использование фикстуры sample_product"""
    assert sample_product.name == "Ноутбук"
    assert sample_product.price == 150000.5


def test_with_sample_json(sample_json_data, reset_counters):
    """Тест: Использование фикстуры sample_json_data"""
    categories = creat_objects_from_json(sample_json_data)

    assert len(categories) == 1
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 2


def test_with_first_category(first_category):
    """Тест: Использование фикстуры first_category"""
    assert first_category.name == "Чайники"
    assert len(first_category.products) == 2


def test_with_second_category(second_category):
    """Тест: Использование фикстуры second_category"""
    assert second_category.name == "Духовой шкаф"
    assert len(second_category.products) == 3


@pytest.mark.parametrize("product_count", [0, 1, 3, 5])
def test_category_with_different_product_counts(product_count, reset_counters):
    """Тест 19: Создание категорий с разным количеством продуктов"""
    products = [Product(f"Товар {i}", f"Описание {i}", 100.0, i) for i in range(product_count)]

    category = Category("Категория", "Описание", products)

    assert len(category.products) == product_count
    assert Category.product_count == product_count


@pytest.mark.parametrize(
    "name, description",
    [
        ("Смартфоны", "Современные смартфоны"),
        ("Телевизоры", "Современные телевизоры"),
        ("Ноутбуки", "Мощные ноутбуки"),
    ],
)
def test_category_different_names(name, description, reset_counters):
    """Тест 20: Создание категорий с разными названиями"""
    category = Category(name, description)

    assert category.name == name
    assert category.description == description
    assert Category.category_count == 1


@pytest.mark.parametrize("product_count", [1, 2, 3])
def test_category_product_count_multiple_categories(product_count, reset_counters):
    """Тест 21: Проверка счетчика продуктов с параметризацией"""
    categories = []
    total_products = 0

    for i in range(product_count):
        products = [Product("Товар", "Описание", 100.0, 1) for j in range(i + 1)]
        total_products += len(products)
        category = Category(f"Категория {i}", f"Описание {i}", products)
        categories.append(category)

    assert len(categories) == product_count
    assert Category.product_count == total_products


def test_category_with_none_name(reset_counters):
    """Тест 22: Создание категории с None в названии"""
    category = Category(None, "Описание")

    assert category.name is None
    assert category.description == "Описание"
    assert len(category.products) == 0


def test_category_with_none_description(reset_counters):
    """Тест 23: Создание категории с None в описании"""
    category = Category("Категория", None)

    assert category.name == "Категория"
    assert category.description is None
    assert len(category.products) == 0


def test_category_with_empty_name(reset_counters):
    """Тест 24: Создание категории с пустым названием"""
    category = Category("", "Описание")

    assert category.name == ""
    assert category.description == "Описание"


def test_category_product_count_with_mixed_types(reset_counters):
    """Тест 25: Проверка обработки разных типов в списке продуктов"""
    products = [
        Product("Товар 1", "Описание 1", 100.0, 1),
        Product("Товар 2", "Описание 2", 200.0, 2),
    ]

    category = Category("Категория", "Описание", products)

    assert len(category.products) == 2
    assert all(isinstance(p, Product) for p in category.products)

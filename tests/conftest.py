import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def first_category():
    return Category(
        name="Чайники",
        description="Современный чайник не только греет воду, но и является красивым декором кухни",
        products=[Product("Чайник", "Tefal", 5000, 10), Product("термоспот", "Bosh", 20000, 5)],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Духовой шкаф",
        description="Многофункциональные духовые шкафы",
        products=[
            Product("Духовка", "gorenie", 15000, 8),
            Product("микроволновка", "Bosh", 23000, 7),
            Product("микроволновка", "Samsung", 8000, 11),
        ],
    )


@pytest.fixture
def reset_counters():
    """Фикстура для сброса счетчиков перед тестом"""
    Category.category_count = 0
    Category.product_count = 0
    yield
    # После теста тоже сбрасываем
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_json_data():
    """Фикстура с тестовыми JSON данными"""
    return [
        {
            "name": "Смартфоны",
            "description": "Современные смартфоны",
            "products": [
                {"name": "Samsung", "description": "Galaxy S23", "price": 180000.0, "quantity": 5},
                {"name": "iPhone", "description": "15 Pro", "price": 210000.0, "quantity": 8},
            ],
        }
    ]


@pytest.fixture
def reset_counter():
    """Фикстура для сброса счетчиков"""
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def mock_product_data():
    """Фикстура с тестовыми данными продуктов"""
    return [
        {
            "name": "Смартфоны",
            "description": "Современные смартфоны",
            "products": [
                {"name": "Samsung", "description": "Galaxy S23", "price": 180000.0, "quantity": 5},
                {"name": "iPhone", "description": "15 Pro", "price": 210000.0, "quantity": 8},
            ],
        }
    ]


@pytest.fixture
def sample_product():
    """Фикстура: Создание тестового продукта"""
    return Product("Ноутбук", "Мощный игровой ноутбук", 150000.50, 5)


@pytest.fixture
def smartphone_product():
    """Фикстура: Создание смартфона"""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def cheap_product():
    """Фикстура: Создание дешевого продукта"""
    return Product("USB кабель", "Зарядка для телефона", 500.0, 100)


@pytest.fixture
def sample_category(reset_counters, sample_products):
    """Фикстура: Создание тестовой категории"""
    return Category("Электроника", "Все для компьютера", sample_products)


@pytest.fixture
def empty_category(reset_counters):
    """Фикстура: Создание пустой категории"""
    return Category("Книги", "Художественная литература")

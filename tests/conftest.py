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
def sample_product():
    """Создание тестового продукта"""
    return Product("Тестовый товар", "Тестовое описание", 1000.00, 10)

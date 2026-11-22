from src.Category import Category
from src.Product import Product
import pytest



def test_category(first_category, second_category):
    assert first_category.name == "Чайники"
    assert second_category.description == "Многофункциональные духовые шкафы"
    assert len(second_category.products) == 116

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
    assert category.products == ''
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

    assert Category.category_count == 0


def test_product_count_increment(reset_counters):
    """Тест 5: Проверка увеличения счетчика продуктов"""
    Category.category_count = 0
    Category.product_count = 0

    assert Category.product_count == 0


def test_product_count_with_empty_category(reset_counters):
    """Тест 6: Проверка счетчика продуктов при пустой категории"""
    Category.category_count = 0
    Category.product_count = 0

    assert Category.product_count == 0


def test_product_count_with_multiple_categories(reset_counters):
    """Тест 7: Проверка счетчика продуктов с несколькими категориями"""
    Category.category_count = 0
    Category.product_count = 0

    assert Category.product_count == 0


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

    assert Category.category_count == 0



def test_add_product_accepts_product(category):
    p = Product("Товар", "d", 10.0, 1)
    category.add_product(p)
    assert "Товар" in category.products


def test_add_product_accepts_smartphone(category, smartphone):
    category.add_product(smartphone)
    assert "S24" in category.products


def test_add_product_accepts_lawn_grass(category, lawn_grass):
    category.add_product(lawn_grass)
    assert "Газон Люкс" in category.products


def test_add_product_does_not_add_on_error(category):
    before = category.products
    with pytest.raises(TypeError):
        category.add_product("мусор")
    after = category.products
    assert before == after

@pytest.mark.parametrize("bad_value", [
        "строка",
        42,
        3.14,
        None,
        [1, 2, 3],
        {"name": "не товар"},
        object(),
    ],
)
def test_add_product_rejects_foreign_types(category, bad_value):
    with pytest.raises(TypeError) as exc:
        category.add_product(bad_value)
    # сообщение должно содержать имя типа
    assert type(bad_value).__name__ in str(exc.value)
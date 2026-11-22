import pytest

from src.Category import Category
from src.Product import Product
from src.Smartphone import Smartphone



def test_smartphone_is_product(smartphone):
    assert isinstance(smartphone, Product)
    assert isinstance(smartphone, Smartphone)


def test_smartphone_extra_fields(smartphone):
    assert smartphone.efficiency == "высокая"
    assert smartphone.model == "S24"
    assert smartphone.memory == 256
    assert smartphone.color == "чёрный"
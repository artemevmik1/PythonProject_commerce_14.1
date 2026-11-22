import pytest

from src.Category import Category
from src.Product import Product
from src.LawnGrass import LawnGrass



def test_lawn_grass_is_product(lawn_grass):
    assert isinstance(lawn_grass, Product)
    assert isinstance(lawn_grass, LawnGrass)



def test_lawn_grass_extra_fields(lawn_grass):
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7–14 дней"
    assert lawn_grass.color == "зелёный"
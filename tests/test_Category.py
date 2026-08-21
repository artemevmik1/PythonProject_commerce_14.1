def test_category(first_category, second_category):
    assert first_category.name == "Чайники"
    assert second_category.description == "Многофункциональные духовые шкафы"
    assert len(second_category.products) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5

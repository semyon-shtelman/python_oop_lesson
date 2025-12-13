def test_category_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert isinstance(category_1.products, str)

    assert category_2.name == "Телевизоры"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert isinstance(category_2.products, str)

    assert category_1.category_count == 2
    assert category_1.product_count == 4

def test_category_getter(category_1, product_4):
    expected = ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
                "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
                "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n")
    assert category_1.products == expected

    expected_2 = expected + "55\" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"
    category_1.add_product(product_4)
    assert category_1.products == expected_2


def test_category_add_product(category_1, product_4):
    category_1.product_count = 3
    category_1.add_product(product_4)
    assert category_1.product_count == 4

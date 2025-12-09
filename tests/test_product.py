import pytest
from src.product import Product

@pytest.mark.parametrize(
    "product_fixture,expected_data",
    [
        (
            "product_1",
            {
                "name": "Samsung Galaxy S23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
        ),
        (
            "product_2",
            {
                "name": "Iphone 15",
                "description": "512GB, Gray space",
                "price": 210000.0,
                "quantity": 8,
            },
        ),
        (
            "product_3",
            {
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000.0,
                "quantity": 14,
            },
        ),
    ],
)
def test_product_init(request, product_fixture, expected_data):
    product = request.getfixturevalue(product_fixture)
    assert product.name == expected_data["name"]
    assert product.description == expected_data["description"]
    assert product.price == expected_data["price"]
    assert product.quantity == expected_data["quantity"]

def test_product_new_product(new_product):

    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5

def test_product_price(capsys,new_product):
    new_product.price = 800
    message = capsys.readouterr()
    assert message.out.strip() == ""
    assert new_product.price == 800

    new_product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    assert new_product.price == 800

    new_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    assert new_product.price == 800
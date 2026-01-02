import pytest

from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


def test_product_price(capsys, new_product):
    capsys.readouterr()
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


def test_product_str(product_1, product_2, product_3):
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product_2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product_3) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_product_add(product_1, product_2, product_3):
    assert product_1 + product_2 == 2580000.0
    assert product_1 + product_3 == 1334000.0
    assert product_2 + product_3 == 2114000.0


def test_product_addition(
    smartphone1: Smartphone,
    smartphone2: Smartphone,
    grass1: LawnGrass,
    grass2: LawnGrass,
):
    smartphone_sum = smartphone1 + smartphone2
    assert smartphone_sum == 2580000.0

    grass_sum = grass1 + grass2
    assert grass_sum == 16750.0

    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_product_zero_quantity():
    with pytest.raises(ValueError) as e:
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    assert str(e.value) == "Товар с нулевым количеством не может быть добавлен"

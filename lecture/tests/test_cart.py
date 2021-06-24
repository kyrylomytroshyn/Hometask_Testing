""" Cart module test cases """
from typing import List

import pytest

from lecture.shop.cart import Cart
from lecture.shop.products import Product

product1 = Product(
    product_id=1,
    title='Hello',
    price=10.0
)

product2 = Product(
    product_id=2,
    title='Hello2',
    price=100.0
)




@pytest.fixture()
def db():
    """ PRE TEST """
    # INITIALIZE DB. FRESH. SEED WITH OBJECT
    yield
    """ POST TEST """
    # CLEAN DB


def test_add_to_cart():
    cart = Cart()
    product = Product(
        product_id=1,
        title='Hello',
        price=10.0
    )

    cart.add_to_cart(product)

    assert [product] == cart.get_products()


@pytest.mark.parametrize(
    'product_to_add, product_to_remove, result',
    [
        (product2, product2, []),
        (product1, product2, [product1]),
    ]
)
def test_remove_product(
    cart: Cart,
    product_to_add: Product,
    product_to_remove: Product,
    result: List[Product]
):
    cart.add_to_cart(product_to_add)
    cart.remove_from_cart(product_to_remove)

    assert result == cart.get_products()

@pytest.mark.parametrize(
    'number',
    [
        '123456789012',
        '123456789011',
    ]
)
def test_number_valid(cart: Cart, number: str):
    assert cart.is_phone_number(number)


@pytest.mark.parametrize(
    'number',
    [
        '12345678901',
        '1234567890123',
        '1234567890A2',
        '1234567890#2',
    ]
)
def test_number_invalid(db, cart: Cart, number: str):
    assert not cart.is_phone_number(number)

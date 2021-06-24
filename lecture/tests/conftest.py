import pytest

from lecture.shop.cart import Cart


@pytest.fixture()
def cart() -> Cart:
    return Cart()


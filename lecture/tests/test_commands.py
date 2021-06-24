from unittest import mock

from lecture.shop.cart import Cart
from lecture.shop.products import Products, Product
from lecture.shop.commands import AddToCart, RemoveFromCart


class TestAddToCart:
    _cart = None
    _products = None
    _command: AddToCart = None

    def test_product_absent(self):
        self._prepare_env()
        self._products.by_id.return_value = None

        assert not self._command.execute(1)
        self._products.by_id.assert_called_once_with(1)
        self._cart.add_to_cart.assert_not_called()

    def test_product_present(self):
        self._prepare_env()
        product = mock.create_autospec(Product)
        self._products.by_id.return_value = product

        assert not self._command.execute(2)
        self._products.by_id.assert_called_once_with(2)
        self._cart.add_to_cart.assert_called_once_with(product)

    def _prepare_env(self) -> None:
        self._products = mock.create_autospec(Products)
        self._cart = mock.create_autospec(Cart)
        self._command = AddToCart(self._products, self._cart)


class TestRemoveFromCart:
    _products = None
    _cart = None
    _command = None

    def test_product_absent(self):
        self._prepare_env()
        self._products.by_id.return_value = None

        assert not self._command.remove(1)
        self._products.by_id.assert_called_once_with(1)
        self._cart.remove_from_cart.assert_not_called()

    def test_product_avoid(self):
        self._prepare_env()

        assert not self._command.remove(10)
        self._products.by_id.assert_not_called()
        self._cart.remove_from_cart.assert_not_called()

    def test_product_removed(self):
        self._prepare_env()
        product = mock.create_autospec(Product)
        self._products.by_id.return_value = product

        assert self._command.remove(2)
        self._products.by_id.assert_called_once_with(2)
        self._cart.remove_from_cart.assert_called_once_with(product)

    def _prepare_env(self) -> None:
        self._cart = mock.create_autospec(Cart)
        self._products = mock.create_autospec(Products)
        self._command = RemoveFromCart(self._cart, self._products)

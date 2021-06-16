""" Cart module """
from typing import List


from .products import Product


class Cart:
    def __init__(self):
        self._products: List[Product] = []

    def add_to_cart(self, product: Product) -> None:
        self._products.append(product)

    def remove_from_cart(self, product: Product) -> None:
        self._products.remove(product)

    def get_products(self) -> List[Product]:
        return self._products

    def clear(self) -> None:
        self._products = []

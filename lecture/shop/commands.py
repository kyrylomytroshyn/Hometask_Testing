""" Commands module """
from lecture.shop.cart import Cart
from lecture.shop.products import Products


class AddToCart:
    """ Command that add to cart """
    def __init__(self, products: Products, cart: Cart):
        self._products: Products = products
        self._cart: Cart = cart

    def execute(self, product_id: int) -> None:
        product = self._products.by_id(product_id)
        if product:
            self._cart.add_to_cart(product)


class ClearCart:
    """ Card clearing command """
    def __init__(self, cart: Cart):
        self._cart = cart

    def execute(self) -> None:
        self._cart.clear()


class RemoveFromCart:
    def __init__(self, cart: Cart, products: Products):
        self._cart: Cart = cart
        self._products: Products = products

    def remove(self, product_id: int) -> bool:
        if product_id % 10 == 0:
            return False
        product = self._products.by_id(product_id)
        if product:
            self._cart.remove_from_cart(product)
            return True
        return False

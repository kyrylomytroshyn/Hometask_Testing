""" Lecture about pytest  """
from lecture.shop.products import Products
from lecture.shop.cart import Cart
from lecture.shop.commands import AddToCart, RemoveFromCart, ClearCart


products = Products()
cart = Cart()

command = AddToCart(products, cart)
command.execute(product_id=1)

print(cart.get_products())


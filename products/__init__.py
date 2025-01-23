import json
import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])

def get_cart(username: str) -> list[Product]:
    """Retrieve the cart for a user and return a list of Product objects."""
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    products_list = []
    for cart_detail in cart_details:
        contents = json.loads(cart_detail['contents'])  # Safely parse JSON instead of eval
        for product_id in contents:
            product = products.get_product(product_id)
            if product:
                products_list.append(product)
   
    return products_list

def add_to_cart(username: str, product_id: int):
    """Add a product to the user's cart."""
    dao.add_to_cart(username, product_id)

def remove_from_cart(username: str, product_id: int):
    """Remove a product from the user's cart."""
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    """Delete the user's cart."""
    dao.delete_cart(username)

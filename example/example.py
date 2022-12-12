from typing import List, Tuple

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def in_stock(self) -> bool:
        return self.quantity > 0

class Cart:
    def __init__(self, product: Product):
        # pyreverse currently doesn't support List, Union type hints
        self.products = [product]

    def add_item(self, product: Product, quantity: int):
        self.product.append((product, quantity))

    def remove_item(self, product: Product):
        self.products = [item for item in self.items if item[0] != products]

    def total_price(self) -> float:
        return sum([item[0].price * item[1] for item in self.products])

class Customer:
    def __init__(self, name: str, email: str, address: str):
        self.name = name
        self.email = email
        self.address = address

class Order:
    def __init__(self, customer: Customer, cart: Cart):
        self.customer = customer
        self.cart = cart
        self.status = "pending"

    def complete(self) -> None:
        self.status = "completed"

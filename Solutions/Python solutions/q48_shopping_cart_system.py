class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.items)
        gst = total * 0.18

        print("Total:", total)
        print("GST:", gst)
        print("Final Amount:", total + gst)

cart = ShoppingCart()

cart.add_item(CartItem("Laptop", 50000, 1))
cart.add_item(CartItem("Mouse", 500, 2))

cart.calculate_total()
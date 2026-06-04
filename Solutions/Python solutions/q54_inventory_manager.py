class Product:

    def __init__(self, name):
        self.name = name

class Perishable(Product):
    pass

class Electronics(Product):
    pass

inventory = {
    "Milk": 3,
    "Laptop": 15,
    "Bread": 2
}

low_stock = {item for item, qty in inventory.items() if qty < 5}

print("Inventory Summary")

for item, qty in inventory.items():
    print(item, qty)

print("Low Stock Alerts:", low_stock)
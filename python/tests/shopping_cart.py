class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item(name: {self.name}, price: {self.price})"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def total_price(self):
        return sum(item.price for item in self.items)

    def list_items(self):
        return [str(item) for item in self.items]

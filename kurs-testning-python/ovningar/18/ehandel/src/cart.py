class ShoppingCart:
    DISCOUNT_CODES = {
        "RABATT10": 0.10,
        "RABATT20": 0.20,
    }

    def __init__(self):
        self.items = []
        self.discount = 0.0

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def remove_item(self, name):
        self.items = [item for item in self.items if item["name"] != name]

    def get_item_count(self):
        return len(self.items)

    def apply_discount(self, code):
        self.discount = self.DISCOUNT_CODES.get(code, 0.0)

    def get_total(self):
        subtotal = sum(item["price"] for item in self.items)
        return round(subtotal * (1 - self.discount), 2)

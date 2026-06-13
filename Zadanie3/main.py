class Product:
    def __init__(self, product_id, name, quantity):
        self._id = product_id
        self._name = name
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    def add_stock(self, amount):
        if amount > 0:
            self._quantity += amount

    def remove_stock(self, amount):
        if 0 < amount <= self._quantity:
            self._quantity -= amount

def main():
    mleko = Product(1, "melko", 1)
    mleko.add_stock(5)

    print(mleko._name)

if __name__ == '__main__':
    main()
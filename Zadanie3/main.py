from abc import ABC, abstractmethod

class Product(ABC):
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

    @abstractmethod
    def get_info(self):
        pass

class FoodProd(Product):
    def __init__(self, product_id, name, quantity, expiry_date):
        super().__init__(product_id, name, quantity)
        self.expiry_date = expiry_date

    def get_info(self):
        return f"Food: {self._name}, quantity: {self._quantity}, expiration date: {self.expiry_date}"

class Warehouse:
    def __init__(self, warehouse_id, name):
        self.id = warehouse_id
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(product.get_info())

def main():
    mleko = FoodProd(1, "melko", 1, "21.07.2026")
    mleko.add_stock(5)

    magazyn = Warehouse(0, "Magazyn jedzenia")
    magazyn.add_product(mleko)

    magazyn.show_products()

if __name__ == '__main__':
    main()
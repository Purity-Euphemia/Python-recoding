class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_price(self):
        print(self.name, "costs", self.price)


product1 = Product("Laptop", 500000)

product1.show_price()
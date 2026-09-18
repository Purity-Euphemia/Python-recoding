class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def start(self):
        print(self.brand, "laptop is starting")

laptop1 = Laptop("Dell", "16GB")
print(laptop1.brand)
print(laptop1.ram)
laptop1.start()
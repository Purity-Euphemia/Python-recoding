class Phone:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def call(self):
        print("Calling...")


phone1 = Phone("Samsung", "S24")

print(phone1.brand)
print(phone1.model)

phone1.call()
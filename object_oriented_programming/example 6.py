class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print("The car is driving")


car1 = Car("Toyota", "Black")

print(car1.brand)
print(car1.color)

car1.drive()
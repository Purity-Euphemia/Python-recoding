class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def eat(self):
        print("I am eating", self.name)

food1 = Food("Pizza", 5000)

print(food1.name)
print(food1.price)
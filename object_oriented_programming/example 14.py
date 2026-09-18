class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def open_door(self):
        print("The door is open")

house1 = House("White", 4)

print(house1.color)
print(house1.rooms)
house1.open_door()
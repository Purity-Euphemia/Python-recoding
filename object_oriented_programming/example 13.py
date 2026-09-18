class Customer:
    def __init__(self, name, queue_number):
        self.name = name
        self.queue_number = queue_number

    def show_ticket(self):
        print(self.name, "has ticket", self.queue_number)

customer1 = Customer("Mary", "A101")
customer2 = Customer("John", "A102")
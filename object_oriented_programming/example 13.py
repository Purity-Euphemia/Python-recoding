class Customer:
    def __init__(self, name, queue_number):
        self.name = name
        self.queue_number = queue_number

    def show_ticket(self):
        print(self.name, "has ticket", self.queue_number)
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount


account1 = BankAccount("Mary", 1000)

print(account1.balance)

account1.deposit(500)

print(account1.balance)
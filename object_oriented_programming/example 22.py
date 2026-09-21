class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Money withdrawn")
        else:
            print("Not enough money")

account1 = BankAccount("Mary", 10000)

account1.withdraw(3000)

print(account1.balance)


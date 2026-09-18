class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful")
        else:
            print("Not enough balance")
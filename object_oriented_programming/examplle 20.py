class Wallet:

    def __init__(self, money):
        self.money = money

    def add_money(self, amount):
        self.money = self.money + amount

    def spend_money(self, amount):
        self.money = self.money - amount 

wallet = Wallet(5000)

print(wallet.money)

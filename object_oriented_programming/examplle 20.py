class Wallet:

    def __init__(self, money):
        self.money = money

    def add_money(self, amount):
        self.money = self.money + amount

    def spend_money(self, amount):
        self.money = self.money - amount 

wallet1 = Wallet(5000)

print(wallet1.money)

wallet1.add_money(2000)

print(wallet1.money)

wallet1.spend_money(1000)

print(wallet1.money)

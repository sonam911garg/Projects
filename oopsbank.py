import json
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount1):
        self.balance -= amount1
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def interest(self, interest):
        self.balance *= interest
        return self.balance

x = SavingsAccount(500)
x.deposit(200)
x.withdraw(100)
x.interest(1.05)
print(x.balance)

with open("bank.json", "w") as f:
    json.dump({"balance": x.balance}, f)
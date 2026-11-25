class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings account gives interest")


class CurrentAccount(BankAccount):
    def overdraft(self):
        print("Current account allows overdraft")


savings = SavingsAccount("Isha", 10000)
current = CurrentAccount("Megha", 15000)

savings.show_balance()
savings.interest()

current.show_balance()
current.overdraft()
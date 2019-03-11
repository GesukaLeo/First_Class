class BankAccount:
    def __init__(self):
        self.balance  = 0

    def withdraw(self,amount):
        self.balance -=amount
        return self.balance

    def deposit(self,amount):
        self.balance +=amount
        return self.balance

personal = BankAccount()
personal.balance= 1000
print(personal.deposit(200))

class Account:
    def __init__(self,money,deposit1,withdraw1):
        self.money = money
        self.deposit1 = deposit1
        self.withdraw1 = withdraw1
    def deposit(self):
        print('After deposit:',self.money + self.deposit1)
    def withdraw(self):
        print('After withdraw:',self.money - self.withdraw1)


obj1 = Account(10000,3000,7000)
obj1.deposit()
obj1.withdraw()

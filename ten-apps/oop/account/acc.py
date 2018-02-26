class Account:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.file_path, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    def __init__(self, file_path, fee):
        Account.__init__(self, file_path)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


checking = Checking('balance.txt', 2)
checking.deposit(10)
print(checking.balance)
checking.transfer(110)
print(checking.balance)
checking.commit()
# account = Account('balance.txt')
# print(account.balance)
# account.deposit(200)
# print(account.balance)
# account.commit()

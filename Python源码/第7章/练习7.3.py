class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("余额不足")
        else:
            self.balance -= amount
            return self.balance

    def check_balance(self):
        print(f"当前余额是 {self.balance}")

# 创建 BankAccount 对象
account = BankAccount()

# 存款
account.deposit(1000)

# 取款
account.withdraw(500)

# 取款超过余额
account.withdraw(700)

# 查看余额
account.check_balance()


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


class AdvancedCalculator(Calculator):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("除数不能为0")
        else:
            return a / b


ac = AdvancedCalculator()
print(ac.add(5, 2))  # 输出7
print(ac.subtract(5, 2))  # 输出3
print(ac.multiply(5, 2))  # 输出10
print(ac.divide(10, 2))  # 输出5
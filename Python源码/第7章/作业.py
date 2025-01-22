class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def run(self):
        self.weight -= 2

    def eat(self):
        self.weight += 1

    def show(self):
        print(f'Height: {self.height}, Weight: {self.weight}')

class Student(Person):
    def __init__(self, height, weight, major):
        super().__init__(height, weight)
        self.major = major

    def eat(self):
        self.weight += 2
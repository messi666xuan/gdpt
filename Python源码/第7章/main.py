class Person:

    def __init__(self,height,weight):
        self.height = height
        self.weight = weight
        print(f"初始身高是{self.height},初始体重是{self.weight}")
    def run(self):
        self.weight = self.weight - 2
    def eat(self):
        self.weight = self.weight + 1
    def show(self):
        print(f"运动过后体重为{self.weight}")
        print(f"进食过后体重为{self.weight}")

class Student(Person):
    def __init__(self,height,weight,major):
        super().__init__(height,weight)
        self.major= major
    def eat(self):
        self.weight =self.weight - 2


P1=Person (150,100)
P1.run()
P1.eat()
P1.show()
S1=Student(160,120,"yingyu")
S1.eat()
S1.show()




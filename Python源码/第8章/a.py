def greet(name):
    print(f"Hello, {name}!")


class student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

    def sayhi(self):
        print(f"hello,我叫{self.name},今年{self.age}岁，学号是{self.id}")
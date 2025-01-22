# 创建Animal类
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "这个动物发出了声音"

# 创建Dog类，并继承Animal类
class Dog(Animal):
    def sound(self):
        return "汪汪"

# 创建Cat类，并继承Animal类
class Cat(Animal):
    def sound(self):
        return "喵喵"

# 创建Dog类和Cat类的实例
dog = Dog("柴犬")
cat = Cat("狸花")

# 打印出他们发出的声音
print(dog.sound())  # 输出: 汪汪
print(cat.sound())  # 输出: 喵喵
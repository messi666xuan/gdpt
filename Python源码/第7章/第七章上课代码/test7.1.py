class iphone11:
    brand="apple"
    def call4g(self):
        print("老版iphone11支持4g通话")

class iphone14(iphone11):
    def call4g(self):

        print("iphone14支持4g通话")

    def call5g(self):
        #super().call4g()
        print("iphone14支持5g通话")

# a14=iphone14()
# a14.call5g()

class job:
    def __init__(self,id,salary):
        self.id=id
        self.salary=salary
    def show(self):
        print(f"工号：{self.id},工资：{self.salary}")
class teacher(job):
    major="计算机"
# t1=teacher(10001,8000)
# t1.show()


# 创建一个 Animal 父类
class Animal:
    def sound(self):
        print("这是动物的声音")
# 创建一个 Dog 子类，继承 Animal 父类
class Dog(Animal):
    def sound(self):
        super().sound()  # 使用 super() 调用父类的 sound 方法
        #Animal.sound(self)
        print("汪汪！")  # 子类 Dog 自己的 sound 方法


# my_dog = Dog()
# my_dog.sound()

# 输出：
# 这是动物的声音
# 汪汪！











# 创建一个名为Animal的类，其中有一个叫做name、number的属性和一个叫做sound的方法。sound方法打印一个字符串“动物叫声”。
# 创建一个名为Dog的类，继承Animal类。在Dog类中重写sound方法，让其打印字符串 "汪汪"。
# 然后创建了Dog类和Cat类的实例，并打印出它们发出的声音。
class Animal:
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def sound(self):
        print("动物叫声")

class dog(Animal):
    def __init__(self,name,number,age):
        super().__init__(name,number) #调用父类的构造方法把从父类继承来的属性先初始化
        self.age=age

    def sound(self):
        super().sound()   #调用父类的sound方法
        print(f"{self.name}汪汪,今年{self.age}岁,一共{self.number}只")

# d=dog("哈士奇",50,10)
# d.sound()



# 创建一个基类 Job ,该类具有属性 salary （薪水）和一个方法 service 用于打印 "正在提供服务"。
# 基于 Job类，创建两个子类，一个是 Teacher（教师）类，一个是 Doctor （医生）类。
# Teacher 类除继承了 Job 的属性和方法外，还有一项自己的属性lesson（即课程），以及一个名为 teach 的方法，当调用该方法时，打印 "正在上xx课 " 的信息。
# Doctor 类除继承了 Job 类的属性和方法外，还有一项自己的属性 department （科室），以及一个名为 treat （治疗）的方法，当调用该方法时，打印 "正在给病人治疗" 的信息。
class Job:
    def __init__(self,salary):
        self.salary=salary
    def service(self):
        print("正在提供服务")

class Teacher(Job):
    def __init__(self,salary,lesson):
        super().__init__(salary)  #super()=父类名
        self.lesson=lesson
    def teach(self):
        self.service()
        print(f"正在上{self.lesson}课")

class Doctor(Job):
    def __init__(self,salary,department):
        super().__init__(salary)  #super()=父类名
        self.department=department
    def treat(self):
        self.service()
        print(f"正在{self.department}给病人治疗")
#
# t1=Teacher(10000,"python")
# t1.teach()
# d1=Doctor(20000,"精神科")
# d1.treat()



# 创建一个名为"Calculator(计算器)"的基类，并定义两个方法：add(加法)，subtract(减法)，分别实现两个数的加、减运算。
# 创建一个名为"AdvancedCalculator(高级计算器)"的子类，该类继承"Calculator"类，并额外定义两个方法：multiply(乘法)和divide(除法)，分别实现两个数的乘、除运算。
# 请你完成以下任务：
# 创建这两个类（包括它们的方法）。
# 创建一个AdvancedCalculator的实例。
# 用这个实例进行加、减、乘、除的运算，并打印出结果。
class Calculator:
    def add(self,a,b):
        print(f"{a}+{b}的结果为{a+b}")
        return a+b
    def subtract(self,a,b):
        print(f"{a}-{b}的结果为{a - b}")
        return a - b
class AdvancedCalculator(Calculator):
    def multiply(self,a,b):
        print(f"{a}*{b}的结果为{a*b}")
        return a*b
    def divide(self,a,b):
        if b==0:
            print("除数不能为0")
        else:
            print(f"{a}/{b}的结果为{a / b}")

# ac=AdvancedCalculator()
# ac.add(3,6)
# ac.multiply(3,6)
# ac.divide(6,0)
# ac.divide(6,3)


# 请创建一个父类 Vehicle (交通工具)和两个子类 Car （汽车）和 Bicycle（自行车）。
# 父类要有一个方法 travel ，打印 "开始旅行"。
# 两个子类除了要重写父类的 travel 方法，还要先调用父类定义的 travel 方法（使用 super() 调用）。
# 当你分别调用 Car 和 Bicycle 的 travel 方法时，它们会先输出 "开始旅行"，然后输出各自的指定语句（如 "开车出发" 和 "骑自行车出发"）。
class Vehicle:
    def travel(self):
        print("开始旅行")
class Car(Vehicle):
    def travel(self):
        super().travel()
        print("开车出发")
class Bicycle(Vehicle):
    def travel(self):
        super().travel()
        print("骑自行车出发")
# c1=Car()
# c1.travel()
# b1=Bicycle()
# b1.travel()


class Math:
    def __init__(self,math_score):
        self.math_score=math_score

class English:
    def __init__(self,english_score):
        self.english_score=english_score

class student(Math,English):
    def __init__(self,name,math_score,english_score):
        Math.__init__(self,math_score)
        English.__init__(self,english_score)
        self.name=name
    def show(self):
        print(f"姓名：{self.name},数学成绩：{self.math_score},英语成绩：{self.english_score}")

# s1=student("周杰伦",80,50)
# s1.show()

















#创建一个名为 Classroom 的类，在这个类中：
# 初始化一个空字典，用于存储学生学号和对应的姓名
# 定义一个 add_student 方法，用于添加新的学生   添加：字典名[键名]=值
# 输入：学号、姓名
# 定义一个 delete_student 方法，用于删除已有的学生  删除：字典名.pop(键名)
# 输入：学号
class classroom:
    def __init__(self):
        self.student={}
    def add_student(self):
        id=int(input("请输入添加的学生学号："))
        name = input("请输入添加的学生姓名：")
        self.student[id]=name  #添加：字典名[键名]=值
        print(f"成功添加学生：{self.student[id]}")
    def delete_student(self):
        id = int(input("请输入删除的学生学号："))
        self.student.pop(id)#删除：字典名.pop(键名)
        print(f"成功删除学号为{id}的学生")
    def show(self):
        for i in self.student.keys():
            print(f"姓名：{self.student[i]},学号：{i}")
c1=classroom()
c1.add_student()
c1.add_student()
c1.show()
print("------------------")
c1.delete_student()
c1.show()


def add(a,b):
    return  a+b



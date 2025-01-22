class student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

    def sayhi(self):
        print(f"hello,我叫{self.name},今年{self.age}岁，学号是{self.id}")

# s1=student("周杰伦",18,1001)
# s1.sayhi()
# s2=student("陈奕迅",58,1002)
# s2.sayhi()

class person:
    def __init__(self,name,sex,birthday,id,address):
        self.name=name
        self.sex=sex
        self.birthday=birthday
        self.id=id
        self.address=address

    def info(self):
        print(f"姓名：{self.name},性别：{self.sex},出生日期：{self.birthday},id:{self.id},地址：{self.address}")

# p1=person("樱木花道","男","2023",1564564,"佛山")
# p1.info()
# p2=person("陈奕迅","男","2000",1002,"香港")
# p2.info()
#ctrl+?
# 创建一个员工类，每个员工有姓名（name）、工号（id）和工资(salary)三个属性。
# 为该类添加一个构造函数，以初始化这些属性，并添加成员方法用于显示员工的信息
class worker:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def info(self):
        print(f"姓名：{self.name},id:{self.id},工资：{self.salary}")

# w1=worker("打工人",12156,500)
# w1.info()
#
#
#创建一个名为Circle的类，它有一个成员变量：半径r，
# 并有两个成员方法:一个计算圆的面积的area方法和一个计算圆的周长的perimeter方法。
class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        S=3.14*self.r*self.r
        print(f"面积：{S}")
    def perimeter(self):
        a=3.14*2*self.r
        print(f"周长：{a}")
# c1=circle(3)
# c1.area()
# c1.perimeter()
# c2=circle(10)
# c2.area()
# c2.perimeter()




# 1.创建一个名为BankAccount的类，在初始化时为其赋予一个balance（余额）属性，初始值为0，并创造这个构造函数.
# 2.在BankAccount类中定义一个名为deposit（存款）的方法，该方法接受一个金额作为参数，并将其添加到余额中。
# 3.定义另一个名为withdraw（取款）的方法，该方法也接受一个金额作为参数。如果要取款的金额大于余额，打印"余额不足"，否则从余额中扣除该金额。
# 4.定义一个名为check_balance（查看余额）的方法，打印出当前的余额。
# 最后，创建一个BankAccount对象，进行存款，取款，并查看余额的操作
class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self):
        money1=float(input("请输入你要存多少钱："))
        self.balance+=money1
        print(f"存款成功{money1}元")
        self.money()
    def withdraw(self):
        money2 = float(input("请输入你要取多少钱："))
        if money2>self.balance:
            print("余额不足")
        else:
            #self.balance=self.balance-money2
            self.balance-=money2
            print(f"取款成功{money2}元")
            self.money()
    #显示余额
    def money(self):
        print(f"当前余额:{self.balance}")
# b1=BankAccount()
# b1.money()
# b1.deposit()
# b1.withdraw()




# 创建一个名为Car的类来模拟一辆汽车。
# Car 类应该有两个属性： brand(品牌) 和 distance(总行驶距离)，他们都通过构造函数设置其初始值。
# 类中应包含一种名为 drive 的方法，该方法接受一段行驶距离作为参数，将此距离添加到总行驶距离上。
# 类中还应包含一种名为 show 的方法，此方法用于显示汽车的总行驶距离
class Car:
    def __init__(self,brand,distance):
        self.brand=brand
        self.distance=distance

    def drive(self,d):
        self.distance+=d
        #self.distance=self.distance+d
    def show(self):
        print(f"{self.brand}汽车总行驶距离{self.distance}km")
c1=Car("奔驰",500)
c1.drive(1000)
c1.show()
c2=Car("小米su7",200)
c2.drive(1000)
c2.drive(1000)
c2.show()











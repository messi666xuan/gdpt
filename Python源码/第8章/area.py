# 新建两个Python文件，在其中一个area.py文件中定义两个类，一个是 square类（正方形），有一个属性是边长。
# 定义构造方法和计算正方形的面积函数。另一个类是 circle类（圆），有一个属性半径r,定义构造方法和计算圆的面积函数来计算圆的面积。
# 在另一个Python文件中，用 import 语句导入 area.py 文件，创建两个类的对象并调用面积函数计算面积。
class square():
    def __init__(self,a):
        self.a=a
    def mianji(self):
        S=self.a*self.a
        print(S)

class circle():
    def __init__(self,r):
        self.r=r
    def mianji(self):
        S=3.14*self.r*self.r
        print(S)



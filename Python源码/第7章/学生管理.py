# 创建一个名为 Math 的类，它包含一个属性 math_score（数学成绩）。
# 创建一个名为 English 的类，它包含一个属性english_score（英语成绩）。
# 创建一个名为 Student 的子类，它同时继承了 Math 和 English 类，还包含自己的属性name和 computer_score（计算机成绩）。
# 三个类都需要定义输出各自的成绩的方法，其中学生类需要定义显示所有成绩的方法
class Math:
    def __init__(self,math_score):
        self.math_score=math_score
    def show(self):
        print(f"数学成绩：{self.math_score}")
class English:
    def __init__(self,english_score):
        self.english_score=english_score
    def show(self):
        print(f"英语成绩：{self.english_score}")
class student(Math,English):
    def __init__(self,name,math_score,english_score,computer_score):
        Math.__init__(self,math_score)
        English.__init__(self,english_score)
        self.name=name
        self.computer_score=computer_score
    def show(self):
        print(f"姓名：{self.name}\n数学成绩：{self.math_score}\n"
              f"英语成绩：{self.english_score}\n计算机成绩:{self.computer_score}")

s1=student("周杰伦",80,60,50)
s1.show()
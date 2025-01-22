"""
��ʾ��Ĺ��췽��?
"""
# ��ʾʹ�ù��췽���Գ�Ա�������и�ֵ?
# ���췽�������ƣ�__init__

class Student:

    def __init__(self, name, age ,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")

stu = Student("周杰伦", 31, "18500006666")
print(stu.name)
print(stu.age)
print(stu.tel)


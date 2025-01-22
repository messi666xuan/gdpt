class Student:
    def __init__(self, student_id, class_name, major, age):
        self.student_id = student_id
        self.class_name = class_name
        self.major = major
        self.age = age

    def print_info(self):
        print("学号:", self.student_id)
        print("班级:", self.class_name)
        print("专业:", self.major)
        print("年龄:", self.age)


# 创建一个学生对象
student1 = Student("2021001", "Python101", "计算机科学", 20)

# 调用打印信息方法
student1.print_info()

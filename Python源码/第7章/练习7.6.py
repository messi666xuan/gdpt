class Job:
    def __init__(self, salary):
        self.salary = salary

    def provide_service(self):
        print("正在提供服务")

class Teacher(Job):
    def __init__(self, salary, lesson):
        super().__init__(salary)
        self.lesson = lesson

    def teach(self):
        print("正在教授{}".format(self.lesson))

class Doctor(Job):
    def __init__(self, salary, department):
        super().__init__(salary)
        self.department = department

    def diagnose(self):
        print("正在给病人看病")

# 实例化子类并调用方法
teacher = Teacher(5000, '数学')
teacher.teach()
teacher.provide_service()


doctor = Doctor(8000, '内科')
doctor.diagnose()
doctor.provide_service()
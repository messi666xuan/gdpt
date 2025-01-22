# 创建一个Python自定义模块，模块名称为"operation"，
# 在其中定义四个运算函数，包括加法、减法、乘法、除法，每个操作都应该接受两个数字作为输入，并返回这两个数字的运算结果。
# 然后在另一个Python文件里导入operations模块，并调用这四个函数，实现加减乘除。

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a* b)
def divide(a,b):
    if b==0:
        print("除数不能为0")
    else:
        print(a/ b)




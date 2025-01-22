# 全局变量
number = 0

# 函数：增加全局计数器并返回增加后的值
def add_number():
    global number
    number += 1
    return number

# 测试
add_number()
print(number)
add_number()
print(number)
add_number()
print(number)

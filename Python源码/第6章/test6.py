def weather(date,temp,air):
    print("*" * 13)
    print(f"日期：{date}")
    print(f"温度：{temp}")
    print(f"空气状况：{air}")
    print("*" * 13)

#
# weather("3月28日","30-40","不好")
# weather(3.22,25.3,"很差")
# weather("3月21日",28,"很好")
#
def print1(school):
    print(f"欢迎报考{school}")

# print1("清华大学")
# print1("广职院")

def add(x,y):
    result=x+y
    return result
#
a=add(20,10)
print(a)


def connect(ip, port=3306):
    print(f"连接地址为：{ip}")
    print(f"连接端口号为：{port}")
    print("连接成功")


# connect("192.168.1.1")
# connect(ip="192.168.1.1",port=5000)









#1.编写一个函数 say_hello(name)，接受一个参数 name，然后打印出 "Hello, xxx!" 的问候语句。
# def say_hello(name):
#     print(f"hello,{name}，你吃饭了吗")
# say_hello("jyetutrey")
#
#2.编写一个函数 calculate_sum(numbers)，接受一个列表参数 numbers，并返回列表中所有数字的总和。
# def calculate_sum(numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     return sum
# #
# b=calculate_sum([1,2,3,4,5])
# print(b)
# list=[1,2,3,4,5,6,7,8,9,10]
# a=calculate_sum(list)
# print(a)

#3.编写一个函数，接受一个温度（摄氏度）作为参数，并根据温度返回一个描述天气的字符串
# （大于30度："炎热"、15-30度："舒适"、小于15度："寒冷"等）。
def abc(temp):
    if temp>30:
        weather="炎热"
    elif temp<=30 and temp>15:
        weather = "舒适"
    else:
        weather="寒冷"
    return weather

# str1=abc(5)
# print(str1)


#3.编写一个Python函数，键盘输入一个摄氏温度c作为参数，然后将其转换为华氏温度F并返回。F=9/5*C+32

# def temp(c):
#     f = 9 / 5 * c + 32
#     return f
#
# a=float(input("请输入摄氏度："))
# b=temp(a)
# print(b)



# def add(x):
#     y=x+1
#     return y
# a=add(6)
# print(a)




#4.编写一个Python函数，接受一个列表作为参数，返回一个新列表，其中只包含原列表中的奇数元素。
# 列表名.append(元素)

def abc(list1):
    list2=[]
    for i in list1:
        if i%2==1:
            list2.append(i)
    return list2

# list=[12,65,70,55,99,304,201]
# x=abc(list)#x=list2
# print(x)

#编写一个函数，参数是列表，找出给定列表中的第一个负数，并打印和返回其值。
# 如果列表中没有负数，则打印"未找到"。
def number(list):
    for i in list:
        if i<0:
            print(i)
            return i   #return语句可以终止函数的执行
    print("未找到负数")















#5.编写一个Python函数，接受一个列表作为参数，返回列表中的最大值。




# x=6
# def a():
#     global x #声明x在函数体内是全局变量
#     x=5
#     print(f"函数体内访问的结果{x}")
# a()
# print(f"函数体外访问的结果{x}")



#编写一个程序，找出给定列表中的第一个负数，并打印其值。如果列表中没有负数，则打印"未找到"。



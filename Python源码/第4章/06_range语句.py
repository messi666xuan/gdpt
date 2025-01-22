"""
演示Python中的range()语句的基本使用
"""

# range语法1 range(num)
# for x in range(10):
#     print(x)

# range 语法2 range(num1, num2)
# for x in range(5, 10):
#     # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间间隔是1
#     print(x)

# range 语法3 range(num1, num2, step)
# for x in range(5, 10, 2):
#     # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间的间隔是2
#     print(x)

















# 编写一个函数，根据用户输入的身高和体重，判断其体型。
# 如果身高超过180cm且体重超过80kg，则输出“你有点胖了”，
# 如果身高超过180cm但体重在80kg以下，则输出“你的体型还可以”，
# 如果身高在160cm到180cm之间且体重在60kg到80kg之间，则输出“你的身材很好”，
# # 其他情况输出“你需要关注健康”。
# def test(h,w):
#     if h>180 and w>80:
#         print("你有点胖了")
#     elif h>180 and w<=80:
#         print("你的体型还可以")
#     elif h>160 and h<180 and w>60 and w<80:
#         print("身材贼好")
#     else:
#         print("你需要关注健康")
# height=float(input("请输入身高（cm）:"))
# weight=float(input("请输入体重（kg）:"))
# test(height,weight)


#编写一个函数，参数是列表，找出给定列表中的第一个负数，并打印其值，停止循环（break）。
# 如果列表中没有负数，则打印"未找到"。
def test1(list):
    flag=True
    for i in list:
        if i<0:
            print(i)
            flag=False
            break
    if flag:
        print("未找到")
test1([1,2,3,5,6,8])







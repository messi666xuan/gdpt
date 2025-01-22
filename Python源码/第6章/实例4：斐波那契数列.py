"""
使用递归解决 斐波那契数列

"""


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


number = int(input('请输入一个正整数: '))
result = fib(number)
print("第%d个斐波那契数为：%d" % (number, result))


# def factorial(n):
#     if n < 1:
#         return -1
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return factorial(n - 1) + factorial(n - 2)
#
#
# number = int(input('请输入一个正整数：'))
# result = factorial(number)
# print("%d 的斐波那契数列最大值：%d" % (number, result))

#格式化打印输出的三种方式
# name = "李强"
# age = 12
# print("你好，我叫%s，今年我%d岁了。"% (name, age))
# print("你好！我的名字是：{}，今年我{}岁了。".format(name, age))
# print(f"你好！我的名字是：{name}，今年我{age}岁了。")
# name = '张天'
# age = 20
# gender = '男'
# print(f'我的名字是{name},今年{age}岁了,我的性别是：{gender}。')

# s="abcdefghijklmn"
# print(s[0:9:2])
# 编写一个程序，接受用户输入的年份，然后判断该年份是否是闰年（输出“是闰年”或不是闰年）。
# 提示：闰年是能够被4整除但不能被100整除的年份，或者能够被400整除的年份。
# year=int(input("输入年份："))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}不是闰年")
sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)
i=1
while i<=10:
    sum=sum+i
    i=i+1
print(sum)


# 根据身高体重计算某个人的BMI指数:
# 体质指数（BMI）=体重（kg）÷身高^2（m）

height = float(input('请输入您的身高(m):'))
weight = float(input('请输入您的体重(kg):'))
BMI = weight / (height * height)
print('您的BMI值为:',BMI)




# 获取用户输入的长和宽
# length = float(input("请输入长方形的长："))
# width = float(input("请输入长方形的宽："))
#
# # 计算面积
# area = length * width
# # 计算周长
# perimeter = 2 * (length + width)
#
# # 输出结果
# print(f"长方形的长为{length}，宽为{width}，面积为{area}，周长为{perimeter}。")

# perimeterdef add(a,b):
#     return a+b
#
# c=add(3,5)
# print(c)
#
# purchase_amount = float(input("请输入购买金额："))
#
# # 根据购买金额计算折扣金额
# if purchase_amount <= 100:
#     discount_price = purchase_amount
# elif purchase_amount <= 500:
#     discount_price = purchase_amount * 0.9  # 9折
# elif purchase_amount <= 1000:
#     discount_price = purchase_amount * 0.8  # 8折
# else:
#     discount_price = purchase_amount * 0.7  # 7折
#
# # 计算实际支付金额
#
#
# print("原价为：", purchase_amount)
# print("您的实际支付金额为：", discount_price)




# 按要求输出以下信息。要求如下：
# 1、定义三个变量name，age，weight，自己初始化三个变量值。
# 2、按要求打印以下三个信息。
#
# 输出结果：
# 我的名字是x，今年x岁了，体重x公斤
# name="tom"
# age=20
# weight=100.22
# print("我的名字是%s，今年%d岁了，体重%.2f公斤"%(name,age,weight))

# a="我见青山多妩媚，喜逐颜开彩云追。欢然自觉情难尽，你若有心比翼飞。"
# print(a[0]+a[8]+a[16]+a[24])
# print(a[8:12])

# 键盘输入一个年龄，并显示提示信息：请输入你的年龄。
# 判断该年龄是否在18岁以上，若大于等于18，则输出：可以进入网吧；
# 否则输出：禁止进入网吧
# age=int(input("请输入年龄："))
# if age>=18:
#     print("可以进入网吧")
# else:
#     print("禁止进入网吧")

#！编写一个程序，根据用户输入的月份，输出该月份的季节。假设季节划分为春季（3月至5月）、夏季（6月至8月）、秋季（9月至11月）和冬季（12月至2月）
# month=int(input("输入月份"))
# if month>=3 and month<=5:
#     print(f"{month}月是春天")
# if month>=6 and month<=8:
#     print(f"{month}月是夏天")
# if month>=9 and month<=11:
#     print(f"{month}月是秋天")
# if (month>=1 and month<=2) or month==12:
#     print(f"{month}月是冬天")


#用户输入购买金额
# 若购买金额小于等于100元，则不打折；
# 若购买金额大于100元且小于等于500元，则打9折；
# 若购买金额大于500元且小于等于1000元，则打8折；
# 若购买金额大于1000元，则打7折。
#输出实际支付金额
# price=float(input("请输入金额："))
# if price<0:
#     print("输出不正确")
#
# if price<=100 and price>=0:
#     pay=price
# elif price>100 and price<=500:
#     pay=price*0.9
# elif price>500 and price<=1000:
#     pay=price*0.8
# else:
#     pay=price*0.7
# print(f"实际支付{pay}元")

#输入一个数字，如果是2的倍数且不是5的倍数，输出这个数的2倍；
#如果是5的倍数且不是2的倍数，输出这个数的5倍；
#如果同时是5的倍数和2的倍数，输出这个数的10倍；
#否则输出这个数本身
# a=int(input("请输入数字："))
# if a%2==0 and a%5!=0:
#     print(a * 2)
# elif a%5==0 and a%2!=0:
#     print(a * 5)
# elif a%5==0 and a%2==0:
#     print(a * 10)
# else:
#     print(a)
#split()方法




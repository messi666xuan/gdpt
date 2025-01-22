
# name = "李强"
# age = 12
# print("你好，我叫%s，今年我%d岁了。"% (name, age))
# print("你好！我的名字是：{}，今年我{}岁了。".format(name, age))
# print(f"你好！我的名字是：{name}，今年我{age}岁了。")
# name = '张天'
# age = 20
# gender = '男'
# print(f'我的名字是{name},今年{age}岁了,我的性别是：{gender}。')


'''
编写一个程序，接受用户输入的一个长方形的长和宽，
然后以 "长方形的长为XXX，宽为XXX，面积为XXX，周长为XXX。" 的格式输出。
'''
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

# 编写一个程序，接受用户输入的年份，然后判断该年份是否是闰年（输出“是闰年”或不是闰年）。
# 提示：闰年是能够被4整除但不能被100整除的年份，或者能够被400整除的年份。
# year=int(input("输入年份："))
# if year%4==0 and year%100!=0:
#     print(f"{year}闰年")
# elif year%400==0:
#     print(f"{year}闰年")
# else:
#     print(f"{year}不是闰年")


# 假设你是一位老师，你需要统计一组学生的成绩。
# 编写一个程序，统计并输出及格（成绩≥60分）的学生人数，并计算及格学生的平均分。
# 如果遇到不及格或者大于100的成绩，直接跳过不计入统计。
# scores = [85, 90, 78, 55, 102, 88, 76, 95, 67, 110, 82, 100, 70]
# sum=0
# number=0
# for i in scores:
#     if i>=60 and i<100:
#         sum+=i
#         number+=1
# print(sum/number)

# numbers = [2, 4, 6, 8, 12, 16, 20, 24, 28, 32]
# total = 0
# count = 0
#
# for num in numbers:
#     if num % 4 == 0:
#         total += num
#         count += 1
#
# average = total / count
# print("平均值为:", average)

scores = [85, 90, -1, 78, 92, -1, 88, 76, 95]
total_score = 0
count = 0
for score in scores:
    if score == -1:
        continue  # 跳过缺考学生的成绩
    total_score += score
    count += 1

if count > 0:
    average_score = total_score / count
    print(f"有效成绩的平均分：{average_score:.2f}")































































































































































































































































































































































































































































































































































































































































































































import random as rm
from random import randint as rt

# x=rt(1,10)
# print(x)
# #
# list=["一等奖","二等奖","三等奖"]
# prize=rm.choice(list)
# print(prize)
# # #
# a=rm.random()
# print(f"random.random()的值:{a}")  # 在[0.0, 1.0)区间返回随机浮点数

#randint(a, b)
# b=random.randint(1,50)
# print(f"random.randint(1,50)的值:{b}")  # 返回[1, 50]区间的随机整数
#
# #choice(sequence)
# my_list = ['一等奖', '二等奖', '谢谢惠顾']
# print(random.choice(my_list))  # 从列表中返回随机元素
# #
# uniform(a, b)
# print("random.uniform(1, 5)的值:", rm.uniform(1, 5))  # 在[1,5]区间返回随机浮点数












import random
# 使用Python的random.choice()方法来实现抽奖功能，奖项包括：“一等奖”，“二等奖”，“三等奖”和“谢谢惠顾”。
# 请用户输入他们的购物金额。
# 根据用户的抽奖结果，为他们应用以下折扣：
# 一等奖：打五折
# 二等奖：八折
# 三等奖：九折
#谢谢惠顾：无折扣
# 请你输出用户的抽奖结果和应付金额。
# list=["一等奖","二等奖","三等奖","谢谢惠顾"]
# prize=random.choice(list)
# money=float(input("请输入购物金额："))
# if prize=="一等奖":
#     money=money*0.5
#     print("恭喜获得一等奖，打五折")
# elif prize=="二等奖":
#     money = money * 0.8
#     print("恭喜获得二等奖，打八折")
# elif prize=="三等奖":
#     money = money * 0.9
#     print("恭喜获得三等奖，打九折")
# else:
#     print("很遗憾未中奖")
# print(f"抽奖结果：{prize},应付金额：{money}")









#石头剪刀布游戏，定义一个列表["石头", "剪刀", "布"]，和计算机进行比赛，
# 首先玩家自己手动输入，然后计算机随机生成，然后判断输赢
def win_lose(user,computer):
    if user==computer:
        return "平局"
    elif ((user=="剪刀" and computer=="布")
        or (user=="石头" and computer=="剪刀")
        or (user=="布" and computer=="石头")):
        return "玩家胜利"
    elif ((user=="剪刀" and computer=="石头")
        or (user=="石头" and computer=="布")
        or (user=="布" and computer=="剪刀")):
        return "计算机胜利"

# list=["石头", "剪刀", "布"]
# computer=random.choice(list)
# user=input("请输入你的手势：")
# print(f"玩家出{user},计算机出{computer}")
# result=win_lose(user,computer)
# print(result)



from operation import add,divide

# add(5,2)
# divide(5,2)

# import area
# from area import circle
# s1=area.square(5)
# s1.mianji()
# c1=circle(10)
# c1.mianji()










import greeting

greeting.say_hello("小红")









#






# import greeting
#
# greeting.say_hello("小红")
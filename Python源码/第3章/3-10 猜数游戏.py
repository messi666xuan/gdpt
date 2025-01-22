#
# print("猜数字游戏,输入一个1-100以内的数字")
# random_num = random.randint(1, 100)
# # print(random_num)  # 打开注释可查看生成的随机数
# for frequency in range(1,6):
#     number = input("请输入一个数字:")
#     if number.isdigit() is False:
#         print('请输入一个正确的数字')
#     elif int(number) < 0 or int(number) > 100:
#         print("请输入1-100范围的数字")
#     elif random_num == int(number):
#         print("恭喜你用了%d次猜对了" % frequency)
#         break
#     elif random_num > int(number):
#         print("很遗憾，你猜小了")
#     else:
#         print("很遗憾，你猜大了")
#     if frequency == 5:
#         print("很遗憾，%d次机会已用尽，游戏结束,答案为%d" %
#               (frequency, random_num))



import random
target=random.randint(1,100)
#flag=True
i=1
while True:
    if i>10:
        print("次数已用完")
        break
    guess=int(input("请输入你猜的数字："))
    i=i+1
    if guess<target:
        print("猜小了，请继续猜")
    elif guess>target:
        print("猜大了，请继续猜")
    else:
        print("牛逼，猜对了")
        break
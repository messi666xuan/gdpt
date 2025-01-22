import random

# 奖项
prizes = ['一等奖', '二等奖', '三等奖', '谢谢惠顾']

# 抽奖
lucky_draw = random.choice(prizes)

# 用户输入购物金额
total_amount = float(input("请输入你的购物金额："))

# 根据抽奖结果应用折扣
if lucky_draw == '一等奖':
    print("恭喜你！你获得了一等奖，本次购物享受50%的折扣。")
    total_amount = total_amount * 0.5
elif lucky_draw == '二等奖':
    print("恭喜你！你获得了二等奖，本次购物享受25%的折扣。")
    total_amount = total_amount * 0.75
elif lucky_draw == '三等奖':
    print("恭喜你！你获得了三等奖，本次购物享受10%的折扣。")
    total_amount = total_amount * 0.9
else:
    print("谢谢惠顾，本次购物没有折扣。")

# 显示应付金额
print("应付金额为：", total_amount)
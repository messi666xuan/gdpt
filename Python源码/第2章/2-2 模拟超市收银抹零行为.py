total_money = 36.15 + 23.01 + 25.12  # 累加总计金额
total_money_str = str(total_money)
# print('商品总金额为：' + total_money_str + '元')
print('商品总金额为：', total_money, '元')
pay_money = int(total_money)  # 进行抹零处理
pay_money_str = str(pay_money)
print('实收金额为：' + pay_money_str + '元')

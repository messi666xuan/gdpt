name_list = ['TOM', 'Lily', 'ROSE']
#
# # 需求：注册邮箱，用户输入一个账号名，判断这个账号名是否存在，如果存在，提示用户，否则提示可以注册
# """
# 1. 用户输入账号
# 2. 判断if...else
# """
#
name = input('请输入您的邮箱账号名:')
for i in name_list:
    if name==name_list:
        print("用户已存在")
    else:
        print("可以注册")


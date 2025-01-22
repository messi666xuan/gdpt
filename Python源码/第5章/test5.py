# 假设我们有以下字典：
my_dict = {'张三': 25, '李四': 30, '王五': 35, '赵六': 40, '钱七': 45}

# 打印出字典中的所有值。
print("所有值:", list(my_dict.values()))

# 打印字典中所有键值对。
for key, value in my_dict.items():
    print(key, ":", value)

# 打印字典中年龄大于30岁的人的姓名。
print("年龄大于30岁的人的姓名：")
for name, age in my_dict.items():
    if age > 30:
        print(name)

# 向字典中添加一个新的键值对，键是你自己的姓名，值是你的年龄。
myname = "王二麻子"
myage = 25  # 请替换为你的实际年龄
my_dict[myname] = myage

# 将字典中所有人的年龄增加5岁。
for name in my_dict:
    my_dict[name] += 5

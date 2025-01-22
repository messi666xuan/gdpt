#列表基本操作
# list1=["python",25,"周杰伦"]
# print(list1[:2])
# list_one = ['章萍', '李昊', '武田', '李彪']
# for i in list_one:
#     print(f"嗨，{i}！今日促销,赶快来抢购吧！")
# list_one = [1, 2, 3, 4,4,4,4,4]
# list_one.append(5)
# list_one.insert(1,6)
#
# del list_one[0]
# list_one.remove(3)
# list_one[0]=10
# print(list_one)

# 有一个列表，内容是：[21, 25, 21, 23, 22, 20]，记录的是一批学生的年龄
#
# 请通过列表的功能（方法），对其进行
# 定义这个列表，并用变量接收它
# 追加一个数字31，到列表的尾部
# 打印第一个元素（应是：21）
# 更新倒数第二个元素为26

# 在列表的第4个位置插入19
# a=[1,2,3,4,5,6]
# #通过位置下标插入元素
# a.insert(2,7)
# #在末尾追加元素
# a.append(8)
# print(a)
# #通过位置下标删除
# del a[3]
# print(a)
# #删除指定元素
# a.remove(8)
# print(a)
# #修改元素
# a[0]=10
# print(a)








# list=[1,2,3,4,5]
# #指定位置插入元素
# list.insert(1,6)
# list.insert(4,"python")
# #追加元素到末尾
# list.append("world")
# #指定位置删除
# del list[4]
# #通过内容删除
# list.remove("world")
# #修改元素
# list[1]=7
# #统计列表长度(元素个数)
# print(len(list))
# print(list)

#给定一个列表numbers，输出列表中所有为3的倍数的和
numbers=[12,25,36,5,8,9,66,35,24,10,15,33,85]
sum=0
for i in numbers:
    if i%3==0:
        sum+=i #等同于sum=sum+i
print(sum)
#把3的倍数添加进一个新列表
list=[]
for i in numbers:
    if i%3==0:
        list.append(i)
print(list)

















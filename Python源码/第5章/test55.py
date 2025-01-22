#字典基本操作
# dict={"a":1,"b":2,"c":3,"d":4}
# #修改字典元素
# dict["c"]=30
#
# #添加元素，当键不存在时
# dict["e"]=5
#
# #update（）添加或修改
# dict.update(f=6)
#
# #删除字典元素
# dict.pop("a")
#
# #
# for i in dict.keys():
#     print(f"键：{i}，值:{dict[i]}")


#假设你有一组学生成绩数据，你想要将学生姓名与其对应的成绩关联起来，可以用一个字典来表示：
student = { '李白': 85, '王维': 70, '杜甫': 92,'白居易': 65,'苏轼': 88}
# # 1.打印出学生姓名为'王维'的成绩。
print(student["王维"])
# # 2.添加一个新的学生'詹姆斯'，成绩为75。
student["詹姆斯"]=75
# # 3.删除学生'杜甫'的成绩。pop
student.pop("杜甫")
# # 4.更新学生'白居易'的成绩为90。
student["白居易"]=90
# # 5.格式化打印出所有学生的姓名和成绩
for i in student.keys():
    print(f"姓名：{i},成绩：{student[i]}")












# set1 = set([1, 2, 3])
# set2 = {3,4,5}
# #并集
# print(set1|set2)
#
# #交集
# print(set1&set2)
# #差分
# print(set1-set2)
# print(set2-set1)
#
# print(set1^set2)

















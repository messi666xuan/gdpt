# 学生成绩字典
student_scores = {
    '巧克力': 30,
    '曲奇饼': 75,
    '羊肉': 56,
    '篮球': 96,
    '羽毛球拍': 120
}

# 1. 打印出学生姓名为'王维'的成绩。
print("王维的成绩:", student_scores['王维'])

# 2. 添加一个新的学生'詹姆斯'，成绩为75。
student_scores['詹姆斯'] = 75

# 3. 删除学生'杜甫'的成绩。
student_scores.pop('杜甫')

# 4. 更新学生'白居易'的成绩为90。
student_scores['白居易'] = 90

# 5. 打印出所有学生的姓名和成绩。
print("所有学生的姓名和成绩:")
for name, score in student_scores.items():
    print(name + ":", score)

data_set = set()
print('=' * 20)
print('欢迎使用生词记录器')
print('1.查看单词本')
print('2.背单词')
print('3.添加新单词')
print('4.删除单词')
print('5.清空单词本')
print('6.退出')
print('=' * 20)
while 1:
    word_data_dict = {}
    fun_num = input('请输入功能编号：')
    if fun_num == '1':  # 查看生词本
        if len(data_set) == 0:
            print('生词本内容为空')
        else:
            print(data_set)
    elif fun_num == '2':  # 背单词
        if len(data_set) == 0:
            print('生词本内容为空')
        else:
            for random_words in data_set:
                w = random_words.split(':')
                in_words = input("请输入" + w[1]+'：\n')
                if in_words == w[2].strip():
                    print('太棒了')
                else:
                    print('再想想')
    elif fun_num == '3':  # 添加新单词
        new_words = input('请输入新单词：')
        new_china = input('请输入单词翻译：')
        word_data_dict.update({'单词': new_words, '翻译': new_china})
        dict_str = str(word_data_dict).replace('{', '') \
            .replace('}', '').replace("'", '')
        data_set.add(dict_str)
        print('单词添加成功')
        dict_str = dict_str.replace(',','')
        print(dict_str)
    elif fun_num == '4':  # 删除单词
        if len(data_set) == 0:
            print('生词本为空')
        else:
            li_st = list(data_set)
            print(li_st)
            del_wd = input("请输入要删除的单词：")
            for i in li_st:
                if del_wd in i:
                    data_set.remove(i)
                    print('删除成功')
                    break
                else:
                    print('请输入正确的单词')
    elif fun_num == '5':  # 清空
        if len(data_set) == 0:
            print('生词本为空')
        else:
            data_set.clear()
            print('清空')
    elif fun_num == '6':
        break
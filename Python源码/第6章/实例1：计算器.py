num_one = int(input('请输入第一个数:'))
num_two = int(input('请输入第二个数:'))

def oper(parm_one, parm_two):
    operator = input('请选择要执行的运算符：+、-、*、/' + '\n')
    if operator == "+":
        print("计算结果为:", +parm_one + parm_two)
    elif operator == '-':
        print("计算结果为:", parm_one - parm_two)
    elif operator == '*':
        print("计算结果为:", parm_one * parm_two)
    elif operator == '/':
        if parm_two == 0:
            print('除数不能为0')
        else:
            print("计算结果为:", parm_one / parm_two)
oper(num_one, num_two)


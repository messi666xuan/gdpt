import random

def determine_winner(user_choice, computer_choice):
    """判断胜负"""
    if user_choice == computer_choice:
        return "平局"
    elif (user_choice == "石头" and computer_choice == "剪刀") or \
         (user_choice == "剪刀" and computer_choice == "布") or \
         (user_choice == "布" and computer_choice == "石头"):
        return "用户获胜"
    else:
        return "计算机获胜"

choices = ["石头", "剪刀", "布"]

print("欢迎来到石头剪刀布游戏！")

while True:
    user_choice = input("请选择（石头/剪刀/布）：")
    while user_choice not in choices:
        print("无效选择，请重新输入。")
        user_choice = input("请选择（石头/剪刀/布）：")

    computer_choice = random.choice(choices)
    print(f"用户选择：{user_choice}，计算机选择：{computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    print(winner)

    play_again = input("是否继续游戏？(yes/no): ").strip().lower()
    if play_again != "yes":
        break

print("游戏结束。")

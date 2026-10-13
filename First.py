import random

def guess_game():
    answer = random.randint(1, 100)
    count = 0
    print("===== 猜数字游戏 =====")
    print("我已经想好了一个1到100之间的数字，你来猜猜看！")

    while True:
        input_str = input("请输入你猜测的数字：")
        if not input_str.isdigit():
            print("输入错误！请输入一个整数！")
            continue

        guess_num = int(input_str)
        count = count + 1

        if guess_num > answer:
            print("猜大了！")
        elif guess_num < answer:
            print("猜小了！")
        else:
            print(f"恭喜猜对！一共猜了{count}次")
            break

guess_game()
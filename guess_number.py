"""猜数字小游戏：电脑随机出 1-100，玩家输入猜测。"""

import random


def get_guess():
    while True:
        text = input("请输入你猜的数字（1-100）：").strip()

        if not text:
            print("输入不能为空，请重新输入。")
            continue

        try:
            guess = int(text)
        except ValueError:
            print("请输入整数。")
            continue

        if guess < 1 or guess > 100:
            print("请输入 1 到 100 之间的整数。")
            continue

        return guess


def main():
    answer = random.randint(1, 100)
    count = 0

    print("===== 猜数字小游戏 =====")
    print("电脑已经想好了一个 1-100 的数字，你来猜猜看。")

    while True:
        guess = get_guess()
        count += 1

        if guess < answer:
            print("小了，再猜大一点。")
        elif guess > answer:
            print("大了，再猜小一点。")
        else:
            print(f"猜对了，答案就是 {answer}。")
            print(f"你一共猜了 {count} 次。")
            break


if __name__ == "__main__":
    main()

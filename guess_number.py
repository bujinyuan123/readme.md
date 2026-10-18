# -*- coding: utf-8 -*-
"""
猜数字小游戏
功能：电脑随机出一个 1-100 的整数，用户输入猜测，
     程序提示“大了”或“小了”，直到猜中，并统计猜了几次。
"""

import random  # 导入随机模块，用来生成随机数


def read_guess():
    """读取并检查用户输入，返回一个 1-100 之间的整数。"""
    while True:
        text = input("请输入你猜的数字（1-100）: ").strip()

        # 空输入：提示后重新输入
        if text == "":
            print("输入不能为空，请重新输入！")
            continue

        # 把字符串转换成整数；转换失败说明不是整数
        try:
            guess = int(text)
        except ValueError:
            print("请输入一个有效的整数！")
            continue

        # 只接受 1-100 之间的数字
        if guess < 1 or guess > 100:
            print("数字必须在 1 到 100 之间，请重新输入！")
            continue

        return guess


def main():
    """游戏主流程"""
    # 1. 电脑随机生成 1-100 之间的一个整数
    answer = random.randint(1, 100)

    # 2. 记录用户猜了几次，初始为 0
    count = 0

    print("===== 猜数字小游戏 =====")
    print("我已经想好了一个 1-100 之间的整数，快来猜猜看吧！")

    # 3. 不断循环，直到用户猜中
    while True:
        # 读取一个合法输入；非法输入不会计入次数
        guess = read_guess()

        # 猜的次数加 1
        count += 1

        # 4. 比较大小，给出提示
        if guess < answer:
            print("小了，再大一点！")
        elif guess > answer:
            print("大了，再小一点！")
        else:
            # 猜中了，结束游戏
            print(f"恭喜你，猜中了！答案就是 {answer}")
            print(f"你一共猜了 {count} 次。")
            break


# 程序入口：只有直接运行这个文件时才会执行 main()
if __name__ == "__main__":
    main()

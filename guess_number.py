# -*- coding: utf-8 -*-
"""
猜数字小游戏
功能：电脑随机出一个 1-100 的整数，用户输入猜测，
     程序提示"大了"或"小了"，直到猜中，并统计猜了几次。
"""

import random  # 导入随机模块，用来生成随机数


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
        # 让用户输入一个整数（如果不是数字会报错，这里用 try 兜底）
        try:
            guess = int(input("请输入你猜的数字: "))
        except ValueError:
            print("请输入一个有效的整数！")
            continue

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

# 猜数字小游戏（Guess the Number）

一个用 Python 编写的命令行小游戏：电脑随机生成一个 **1-100** 的整数，玩家反复输入猜测，程序提示“大了”或“小了”，直到猜中为止，并统计一共猜了几次。

> 本项目是通识任务 2 的实践项目，代码保持单文件、结构简单，适合初学者阅读。

## 功能

- 电脑随机生成 1-100 之间的整数
- 玩家输入猜测，程序提示“大了”或“小了”
- 猜中后显示答案和总猜测次数
- 对空输入、非整数、超出 1-100 范围的输入进行检查，非法输入不计入次数
- 只用 Python 标准库，不需要安装第三方依赖

## 项目结构

```text
D:\play_do\first\
├── guess_number.py   # 游戏主程序（单文件）
├── readme.md         # 项目说明（本文件）
└── .gitignore        # Git 忽略规则（如 __pycache__）
```

## 运行环境

- Windows 10/11
- Python 3.x（本项目在 Python 3.9.12 下测试通过）
- 无需安装第三方库

检查 Python 是否可用：

```bat
python --version
```

## 命令行运行（Win + R → cmd）

1. 按 `Win + R`，输入 `cmd`，回车打开命令提示符。
2. 切换到项目目录（注意 `/d`，从 C 盘切换到 D 盘时必须加）：

   ```bat
   cd /d D:\play_do\first
   ```

3. 运行程序：

   ```bat
   python guess_number.py
   ```

   如果系统里 `python` 命令不可用，也可以尝试：

   ```bat
   py guess_number.py
   ```

4. 按提示输入 1-100 之间的整数，猜中后程序结束，并显示猜测次数。
5. 想中途退出可以按 `Ctrl + C`。

## 玩法说明

1. 程序在 1-100 中随机选一个答案，但不会告诉你。
2. 你每次输入一个整数。
3. 如果输入比答案大，程序提示“大了”；如果比答案小，程序提示“小了”。
4. 不断缩小范围，直到猜中。
5. 程序会统计你一共猜了多少次。

## 运行示例

假设本局答案是 62：

```text
===== 猜数字小游戏 =====
我已经想好了一个 1-100 之间的整数，快来猜猜看吧！
请输入你猜的数字（1-100）: 50
小了，再大一点！
请输入你猜的数字（1-100）: 75
大了，再小一点！
请输入你猜的数字（1-100）: 62
恭喜你，猜中了！答案就是 62
你一共猜了 3 次。
```

如果输入了不合法的内容，程序会提示并让你重新输入，例如：

```text
请输入你猜的数字（1-100）: abc
请输入一个有效的整数！
请输入你猜的数字（1-100）: 200
数字必须在 1 到 100 之间，请重新输入！
```

## 程序逻辑说明

核心代码在 `guess_number.py`，可以分成四步理解：

### 1. 生成答案

```python
answer = random.randint(1, 100)
```

`random.randint(1, 100)` 会随机返回一个 1 到 100 之间的整数（包含 1 和 100），把它存到变量 `answer` 中。

### 2. 记录次数

```python
count = 0
```

变量 `count` 用来记录猜了几次，初始值为 0。每成功读取一次有效猜测，就执行 `count += 1`。

### 3. 循环输入并比较

```python
while True:
    guess = read_guess()
    count += 1

    if guess < answer:
        print("小了，再大一点！")
    elif guess > answer:
        print("大了，再小一点！")
    else:
        print(f"恭喜你，猜中了！答案就是 {answer}")
        print(f"你一共猜了 {count} 次。")
        break
```

- `while True` 表示一直循环，直到遇到 `break`。
- `read_guess()` 负责读取输入并检查合法性，返回一个 1-100 的整数。
- 用 `if / elif / else` 比较猜测值和答案。
- 猜中时执行 `break`，跳出循环，游戏结束。

### 4. 输入检查

`read_guess()` 里做了三层检查：

```python
text = input("请输入你猜的数字（1-100）: ").strip()

if text == "":
    print("输入不能为空，请重新输入！")
    continue

try:
    guess = int(text)
except ValueError:
    print("请输入一个有效的整数！")
    continue

if guess < 1 or guess > 100:
    print("数字必须在 1 到 100 之间，请重新输入！")
    continue
```

- `.strip()` 去掉首尾空格。
- `int(text)` 把字符串转成整数；如果转不了，会抛出 `ValueError`，用 `try / except` 捕获。
- `continue` 表示跳过本次循环，重新让用户输入；因此非法输入不会被计入猜测次数。

## Git 与 GitHub

本项目已使用 Git 管理，并推送到 GitHub：

- 仓库地址：<https://github.com/bujinyuan123/readme.md>
- 默认分支：`main`

常用命令：

```bat
cd /d D:\play_do\first
git status
git add .
git commit -m "提交说明"
git push
```

查看远程仓库：

```bat
git remote -v
```

## 常见问题

### 1. 提示“python 不是内部或外部命令”

说明 Python 没有加入系统环境变量。可以重新安装 Python 并勾选 **Add Python to PATH**，或者改用 `py guess_number.py`。

### 2. `cd D:\play_do\first` 后仍然在 C 盘

在 cmd 中跨盘符切换目录要加 `/d`：

```bat
cd /d D:\play_do\first
```

### 3. 中文显示乱码

可以把命令提示符的代码页切换为 UTF-8：

```bat
chcp 65001
```

然后再运行 `python guess_number.py`。

## 许可证

本项目仅供学习交流使用。

# 猜数字游戏规则：
# ① 系统随机生成1-10之间的一个数字
# ② 一共3次猜数字机会
# ③ 输入不同的数字，然后与系统生成的数字进行判断
# 有三种情况：
# 猜对了
# 猜大了
# 猜小了
# 1. 导入随机模块，生成一个随机数
from random import randint

rand_num = randint(1, 10)

# 2. 定义一个循环，循环3次
for i in range(3):
    # 3. 每次循环提示用户输入要猜的数字
    user_num = int(input('请输入您要猜的数字：'))
    # 4. 进行条件判断
    if user_num == rand_num:
        print('恭喜您，猜对了')
        break

    elif user_num > rand_num:
        print('很抱歉，猜大了')
    else:
        print('很抱歉，猜小了')
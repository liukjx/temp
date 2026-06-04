# 随机生成一个1到100之间的整数，
# 用户通过输入猜测的数字，程序会根据用户的输入提示“猜大了”、“猜小了”或“猜对了”。
# 用户可以无限次猜测，
# 直到猜对为止。猜对后，程序会提示用户并结束游戏。
import random
# 1:随机生成一个1到100之间的整数，
randomNum=random.randint(1,100)
# print(randomNum)
# 用户可以无限次猜测，
while True:
    # 2:用户通过输入猜测的数字，
    inputUserNum = int(input("请输入您猜的数字"))
    # 2-1程序会根据用户的输入提示“猜大了”、“猜小了”或“猜对了”。
    if inputUserNum>randomNum:
        print("猜大了")
    elif inputUserNum<randomNum:
        print("猜小了")
    else:
        print("猜对了")
        break

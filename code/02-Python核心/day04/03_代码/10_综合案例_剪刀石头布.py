"""
参与游戏的角色有两个（玩家 与 电脑），玩家手工出拳，电脑随机出拳，根据石头剪刀布判断输赢。
玩家：player（玩家手工输入石头0、剪刀1、布2）
电脑：computer（随机出拳）

案例分析：
游戏思路分析：人机互动
游戏角色：  ① 玩家    ② 电脑
游戏规则： ①玩家赢   ②平局    ③电脑赢
如果玩家赢  石头0、剪刀1、布2
    第一种情况 ： 玩家出石头     赢      机器剪刀
    第二种情况 ： 玩家出剪刀     赢      机器剪布
    第三种情况： 玩家出布        赢     机器石头
如果平局？
    玩家和机器出同样
else:
    机器赢
"""
# 游戏思路分析：人机互动
import random

computer = random.randint(0,2)  # 默认机器出剪刀
print(computer)
player = int(input("请输入您要出拳的信息：(0:石头  1:剪刀  2：布)"))

# 如果玩家赢  石头0、剪刀1、布2
#     第一种情况 ： 玩家出石头     赢      机器剪刀    (player==0 and computer==1)
#     第二种情况 ： 玩家出剪刀     赢      机器剪布    (player==1  and computer==2)
#     第三种情况： 玩家出布        赢     机器石头    (player==2 and computer==0)
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print("玩家赢")
# 如果平局？
#     玩家和机器出同样    player==computer
elif player == computer:
    print("平局")
else:
    print("机器赢")

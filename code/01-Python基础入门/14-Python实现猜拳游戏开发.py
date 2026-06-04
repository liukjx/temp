'''
核心思路分析
游戏角色：玩家（我们自己）、电脑角色
游戏规则：玩家必须手工选择出拳信息（石头、剪刀、布）
        电脑采用随机出拳（问题：目前还没有学习随机操作）
输赢判断：分为三种情况
第一种：玩家获胜
① 玩家出石头且电脑出剪刀
或
② 玩家出剪刀且电脑出布
或
③ 玩家出布且电脑出石头
第二种：平局player == computer
第三种：电脑获胜
要使用的技术点，if...elif...else
且：and
或：or
非：not
'''
from random import randint
# 1. 获取玩家出拳信息
player = int(input('请输入您的出拳信息（1-石头、2-剪刀、3-布）：'))
# 2. 获取电脑出拳信息
computer = randint(1, 3)
# 3. 输赢比较
if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')
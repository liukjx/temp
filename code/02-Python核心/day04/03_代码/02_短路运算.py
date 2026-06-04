"""
回顾
    1：and  全真为真，有假必假      Flase and True
                                比较第一个值，发现第一个值是假，
                                根据原则：全真为真，有假必假
                                则后面得True不需要参与比较，因为结局确定
    2：or   有真为真，全假为假
    3：not  真亦假来假亦真

短路运算：在python中短路运算并不是一件坏事，反而可以加快程序执行速度
概念：主要针对的and 和 or

总结：
    如果表达式1 and 表达式2 ，如果表达式1为false ，则最终的结果为false
    如果表达式1 or  表达式2 ，如果表达式1为true，则最终结果为ture

比较返回值判断：谁决定运算结果，返回值
注意：如果and 或者 or两边为非布尔值，要遵循如下计算规则
    python把0、空字符串''，None看成False
    其他数值和非空的字符串都看True
"""
# print(False and True or True)  #False
#
# print(0 and 1)   #  0   1   true   false


print('itcast' and 3 or 0 )

print(0  and 3 or 6  and  8)
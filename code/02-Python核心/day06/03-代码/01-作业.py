# 基础题:
# 	1.定义一个字符串，如str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"。
# 	编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码。

# 字符串索引
# 字段赋值 &拼接

import random

str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 随机数  randint(开始位置,结束位置)
# 拿字符串中字符  字符串名字[索引]
# len(str1)-1  索引的最大值= 长度-1
# for i in range(4): print(str1[random.randint(0, len(str1) - 1)],end="")
# for i in range(4):
#     #随机数  randint(开始位置,结束位置)
#     indexs = random.randint(0, len(str1) - 1)
#     random.choice()
#     #字符串名字[索引]
#     print(str1[indexs],end="")

# # 	2.已知列表 list1 = [11, 22, 33, 22, 11, 55], 请对其进行去重, 并将去重后的结果打印到控制台上.
# print(list(set([11, 22, 33, 22, 11, 55])))
#
# list1 = [11, 22, 33, 22, 11, 55]
# new_list=[]
# for i in list1:
#     if i not in new_list:
#         new_list.append(i)
#
# print(new_list)

# 	3.键盘录入1个字符串并接收, 计算其中每个字符出现的次数, 并将结果打印到控制台上.
# 	例如:
# 		录入: abcbcAABBB11133
# 		输出: a(1)b(2)c(2)A(2)B(3)1(3)3(2)	格式一致即可, 不要求顺序.

# # 键盘录入1个字符串并接收
# str1 = input("请输入一个字符串")
# count = {}
# # 计算其中每个字符出现的次数
# for i in str1:
#     # print(i)
#     if i in count:
#         count[i] += 1
#         # print(count[i],i)
#     else:
#         count[i] = 1
#         # print(count[i], i)
#
# for e in count:
#     print(f"{e}({count[e]})",end="")
#     # print(e,"---",count[e])


# 	4给定一个集合numbers，集合中包含1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15元素，求该集合中所有奇数的和是多少.
numbers={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
sum_qs=0
for nb in numbers:
    if nb%2!=0:
        sum_qs+=nb
print(sum_qs)
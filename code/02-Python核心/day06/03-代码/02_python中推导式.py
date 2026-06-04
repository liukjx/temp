# """
# 解释：
#     推导式是 while 循环 for循环  for ...if    for ... for一种简便写法
#
# 推导式语法：
#     [结果 for i in 数据容器]                   简化for循环
#     [结果 for i in 数据容器 if 条件判断]        for循环+if结构
#     [结果 for i in 数据容器 for j in 数据容器]  for循环+for循环
# """
# # # #没有推导式之前 while 1~100循环
# # # i =1
# # # while i<=100:
# # #     print(i)
# # #     i+=1
# #
# # #【没有】推导式之前 for  1~100循环
# # for i in range(1,101):
# #     print(i)
# # #【推导式】后
# # [print(i) for i in range(1,101)]
#
# #案例 找1~100之间偶数
# # 【没有推导式】
# # for i in range(1,101):
# #     if i%2==0:
# #         print(i)
# # 【推导式】
# [print(i) for i in range(1, 101) if i % 2 == 0]

# 外循环循环一次，内循环循环一轮   外循环*内循环
for i in range(5):
    for j in range(5):
        print(j)


# 案例：创建列表 => [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 注意：只要给定一个结构，必须有规律可循
# 前三个
# (1, 0)
# (1, 1)
# (1, 2)

#后三个
# (2, 0)
# (2, 1)
# (2, 2)
#
list_new =[]
# for i in range(1,3):
#     for j in range(0,3):
#             list_new.append((i,j))
# print(list_new)

#推导式：
[list_new.append((i, j)) for i in range(1, 3) for j in range(0, 3)]
print(list_new)














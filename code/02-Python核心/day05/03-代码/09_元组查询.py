# 1元组[索引]根据==索引下标==查找元素
# 2index()查找某个数据，如果数据存在返回对应的下标，否则报错，语法和列表、字符串的index方法相同
# 3count()统计某个数据在当前元组出现的次数
# 4len()统计元组中数据的个数

tuple2 = (1, 1.5, "str", "True", "str", "", " ")
# 元组[索引]根据==索引下标==查找元素
# tuple2[1]=2.0  #TypeError: 'tuple' object does not support item assignment
print(tuple2)
# print(tuple2[1])
# index()查找某个数据，如果数据存在返回对应的下标
print(tuple2.index(1))
# 找值1   star:从索引1开始   stop：到索引3结束
# print(tuple2.index(1,1,3))
# count()统计某个数据在当前元组出现的次数
print(tuple2.count("itcast"))
# len()统计元组中数据的个数
print(len(tuple2))  # 5   6   7
#    1
# tuple3 = (1,True,0,0,False)   # 你看到是True 计算底层 1
# print(tuple3.count(False))        # 你看到是False 计算底层 0
# 给定一个元组my_tuple，里面包含1, 2, 3, 4, 5, 6, 7, 8, 9元素，要求统计数字元组中, 奇数的个数
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9)


# tp.for
count = 0
for e in tp:
    if e % 2 != 0: count += 1
print(count)

# 1. 定义一个单元素的元组
tuple1 = (10,)
print(tuple1)
print(type(tuple1))

# 2. 定义一个多元素的元组
tuple2 = (10, 20, 30)
print(tuple2)
print(type(tuple2))

# 3. 通过索引下标实现元组中元素的访问
print(tuple2[0])
print(tuple2[1])
print(tuple2[2])

# 4. 使用for循环实现元组的遍历操作
for i in tuple2:
    print(i)
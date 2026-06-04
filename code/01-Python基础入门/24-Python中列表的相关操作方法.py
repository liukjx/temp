# 列表操作包含以下函数:
# 1、len(list)：列表元素个数
# 2、max(list)：返回列表元素最大值
# 3、min(list)：返回列表元素最小值
# 4、list(seq)：将元组转换为列表

# 列表操作包含以下方法:
# 1、list.append(obj)：在列表末尾添加新的对象
# 2、list.count(obj)：统计某个元素在列表中出现的次数
# 3、list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4、list.remove(obj)：移除列表中某个值的第一个匹配项
# 5、list.reverse()：反向列表中元素
# 6、list.sort([func])：对原列表进行排序

# 1. 定义一个列表
list1 = [1, 2, 3, 1]
print(len(list1))

# 2. 获取列表中元素最大值与最小值
print(max(list1))
print(min(list1))

# 3. 定义一个元组
tuple1 = (10, 20, 30)
list2 = list(tuple1)
print(list2)
print(type(list2))

# 4. 获取列表元素在列表中出现次数
count = list1.count(1)
print(count)

# 5. 使用extend方法实现列表的合并操作
list1.extend([4, 5, 6])
print(list1)

# 6. 使用remove移除列表中的元素6
list1.remove(6)
print(list1)

# 7. 定义一个列表，使用reverse方法实现对其翻转操作
list2 = [10, 20, 30]
list2.reverse()
print(list2)

# 8. 使用sort()方法实现对列表元素的排序
list2.sort(reverse=True)
print(list2)
# 1列表[索引] = 修改后的值修改列表中的某个元素
# 2reverse()将数据序列进行倒叙排列
# 3sort()对列表序列进行排序
list2 = ["盲僧", "亚索", "瑞文", "铁男"]
# 1列表[索引] = 修改后的值修改列表中的某个元素  李青
list2[0] = '李青'
print(list2)
# 2reverse()将数据序列进行倒叙排列
list2.reverse()  # 没有返回值
print(list2)
# 3sort()对列表序列进行排序
list2 = [11, 33, 66, 10, 90]
# print(list2)
# list2.sort()  # None 没有返回值   默认从小到大
# print(list2)
print("排序前",list2)
list2.sort(reverse=True)
print("排序后",list2)


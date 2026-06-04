# 1. 定义一个空字典
dict1 = {}
# 2. 定义有数据的字典
dict2 = {'title':'Python入门教程', 'price':9.98, 'publish':'黑马程序员'}
print(dict2)
print(type(dict2))

# 3. 通过key获取字典元素值
print(dict2['title'])
print(dict2['price'])
print(dict2['publish'])

# 4. 字典的新增与更新操作
dict2['price'] = 6.69
print(dict2)

# 5. 删除字典元素
del dict2['publish']
print(dict2)

# 6. 使用clear()方法实现字典的清空操作
dict2.clear()
print(dict2)

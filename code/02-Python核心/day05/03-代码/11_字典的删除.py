"""
存储一个人的信息
    姓名
    年龄
    性别
    地址
使用字典方式
"""
dict_init = {}
dict_init['name'] = '哪吒'
dict_init['age'] = '3岁'
dict_init['gender'] = '男'
dict_init['address'] = '陈塘关'
print(dict_init)

# 删除格式一 性别
del dict_init['gender']
print(dict_init)

# del dict_init['3岁']  #KeyError: '3岁'
# print(dict_init)

#清空字典
print(dict_init.clear())  #None 没有返回值
print(dict_init)

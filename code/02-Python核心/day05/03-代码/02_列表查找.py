"""
index()指定数据所在位置的下标
count()统计指定数据在当前列表中出现的次数
in 判断指定数据在某个列表序列，如果在返回True，否则返回False
not in判断指定数据不在某个列表序列，如果不在返回True，否则返回False
"""
list1 = ["雷军", "张彤", "刘强东", "龚晓京","雷军"]
#        0         1       2       3
#index() 格式：   列表名.index("要找的数据")
print(list1.index("刘强东"))  #返回索引值
# print(list1.index("奶茶妹妹")) #ValueError: '奶茶妹妹' is not in list
#结论：找到，返回索引值，找不到报错

#count() 格式：   列表名.count("要统计数据")
print(list1.count("雷军"))   # 雷军出现1次
#注意！！！ in 不是一个函数 ，是一个关键字 ，所以不能用列表名.方式调用
if '雷军' in list1 :
    print("在")
else:
    print("不在")
if '雷军' not in list1 :
    print("不在")
else:
    print("在")


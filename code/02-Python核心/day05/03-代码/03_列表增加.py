# append()增加指定数据到列表中
# extend()列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
# insert()指定位置新增数据
# 韦小宝
list2 = ["双儿", "建宁", "曾柔", "阿珂", "方怡", "沐剑屏", "苏荃"]
# append()增加指定数据到列表中  格式: 列表名.append() 特点：默认末尾追加
print(list2.append("韦小宝"))  # 啥意思None  ， 因为append方法（函数）没有返回值（貔貅）
print(list2.append("陈近南"))
print(list2)

#需求 ，指定位置增加
## insert()指定位置新增数据   无返回值 None
print(list2.insert(3, "韦小宝"))
print(list2)
# extend()列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
list3=["张三","李四","王五","赵六","麻七","周八"]
#案例 把list3加到list2后面
# list2.append(list3)
# append：['双儿',.... '苏荃', ['张三', '李四', '王五', '赵六', '麻七', '周八']]
# extend：['双儿', '.... '苏荃', '张三', '李四', '王五', '赵六', '麻七', '周八']
#总结 ：append实现将list3加入到list2的一个数据中，实现列表嵌套

# #      extends实现了将list3中的每一个数据加入到了list2
# list2.extend(list3)
# print(list2)








# #需求 ，使用append 实现extend  遍历
# for i in list3:
#     list2.append(i)
# print(list2)
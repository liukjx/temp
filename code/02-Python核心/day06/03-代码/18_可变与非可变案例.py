# def func(names):
#     names.append("赵四")
#
#
# #定义一个列表
# list1=["张三","李四","王五"]
# func(list1)
# print(list1)


def func(num2):
    num2 += 1


num1 = 10
func(num1)
print(num1)  # 10 or 11

# 总结
# 可变数据类型：内存地址一旦固定，其值可以发生改变，在赋值过程中，一个改变，另一个100%改变
# 不可变数据类型：内存地址一旦固定，其值不可以发生改变，在赋值过程中，一个改变，另一个100%不改变

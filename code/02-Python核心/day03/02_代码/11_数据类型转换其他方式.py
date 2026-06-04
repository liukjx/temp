"""
有问题！！！有什么问题 ？就是我们使用int做数据类型转换，但是用户可能不会按照我们设计的
方式输入，可能会输入一些其他的类型
解决方案：eval(str)
特点：是根据用户的数据进行推测数据类型
"""

pro_name = input("请输入商品名字")
num = eval(input("请输入购买数量"))
print(f"您这次推测的类型是：{type(num)}")
price = eval(input("请输入单价"))
print(f"您这次推测的类型是：{type(price)}")
print(f"您购买了{pro_name}商品,数量{num}总花费是{num*price}")

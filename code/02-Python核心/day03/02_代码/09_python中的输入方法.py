"""
#
# input()方法
# 格式： 变量名 = input("提示词")
#
# 总结：
    1：input方法可以中断程序执行 （等待输入）
    2：input接受到的数据赋值后都是字符串类型
# """
# name = input("请输入您的名字")
# # 格式化输出 ： 你的名字是
# # 三种    百分号   、format   f
# print("你的名字是%s"%(name))
# print("你的名字是{}".format(name))
# print(f"你的名字是{name}")


#需求 用户输入   要买的商品名字   购买数量2  单价是30
# #需求 您购买了 xxx商品 数量 2  总花费是 2*30
# pro_name = input("请输入商品名字")   #str
# print(type(pro_name))
# num = input("请输入购买数量")       #int   str
# print(type(num))
# price = input("请输入单价")       # float   str
# print(type(price))

# print(f"您购买了{pro_name}商品,数量{num}总花费是{num*price}")






#需求  ：定义两个变量 name address
#输入要求允许用户自定义输入 name address
#输出  您是name 您的地址是address
#三种输出

#知识一：变量定义      变量名 = 变量值
#知识二：input输入格式 变量名 =  input()
#知识点三   %輸出   format 輸出   f輸出
#知识点四：变量命名做到见名知意
name = input("请输入您的名字")
address = input("请输入您的地址")
print("您是%s您的地址是%s"%(name,address))
print("您是{}您的地址是{}".format(name,address))
print(f"您是{name}您的地址是{address}")
#需求 用户输入   要买的商品名字   购买数量2  单价是30.5   ctrl+/
#需求 您购买了 xxx商品 数量 2  总花费是 2*30

# #方式一
# pro_name = input("请输入商品名字")        #str
# print(type(pro_name))
# num = int(input("请输入购买数量"))        #int   str
# print(type(num))
# price = float(input("请输入单价"))       # float   str
# print(type(price))
#
# print(f"您购买了{pro_name}商品,数量{num}总花费是{num*price}")


# #方式二
# pro_name = input("请输入商品名字")        #str
# num = input("请输入购买数量")        #int   str
# price = input("请输入单价")      # float   str
# print(f"您购买了{pro_name}商品,数量{num}总花费是{int(num)*float(price)}")



#方式三  拓展
pro_name = input("请输入商品名字")        #str
num= input("请输入购买数量")        #int   str
num=int(num)
price= input("请输入单价")      # float   str
price = float(price)

print(f"您购买了{pro_name}商品,数量{num}总花费是{num*price}")
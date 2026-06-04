# 需求：用户手动输入梯形的上底、下底以及高，
# 能直接通过Python打印出梯形的面积为多少。

# 用户手动输入梯形的上底、下底以及高
# 定义变量 上底  下底  高
# 手动输入 input
#     #  input返回都是字符串
sd=eval(input("请输入上底"))
xd=eval(input("请输入下底"))
h=eval(input("请输入高"))

#计算 ？ 公式： s =(sd+xd)*h/2
s=(sd+xd)*h/2
print(s)





# #算术运算符
# print(1+1)
# print(1-1)
# print(1*1)
# print(type(1/1))
# print(type(54%4))
# print(2**3)  # 2*2*2
# 需求：把元组中的数据给我拿出来
tuple1 = (1, 2)

# 能，for循环
for e in tuple1:
    print(e)

# 不需要使用for循环，拆包即可！！！
# # 如何拆包
# num1, num2 = tuple1
# print(num1)
# print(num2)

#没给够
num1 = tuple1
print(num1)

#给多了  报错
# num1,num2,num3 = tuple1
# print(num1)

num1,num2=10,20
print(num1)
print(num2)

#变量赋值
a=10

a,b=10,20

a=b=c=10

c1='牛奶'

c2='可乐'

print("没交换前",c1,c2)
c1,c2=c2,c1
print("交换后",c1,c2)

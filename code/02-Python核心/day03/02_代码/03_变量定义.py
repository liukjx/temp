# print(a)   #报错，因为违反了变量先定义后使用原则


# 演示 标准变量定义原则 ：先定义 后使用

# 定义 ： 变量名 = 变量值
name = "张三"

# 变量的使用
print(name)


#需求  ： 定义下面这些变量
# name zhangsan  age 20   address =北京市昌平区
name ="zhangsan"
age =20
address="北京市昌平区"
print(name)
print(age)
print(address)
#痛点： 一个变量 print一次！如果有100变量？print
# 在一起？
#变量访问可以允许同时多个变量
print(name,age,address)
print(age,name,address)

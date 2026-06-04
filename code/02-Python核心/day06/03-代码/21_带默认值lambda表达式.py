print((lambda a=1, b=2, c=100: a + b + c)())

# 三目运算符  三元运算符 （if）  简化if语句的

# 案例：两个值求大小
x = 30
y = 20
if x>y:
    print(x)
else:
    print(y)
#简便写法： 返回结果  if 条件表达式 else 值
# 条件判断成立 if 条件判断 else 值
max_value=x if x>y else y
print(max_value)

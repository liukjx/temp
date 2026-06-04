# 编写一个函数 `greet`，接受一个参数 `name`，并返回字符串 `"Hello, {name}!"`。
# 编写一个函数
#函数定义
def greet(name):
    return f"Hello, {name}!"
#函数调用
# print(greet("zhangsan"))
# sayhello=greet("zhangsan")
# print(sayhello)

# 编写一个函数 `add`，接受两个参数 `a` 和 `b`，返回它们的和。如果 `a` 或 `b` 不是数字，返回 `"参数必须是数字"`。
def add(a,b):
    #对a,b进行类型判断
    if type(a) not in(int,float) or type(b) not in (int,float):
            return "参数必须是数字"
    return a+b

print(add(1, 3))


#新增方法 对类型进行判断 返回布尔值
num=10
print(isinstance(num, str))
def add2(a,b):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float))):
        return "参数必须是数字"
    return a+b
print(add2("True", 2))



# 编写一个函数 `average`，接受任意数量的参数，返回这些参数的平均值。
# 编写一个函数 `average`，
# 接受任意数量的参数
def average(*args):
    sum =0
    for i in args:
        sum+=i
    return sum/len(args)


print(average(1, 2, 3, 4, 5, 6, 7, 8,10))


# 编写一个函数 `outer`，在函数内部定义另一个函数 `inner`，`inner` 函数返回传入参数的平方。`outer` 函数返回 `inner` 函数的调用结果。

def outer (num):
    def inner(num2):
        return num2**2
    return inner(num)


# 编写一个函数 `modify_global`，在函数内部修改全局变量 `x = 10`，将其值改为 `20`。使用 `global` 关键字。
x=10
def modify_global():
    global  x
    x=20



# 使用 `lambda` 表达式编写一个函数，接受两个参数 `x` 和 `y`，返回它们的乘积。
# lambda 参数 :返回值
x=lambda x,y:x*y
print(x(1,2))

# 编写一个列表推导式，生成一个包含1到20之间所有偶数的平方的列表。
# 编写一个列表推导式  [i for i in 数据容器 ]
# 编写一个列表推导式，生成一个包含1到20之间  [i for i in  range(1,21)]
# 编写一个列表推导式，生成一个包含1到20之间所有偶数的平方的列表。 for + if
# [返回列表值 for i in range  if 条件判断 ]
# print([i ** 2 for i in range(1, 21) if i % 2 == 0])
a=[i ** 2 for i in range(1, 21) if i % 2 == 0]
print(a)
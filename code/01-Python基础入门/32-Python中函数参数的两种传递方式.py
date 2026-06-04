# 定义一个函数
def func(name, age, address):
    print(name)
    print(age)
    print(address)

# 1. 位置传参
func('Tom', 23, '美国纽约')

# 2. 关键词传参
func(name='Tom', address='美国纽约', age=23)
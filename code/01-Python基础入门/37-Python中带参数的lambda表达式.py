# 1. 带普通参数的lambda表达式
func1 = lambda a, b : a + b
print(func1(10, 20))

# 2. 带有默认值的参数lambda表达式
func2 = lambda a, b, c=100 : a + b + c
print(func2(10, 20))

# 3. 带有包裹位置参数的lambda表达式
func3 = lambda *args : args
print(func3(1, 10, 100))

# 4. 带有包裹关键词参数的lambda表达式
func4 = lambda **kwargs : kwargs
print(func4(a=1, b=10, c=100))
# 1. 定义一个函数
def func(*args):
    print(args)
    print(type(args))

# 2. 调用func函数
func()
func(1)
func(1,2,3)
# 1. 定义一个函数
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

# 2. 调用func函数
func()
func(name='Tom')
func(name='Tom', age=23, mobile='10086')
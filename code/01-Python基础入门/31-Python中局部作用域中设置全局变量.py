# 全局变量
num = 10
# 定义一个函数
def func():
    # 引入global关键字，作用：在局部作用域中声明全局变量
    global num
    num = 100

# 调用func()函数
func()
print(num)
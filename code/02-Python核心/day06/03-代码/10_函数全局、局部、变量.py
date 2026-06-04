num = 20  # 全局变量


def sum_num():
    a = 10  # 局部变量
    # print(num)  #调用
    num=50
    print(num)
    # 函数体内部就是局部作用域


print(num)   #  20  50
# print(num) #打印全局变量
# print(a)
# sum_num()

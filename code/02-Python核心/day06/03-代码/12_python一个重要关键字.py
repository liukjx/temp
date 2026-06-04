"""
需求：我们能不能再局部作用域下修改全局变量。
答案：可以，我们需要引入一个关键字 global
global代表声明为全局变了（此刻起，我们使用的就是全局变量）
"""
num = 20
def sum_num():
    global num  # 使用global关键字，将局部变量提升全局变量
    a = 10
    num=50

sum_num()
print(num)
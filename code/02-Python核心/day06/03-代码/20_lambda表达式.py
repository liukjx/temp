"""
在python中，lambda表达式称之为匿名函数（没有名字的函数），简化python代码
基本语法：
    lambda 函数参数:表达式或者返回值
"""
def func():
    return 10

#如何修改lambda表达式
funb=lambda :10
print(funb)  #<function <lambda> at 0x00000167B1A0BB88>
print(funb()) #10

print((lambda :10)())

#特别注意：由于lambda表达式没有名字，所以在实际的工作中必须把他赋值给某一个变量，否则无法直接调用

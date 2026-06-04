"""
在python中，函数执行完毕后，可以返回一个值给函数的调用位置。
这个返回值，我们可以return.

原则：谁调用返回给谁
"""


# 函数定义
def say():
    a = 10
    a += 1


# None 返回None

# 函数调用
print(say())


def say2():
    a = 10
    a += 1
    return a


print(say2())


def say4():
    a = 10
    a += 1
    return a    #11   # 只有第一个return返回值才起作用
    return 10
    return 1
    return 3    #3

print(say4())

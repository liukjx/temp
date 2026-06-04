# f = open("嘿嘿.avi", "rb")
# c = f.readlines()
# print(c)
# [Errno 2] No such file or directory: '嘿嘿.avi'
# 背景：如果几千行、几万行代码因为某一行或者某几行代码直接导致程序报错退出！！
# 不允许出现这样的情况。给与解决方案！！！
# 如何解决？  让抓住这个异常，让这个异常不影响我们其他代码功能运行
# 抓这个异常的错误信息，把他保存为文件（线上运行日志）。

# 如何处理 ？  异常格式：
"""
try:
    可能出现异常的代码
except:
    捕获后对代码进行处理
"""
try:
    a = 1 / 0
    f = open("嘿嘿.avi", "rb")
    c = f.readlines()
    print(c)
except ZeroDivisionError as b:
    print(b)
except FileNotFoundError as a:
    print(a)
    print("我捕获到了！！！嘿嘿嘿")



# 异常没有影响后续执行  （顺序执行）
for i in range(100):
    print("哈哈，我还可以执行")

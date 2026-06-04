"""
用Exception异常类型捕获可能遇到的所有未知异常
"""
try:
    # print(name)
    # print(1/0)
    # str1=eval(input("请输入一个字符串，我一定使用eval给你强转"))
    print(open("a.txt", "r"))
except Exception as  e:
    print(e)

print("上面捕获到了，所以我才可以执行")

import random


#完成函数调用
def randomCode(num):
    """
    randomCode函数主要是根据用户的输入num来指定打印字符串长度。
    :param num: 接受一个int值，用来指定字符串长度
    :return: 无返回值，因为函数体打印了字符串内存
    """
    str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(num):
        indexs = random.randint(0, len(str1) - 1)
        print(str1[indexs],end="")


#函数调用
num=int(input("请输入你要的验证码长度"))
randomCode(num)

import  ollama
import langchain
import  os
import random
import time
"""
try:
    可能出现异常代码
expect:
    如果出现异常，要执行代码
else:
    如果没有出现异常，要执行代码
finally:
    无论异常与否，都执行代码
"""

try:
    f=open("123.txt","r",encoding="utf-8")
except Exception as e:
    print("1有异常啦")
    print(e)
else:
    print("2没有异常，程序打印")
    c=f.read()
    print(c)
finally:
    print("3有没有异常我都打印")
    print("有借有还")
    try :
        f.close()
    except Exception as  e:
        print("没有申请f资源，无需关闭")
"""
try :
    可能出现代码
except:
    异常捕获
else:
    如果没有捕获到异常，自动执行else中缩进代码
"""

try:
    f = open("123.txt", "r", encoding="utf-8")
except Exception as e:
    print("------进异常了------")
    print(e)  #[Errno 2] No such file or directory: '123.txt'
else:
    print("----else缩进----")
    context = f.read()
    print(context)

print("-----顺序执行-----")

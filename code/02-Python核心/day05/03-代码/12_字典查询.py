"""
在python中，如果我们想要字典中所有的键，可以使用keys方法来获取
           如果我们想要字典中所有的值，可以使用values方法来获
基本语法:
    字典名称.keys()    返回的都是列表
    字典名称.values()  返回的都是列表
提示：返回的都是列表
"""
w = {'邓超': '孙俪', '张杰': '谢娜', '吴京': '谢楠', "韦小宝": "阿珂"}
print(w)  # {'邓超': '孙俪', '张杰': '谢娜', '吴京': '谢楠'}
print(w.keys())
print("-" * 35)  # 复制35个
print(w.values())
print("*" * 35)
print(w.items())
print("*" * 35)
# 字典的遍历 找到韦小宝 ，修改双儿
for tmp in w.keys():
    if tmp=="韦小宝":
        w[tmp]="双儿"
print("*" * 35)
print("修改后:",w)
print("❤" * 35)
for tmp in w.values():
    print(tmp)
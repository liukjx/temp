"""
不定长参数，也叫可变参数，用于不确定调用时会传递多少个参数场景（一个不传递）

1：不定长位置参数（不定长元组参数，可以使用一个元组来接受所有的参数）
        *args  *args参数整体   args变量名  *只是一个符号，没有别的意思
2：不定长关键字参数（不定长字典参数），使用一个字典接受所有的参数
        **kwargs    **kwargs 是一个整体   kwargs是一个变量名  **只是一个符号，没有别的意思
规则：
    ①两者可以单独使用
    ②也可以配合使用，但是*args要放在**kwargs前面。否则报错
# """
# #定义一个不定长位置参数
# # def fun(*args):
# def fun(*args):
#     for i in args:
#         print(i,end="")
#     print("❤❤❤❤❤❤❤❤❤")
#
# fun("张三")
# fun("张三",20)
# fun("张三",20,"北京昌平")
# fun("张三",20,"北京昌平","男")
# fun("张三",20,"北京昌平","男","未婚")
# fun("张三",20,"北京昌平","男","未婚","没有曾用名")

#
def func(**kwargs):
    for key in kwargs:
        value =  kwargs[key]
        print( f"{key}:{value}")
#不定长关键字参数
func()
print("*"*35)
func(name="刘备",age=23)
func(name="刘备",age=23,address="涿州")

#错误
# def funcf(**kwargs,*args):
#     print(0)
#
def funcf(*args,**kwargs):
    for i in args:
        print(i)
    for key in kwargs:
        value =kwargs[key]
        print(key,value)
#调用
funcf(1,2,3,4,54,6,7,78,8,9,"张三",name="张三三")


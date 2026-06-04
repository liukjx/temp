# #int(x) 方法 特点：输入一个x值，将x值转换为int类型
# a=1  # a 的类型是 int
# print(f"转换前类型{type(a)}")
# a=int(a)
# # print(f"转换后类型{type(a)}")  # 把int类型转换为int类型
#
# #float->int ？？？  数值型大转小 ：丢失精度，不报错
# a=1.0  # a 的类型是 float
# # print(a)   # 1.0
# # print(f"转换前类型{type(a)}")
# # a=int(a)
# # print(f"转换后类型{type(a)}")  # 把int类型转换为int类型
# # print(a)  # 1
#
#
# # str-》int     字符串必须是数值型  （float 、int）
#
# str="1.0"   #字符串类型的数值类型的float
# print(str)  #字符串类型的数值类型的float
# print(f"转换前类型{type(str)}")   # str
# str=int(str)  #把字符串类型数值类型float转换为 int  报错
# print(f"转换后类型{type(str)}")
# print(str)
#
# str -> int   字符串必须是数值型  int
str1="01"    #
print(str1) #
print(f"转换前类型{type(str1)}")
str1=int(str1)
print(f"转换后类型{type(str1)}")
print(str1)

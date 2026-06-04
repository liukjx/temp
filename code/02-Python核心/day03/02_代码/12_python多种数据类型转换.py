#
# # int ->float
# num1 =1
# print(type(float(num1)))
# print(float(num1))
#
# #float ->int  丢失精度
# num2 =3.5
# print(int(num2))  # 3   4
#
# #str -》 float
#有没有限制 ？
#
# str1="haha"
# print(float(str1))
#至此能不能下结论 字符串无法转换为float 不能
# 字符串3.5
# # str2="3.5"
# # # print(float(str2))
# # #结论：字符串要是转换为float 必须要求字符串是数值型字符串
# # print(int(float(str2)))
#
# # 字符串转换为int
# # str3="1.0"
# # print(int(str3))
#
# #
#
# str4="22"
# print(float(str4))
#
# 字符串 整型 转换为 浮点型 ？
# # 字符串整型-》浮点型
# str5="40"
# print(float(str5))
# # str5="40.0"
# # print(int(str5))
str6=40
print(f"{str6:.2f}")

"""
在python中，我们可以通过 引号（单引号、双引号、三引号）来定义字符串
"""

#基本操作
str1='abc'
print(type(str1))  #<class 'str'>

str2="abc"        #<class 'str'>
print(type(str2))

str3="""
你好，
好，
非常好。
"""
print(type(str3))   #快捷使用 type(str3).print 直接完成包裹

#注意  这里的三引号不是注释，如果有赋值，属于变量的内容

# 如果我想输入 I'm Tom  定义这个字符串
# str4 ='I'm Tom'
#解决方案
# ① 如果语句中有单引号，则采用非单引号方式来进行定义
str5 ="I'm Tom"
print(str5)

str6 ="""I'm Tom"""
print(str6)

#转义字符  \
str7='I\'m Tom'
print(str7)



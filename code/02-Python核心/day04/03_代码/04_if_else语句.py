"""
语法格式：
   if 条件判断:
       当条件判断为True时，则执行这个语句段
   else:
       当条件判断为False时，则执行这个语句段

去网吧进行升级 ， 不满足提示，回家写作业吧 ，满足进去
"""
age = eval(input("请输入您的年龄"))
if age>=18:
 print("欢迎光临")
else:
 print("回家写作业吧")

print("哈哈哈哈")


# 坑一：错误提示  SyntaxError: invalid character in identifier
# 原因：存在识别错误的字符   必须是英文冒号

#坑二：如果你和我敲得一样的话，请检查一下缩进，pyhon对缩进敏感
#原因：查看缩进 SyntaxError: invalid syntax


# 需求  升级考试    60分数线    用户输入一个成绩 ，判断 如果大于等于60分 ，可以升级
# 如果小于60分 ，不能升级,复考
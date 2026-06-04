"""
python三种输出方式
    1：百分号输出
    2：format格式输出
    3：f方式输出
"""

# 需求一：定义变量 名字 张三  年龄 18   学号 1
# 需求二：我的名字叫张三，今年18岁，学号是1

# 定义变量：  变量名 = 变量值
name = "张三"  # 见名知意
age = 18
student_id = 1
str1 = "我的名字叫"
print("我的名字叫", name, "今年", age, "岁", "学号是", student_id)
# 采用%号的方式
print("我的名字叫%s，今年%d岁，学号是%d" % (name, student_id, age))
# 坑：
# 坑一：注意括号不是中文的
# eg:print（ ）
# 坑二：%（）里面的变量分隔符逗号是英文
# print("我的名字叫%s，今年%d岁，学号是%d"%(name,student_id,age))
# eg ：print("我的名字叫%s，今年%d岁，学号是%d"%(name，student_id，age))
# 坑三  变量位置错误    学号是   %d   传入的是   name
print("我的名字叫%s，今年%d岁，学号是%d" % (student_id, age, name))

"""
注释：对代码进行解释说明并且不影响代码运行（逻辑）
python注释两种形式
     单行注释
        格式：#

     多行注释
        格式： 三引号    三引号
在企业中：
    1：一般使用注释对核心代码进行解释说明
    2：对整个代码进行标注（开发人、时间、代码作用、开发人联系邮箱）
"""
#演示单行注释
print("14hello")
# print("hello")
# print("hello")
print("17hello")


#多行注释
"""
print("17hello")
print("17hello")
print("17hello")
print("17hello")
print("17hello")
print("17hello")
print("17hello")
print("17hello")
"""


# 定义颜色代码
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
# 定义玫瑰花的字符画（带颜色）
rose = [
    f"         {RED}@@@{RESET}         ",
    f"       {RED}@@@@@@@{RESET}       ",
    f"      {RED}@@@@@@@@@{RESET}      ",
    f"     {RED}@@@@@@@@@@@{RESET}     ",
    f"    {RED}@@@@@@@@@@@@@{RESET}    ",
    f"   {RED}@@@@@@@@@@@@@@@{RESET}   ",
    f"  {RED}@@@@@@@@@@@@@@@@@{RESET}  ",
    f"   {RED}@@@@@@@@@@@@@@@{RESET}   ",
    f"    {RED}@@@@@@@@@@@@@{RESET}    ",
    f"     {RED}@@@@@@@@@@@{RESET}     ",
    f"      {RED}@@@@@@@@@{RESET}      ",
    f"       {RED}@@@@@@@{RESET}       ",
    f"         {RED}@@@{RESET}         ",
    f"          {GREEN}|{RESET}          ",
    f"          {GREEN}|{RESET}          ",
    f"          {GREEN}|{RESET}          ",
    f"         {GREEN}/|\\{RESET}         ",
    f"        {GREEN}//|\\\\{RESET}        ",
    f"       {GREEN}///|\\\\\\{RESET}       ",
    f"      {GREEN}////|\\\\\\\\{RESET}      "
]

# 打印玫瑰花
for line in rose:
    print(line)

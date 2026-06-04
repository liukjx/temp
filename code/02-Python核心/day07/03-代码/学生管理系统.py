# 添加学生
def add_student():
    print("add_student")


# 删除学生
def del_student():
    print("del_student")


# 修改学生信息
def edit_student():
    print("edit_student")


# 查询学生信息
def get_student():
    print("get_student")


# 遍历学生信息
def get_all_student():
    print("get_all_student")


# 退出系统
def get_out_student():
    print("get_out_student")


# 定义菜单函数
def menu():
    print("*" * 35)
    print("欢迎登录学生管理系统")
    print("1:添加学生信息")
    print("2:删除学生信息")
    print("3:修改学生信息")
    print("4:查询学生信息")
    print("5:遍历所有学生信息")
    print("6:退出系统")


while True:
    menu()
    user_num = int(input("请输入您要选择的功能"))
    if user_num == 1:
        add_student()
    elif user_num == 2:
        del_student()
    elif user_num == 3:
        edit_student()
    elif user_num == 4:
        get_student()
    elif user_num == 5:
        get_all_student()
    elif user_num == 6:
        get_out_student()

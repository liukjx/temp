"""
数据该用什么容器进行存储 ？
  学生信息  姓名 、年龄 、 班级
  字典
  列表
  列表+字典  (选择) [{},{},{}]
"""
import os

students = []


# 添加学生
def add_student():
    # 1-1接受学生信息
    name = input("请输入您的姓名")
    age = input("请输入您的年龄")
    class_num = input("请输入您的班级")
    # 创建字典  (数据已经来了，考虑存放容器)
    student = {}
    student['name'] = name  # name:张三
    student['age'] = age
    student['class_num'] = class_num
    students.append(student)
    # print("add_student")
    print(f"学生{name}信息添加成功")


# 查询学生信息
def get_student():
    name = input("请输入您要查询学生姓名")
    for i in students:
        if i['name'] == name:
            print(f"查询到学生名字:{i['name']} ,年龄{i['age']},班级{i['class_num']}")
            break
    else:
        print(f"您查询的{name}学生不存在")


# 删除学生
def del_student():
    name = input("请输入您想删除学生姓名")
    for i in students:
        if i['name'] == name:
            students.remove(i)
            print(f"{name}学生删除成功")
            break
    else:
        print(f"您要删除的{name}信息不存在")


# 修改学生信息
def edit_student():
    old_name = input("请输入您要修改学生姓名")
    for i in students:
        if i['name'] == old_name:
            i['name'] = input("请输入新的名字")
            i['age'] = input("请输入新的年龄")
            i['class_num'] = input("请输入新的班级")
            print("学生信息修改成功")
            break
    else:
        print("您要修改学生的姓名不存在")


# 遍历学生信息
def get_all_student():
    for i in students:
        print(i)

# 退出系统
def get_out_student():
    os._exit(0)


def get_save_student():
    f = open("student.txt", "w", encoding="utf-8")
    f.write(str(students))
    f.close()
    print("信息保存成功")

# 定义菜单函数
def menu():
    print("*" * 35)
    print("欢迎登录学生管理系统")
    print("1:添加学生信息")
    print("2:删除学生信息")
    print("3:修改学生信息")
    print("4:查询学生信息")
    print("5:遍历所有学生信息")
    print("6:保存学生信息到本地文件")
    print("7:退出系统")


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
        get_save_student()
    elif user_num == 7:
        get_out_student()

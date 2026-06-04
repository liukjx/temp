"""
集合
    概念：天生去重的无序的数据集合  （数据容器）
基本语法：
    格式一：集合名称={具体的数据}
    格式二：集合名称=set(具体的数据)
    格式三：如果是一个空集合只能是set()
    ！！！注意格式一集合里面传  集合名称={具体的数据}  key  value
# """
# # 定义一个集合
# set_init = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2}
# print(set_init)
# #天生去重
# # print(set_init)  #打印1~10 ，重复的2已经被去掉
#
# # set_init2 = {"Remembering","Discover","Those","Forgotten","See"}
# # print(set_init2)
#
# set_init3 = {"a","b","c","d"}
# print(set_init3)
#
# # for i in range(100):
# #     set_init4 = {12312421, 2543532, 354534532, 443543253, 5534534534, 653453462, 7654634634, 8532524, 9532532, 105325223}
# #     print(set_init4)
#
# # for i in range(100):
# set_init2 = {"Remembering","Discover","Those","Forgotten","See"}
# print(set_init2)

    # print(set_init2)

# set_init4 = {12312421, 2543532, 354534532, 443543253, 5534534534, 653453462, 7654634634, 8532524, 9532532, 105325223}
# # print(set_init4)
#
# # set_init2 = {"Remembering","Discover","Those","Forgotten","See"}
# # print(set_init2)
et_init4={"a","b","c","d"}
print(et_init4)

students = set()
students.add('李哲')
students.add('刘毅')
print(students)

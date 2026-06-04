# #集合添加 add
# students = set()
# students.add('李哲')
# students.add('刘毅')
# students.add('李雷')
# students.add('韩梅梅')
# print(students)
#
# # remove()方法：删除集合中的指定数据，如果数据不存在则报错。
# print(students.remove("李雷"))
# print(students)
#
# if '李雷' in students:
#     print("在")
# else:
#     print("不在")
#
# if '李雷' not in students:
#     print("不在")
# else:
#     print("在")
#
# # print(students.clear())
#
# a=set()
# a=students.copy()
# print(a.clear())
# print(students.difference(a))
#
st1 = set()
st1.add('李哲1')
st2 = set()
st2.add('李哲1')
st3 = set()
st3.add('李哲3')
st1.difference(st2,st3)
print(st2.difference(st1))

st1.update(st2)
print(st1)


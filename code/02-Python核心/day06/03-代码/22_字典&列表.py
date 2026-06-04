students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]
list2=[]
for i in students:
    list2.append(i['age'])
list2.sort()
print(list2)

# # 按name值升序排列
# students.sort(key=lambda x: x['name'])  # Jack/Rose/Tom
# print(students)
#
# # 按name值降序排列
# students.sort(key=lambda x: x['name'], reverse=True)
# print(students)
#
# # 按age值升序排列
# students.sort(key=lambda x: x['age'])
# print(students)
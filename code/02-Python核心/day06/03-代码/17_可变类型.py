"""
可变类型（内存地址一旦固定，其值是可以发生改变）
        列表（list [1, 2, 3]）
        字典（dict {key:value})
        集合（set {1, 2})
"""
list3=[7,4]
list1=[1,2,3]
print("------",id(list1))  #1539421721096
list2=list1
# print(id(list2))  #1539421721096

#尝试修改list1的值
# list1.append(4)
print(list1.extend(list3))
print(list1)
print("------",id(list1))
# print(list2)  #[1,2,3]  [1,2,3,4]
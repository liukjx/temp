# del 列表[索引]删除列表中的某个元素
# pop()删除指定下标的数据(默认为最后一个)，并返回该数据
# remove()移除列表中某个数据的第一个匹配项。
list2 = ["双儿", "建宁", "曾柔", "阿珂", "方怡", "沐剑屏", "苏荃"]
print("删除前",list2)
del list2[1]
print("删除后",list2)
# pop()删除指定下标的数据(默认为最后一个)，并返回该数据
print(list2.pop())  #有返回值 ，返回的是删除的数据
print(list2)
print(list2.pop(2))
print(list2)
# remove()移除列表中某个数据的第一个匹配项。
list2.insert(0,"方怡")
print(list2)
print(list2.remove("方怡"))  # 没有返回值 None
print(list2)
print(list2.remove("方怡"))
print(list2)






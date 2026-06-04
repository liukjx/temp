"""
and :要求比较严格   必须两边的表达式【全部】为真，最终结果为True ，反之Flase
       全真为真，有假必假
or  ：要求没有那么严格  只要保证or 两边有一个表达式为真，即最终结果为真，反之为Flase
      有真则真，全假为假
not  取反！！ 真亦假来假亦
     真亦假来假亦

总结：
  and 全真为真，有假必假
 or   有真则真，全假为假
 not  真亦假来假亦
"""

print(False and True)  #False
print(False and False) #纯False

print(False or True)  #真
print(True or True) #纯真
print(not(False) and (not(True)))


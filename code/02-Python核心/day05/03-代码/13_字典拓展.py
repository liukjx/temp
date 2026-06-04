"""
在python中，有一个特殊方法，可以把其他的数据容器如列表转换为key：value结构
格式：
    容器名称 enumerate,在实际使用过程中结合for
"""
list1 = ['a', 'b', 'c']

tuple2=('a', 'b', 'c')

str1 ="itcast"

# enumerate 转换为key value结构
for key,value in enumerate(tuple2):
    print(key,value)

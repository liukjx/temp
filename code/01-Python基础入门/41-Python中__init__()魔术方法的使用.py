# 1. 定义Person类
class Person(object):
    # 2. 定义属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 3. 实例化对象
p1 = Person('孙悟空', 30)
print(p1.name)
print(p1.age)

p2 = Person('猪八戒', 28)
print(p2.name)
print(p2.age)
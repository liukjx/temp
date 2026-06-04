# 1. 定义一个Person类
class Person(object):
    # 2. 定义公共属性和公共方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('i can speak Chinese!')

# 2. 定义一个Student子类
class Student(Person):
    pass

# 3. 实例化子类对象
s1 = Student('Rose', 23)
print(s1.name)
print(s1.age)

s1.speak()
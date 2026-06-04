# 1. 定义一个Person类
class Person(object):
    # 定义属性和方法
    def speak(self):
        print(self)
        print('Nice to meet you!')

# 2. 实例化Person类获取p1对象
p1 = Person()
print(p1)

p1.speak()
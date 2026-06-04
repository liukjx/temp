# 1. 定义一个Animal父类
class Animal(object):
    # 定义属性和方法
    def eat(self):
        print('i can eat food!')

    def sound(self):
        print('i can make a sound!')

# 2. 定义一个Dog类，继承Animal父类
class Dog(Animal):
    def sound(self):
        print('i can wang wang wang!')

# 3. 定义一个Cat类，继承Animal父类
class Cat(Animal):
    def sound(self):
        print('i can miao miao miao!')

# 4. 实例化子类对象
dog = Dog()
dog.eat()
dog.sound()

cat = Cat()
cat.eat()
cat.sound()
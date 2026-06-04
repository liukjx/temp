# 1. 定义一个Adder类
class Adder(object):
    # 2. 定义魔术方法
    def __init__(self, value=0):
        self.data = value

    def __call__(self, x):
        return self.data + x

# 3. 实例化对象
add = Adder()
print(add(1))
print(add(2))
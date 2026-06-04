'''
在Python中，print()不仅可以实现普通变量的打印输出，还可以使用f形式对其进行格式化输出，基本语法：
print(f'xxx{变量名称}xxx')
'''
# 案例1：定义两个变量 => name = 'Rose'，age = 19，期望的输出结果：我的名字叫做Rose，今年19岁了！
name = 'Rose'
age = 19
print(f'我的名字叫做{name}，今年{age}岁了！')

# 案例2：定义两个变量 = goods_name = '胡萝卜', goods_price = 5.5，期望输出结果：今天蔬菜特价了，胡萝卜只要5.50元/斤！
goods_name = '胡萝卜'
goods_price = 5.5
print(f'今天蔬菜特价了，{goods_name}只要{goods_price:.2f}元/斤！')

'''
切片三步走：① 看步长 ② 绘图像 ③ 记口诀
基本语法：
    列表名称[起始索引:结束索引:步长]

① 看步长，步长为正则从左向右移动，步长为负，则从右向左移动
② 绘制图像，把列表元素值，与正索引、负索引绘制出来
③ 记口诀，切片其实很简单，只顾头来尾不管，步长为正则正向移动，步长为负则你想移动。
'''
abcd_list = ['a', 'b', 'c', 'd']
print(abcd_list[0:3:1])  # 1，代表从左向右移动 => abc
print(abcd_list[0:3])

print(abcd_list[0:])  # 从start（0）位置开始截取，一直截取到列表尾部（包含尾部元素）
print(abcd_list[:3])  # 从0开始截取，截取到stop-1结束
print(abcd_list[:])  # 截取整个列表
print(abcd_list[::-1])  # dcba
print(abcd_list[-4:-1])  # abc

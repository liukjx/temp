"""
在python中，range方法主要作用是用来生成一个容器对象range(5) ->
                                    存储了5个对象：0 1 2 3 4
其内部方法一般是一个数字，代表指定长度的数据容器
元素特点：顾头不顾尾 元素：0~4 长度是5

写法：
for 临时变量 in 数据容器:

完整格式
range(start, stop[, step])
start:开始
stop：结束
step：步长
"""
#如果只传入一个参数 默认开头为0 ，结尾是5  默认步长为 1
# for temp in range(5):
#     print(temp)
# for temp in range(0,5,1):
#     print(temp)

# #star stop
# for temp in range(1,9):
#     print(temp)
#
# for temp in range(5,10):
#     print(temp)

#需求 使用range打印0~100偶数
# for t in range(0,101,2):
#     print(t)

#奇数
for t in range(1,100,2):
    print(t)

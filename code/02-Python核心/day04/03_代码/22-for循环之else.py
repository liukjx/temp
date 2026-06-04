"""
在python中，循环无论是while还是for都存在一个特殊结构else
格式：
    while基本语法：
        while 循环条件:
            ....
        else:
            ....
    小结：当循环正常结果后，执行else里面内容

    for基本语法:
        for 临时变量 in 数据容器:
            .....
        else:
            .....
    小结：当循环正常结果后，执行else里面内容
所谓else指的是 循环正常结果后，要执行的代码，即如果出现break情况
else里面的代码不执行！！！！
即：循环没有正常结束，则else不执行
"""
#遇e案例  字符串中 ，遇到e break

# str1="ithima"  #数据容器
# for i in str1:
#     if i=="e":
#         print("我遇到e了")
#         break
# else:
#     print("哈哈哈哈哈哈哈执行了此代码")


str1="itheima"  #数据容器
for i in str1:
    if i=="a":
        print("我遇到a了")
        continue
else:
    print("哈哈哈哈哈哈哈执行了此代码")


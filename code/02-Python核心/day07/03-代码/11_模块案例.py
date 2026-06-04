"""
案例：求循环代码的执行时间
"""
import time


startime=time.time()
list1 =[]
for i in range(10000):
    for j in range(10000):
        for a in range(10000):
            list1.append(a)
endtime = time.time()
print(endtime-startime)

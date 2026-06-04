import torch
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

# 随机数
data = torch.randn([30,])*10
print(data)
plt.scatter(range(30),data)
plt.plot(range(30),data)
plt.show()


# 指数加权平均
temp = []
beta = 0.9
for i in range(30):
    if i == 0:
        temp.append(data[i])
    else:
        temp.append(temp[i-1]*beta+(1-beta)*data[i])

plt.plot(range(30),temp)
plt.show()
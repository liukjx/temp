import torch.nn as nn
import torch
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 曲线
# sigmoid = nn.Sigmoid()
# tanh = nn.Tanh()
# relu = nn.ReLU()
gelu = nn.GELU()
x = torch.linspace(-10, 10, 100)
# y = sigmoid(x)
# y = tanh(x)
# y = relu(x)
y = gelu(x)
plt.plot(x, y)
plt.grid(True)
plt.show()

# 导函数
x = torch.linspace(-10, 10, 100, requires_grad=True)
# sigmoid(x).sum().backward()
# tanh(x).sum().backward()
# relu(x).sum().backward()
gelu(x).sum().backward()
y = x.grad
x = x.detach()
plt.plot(x, y)
plt.grid(True)
plt.show()

# softmax
scores = torch.tensor([0.2, 0.02, 0.15, 0.15, 1.3, 0.5, 0.06, 1.1, 0.05, 3.75])
softmax =nn.Softmax()
print(softmax(scores))
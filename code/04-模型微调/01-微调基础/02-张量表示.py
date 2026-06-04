import torch
import numpy as np
# 标量
print(torch.tensor(5))
print(5)

# 向量
print([2, 3, 5, 6, 7])
print(torch.tensor([2, 3, 5, 6, 7]))

# 矩阵
data_np = np.random.randn(2, 3)
print(data_np)
print(torch.tensor(data_np))

# 三维
data_np = np.random.randn(2, 3, 2,3)
print(data_np)
print(torch.tensor(data_np))
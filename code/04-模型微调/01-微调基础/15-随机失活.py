import torch.nn as nn
import torch

# 层
layer = nn.Linear(in_features=3, out_features=5)
dropout = nn.Dropout(p=0.5)

# 数据
data = torch.randn(1, 3)
output = layer(data)
print(output)

# 失活
output = dropout(output)
print(output)

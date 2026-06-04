from torch import nn
import torch

# # 交叉熵
# loss = nn.CrossEntropyLoss()
# # 真实值
# # y_true = torch.tensor([1,1,8],dtype=torch.int64)
# y_true = torch.tensor([[1,0,0],[0,1,0],[0,0,1]],dtype=torch.float32)
#
# # 预测值
# y_pre = torch.tensor([[0.7,0.2,0.1],[0.2,0.6,0.2],[0.1,0.2,0.7]],dtype=torch.float32)
#
# print(loss(y_pre, y_true))

# 二分类交叉熵
loss = nn.BCELoss()

# 真实值
y_true = torch.tensor([0, 0, 1], dtype=torch.float32)
# 预测值
y_pre = torch.tensor([0.2, 0.3, 0.9], dtype=torch.float32)

print(loss(y_pre, y_true))

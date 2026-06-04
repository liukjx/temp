from torch.utils.data import Dataset, DataLoader
from torch import nn, optim
import torch

# 数据
# 包装特征和标签
dataset = Dataset()
# batch
dataloader = DataLoader(dataset=dataset, batch_size=4, shuffle=True)

# 模型 + 失活 + Norm
class model(nn.Module):
    def __init__(self):
        super(model, self).__init__()
        pass

    def forward(self, x):
        out = x
        return out

model = model()

# 优化器
optimizer = optim.Adam(model.parameters(), lr=0.001, betas=(0.9, 0.999))

# 损失实例化
loss = nn.CrossEntropyLoss()

# 遍历epoch
epochs = 100
for epoch in range(epochs):
    # 遍历batch
    for (x, y) in dataloader:
        # 模型预测
        y_pre = model(x)
        # 计算损失
        loss_value = loss(y_pre, y)
        # 反向传播
        optimizer.zero_grad()
        loss_value.backward()
        optimizer.step()

    # 模型验证
    with torch.no_grad():
        # 验证集数据
        y = model(x)
        # 评估方式
        # 准确率、损失、精确率、召回率、F1

    # 模型保存
    torch.save(model.state_dict(), 'path')

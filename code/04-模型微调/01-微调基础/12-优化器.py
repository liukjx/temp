import torch

# 权重(模型)
w = torch.tensor([1.], requires_grad=True)
# loss
loss = 0.5 * (w ** 2).sum()

# 优化器
# optimizer = torch.optim.SGD(params=[w], lr=0.2)
optimizer = torch.optim.Adam(params=[w], lr=0.2,betas=(0.9,0.99))

# # 反向传播
# optimizer.zero_grad()
# loss.backward()
# optimizer.step()
#
# print(w.grad)
# print(w)
#
# # loss
# loss = 0.5 * (w ** 2).sum()
#
# # 反向传播
# optimizer.zero_grad()
# loss.backward()
# optimizer.step()
#
# print(w.grad)
# print(w)
# epochs
for epoch in range(10):
    # batch
    for i in range(100):
        # 模型预测
        # loss
        loss = 0.5 * (w ** 2).sum()

        # # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(w.grad)
        print(w)


import pandas as pd  # pip install pandas
import numpy as np
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader
import torch
from torch import nn
from torchsummary import summary
from torch import optim
import time


def create_dataset():
    # 读取数据pandas -> 特征x和目标值y/label
    data = pd.read_csv('data\手机价格预测.csv')
    # print(data.head())
    y = data.iloc[:, -1].astype(np.int64)
    # print(y.head())
    x = data.iloc[:, :-1].astype(np.float32)
    # print(x.head())

    # 数据划分： 训练和测试
    x_train, x_val, y_train, y_val = train_test_split(x, y, train_size=0.8, random_state=22)
    print(x_train.shape, x_val.shape, y_train.shape, y_val.shape)
    # TensorDataset
    train_dataset = TensorDataset(torch.tensor(x_train.values), torch.tensor(y_train.values))
    val_dataset = TensorDataset(torch.tensor(x_val.values), torch.tensor(y_val.values))
    # print(train_dataset, val_dataset)
    return train_dataset, val_dataset


# 构建模型:输入维度：20 输出维度：4
class Model(nn.Module):
    def __init__(self, input_size, output_size):
        super(Model, self).__init__()
        self.linear1 = nn.Linear(input_size, 128)
        self.norm1 = nn.LayerNorm(128)
        self.linear2 = nn.Linear(128, 50)
        self.dropout = nn.Dropout(p=0.2)
        self.linear3 = nn.Linear(50, 20)
        self.out = nn.Linear(20, output_size)

    def forward(self, x):
        x = torch.relu(self.norm1(self.linear1(x)))
        x = self.dropout(torch.relu(self.linear2(x)))
        x = torch.relu(self.linear3(x))
        # out = torch.softmax(self.out(x),dim=1)
        out = self.out(x)
        return out


# 模型训练
def train(dataset):
    # 数据
    dataloader = DataLoader(dataset=dataset, batch_size=18, shuffle=True)
    # 模型
    model = Model(input_size=20, output_size=4)
    # 优化器
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    # 损失函数
    error = nn.CrossEntropyLoss()
    # 遍历epoch
    epochs = 20
    for epoch in range(epochs):
        start = time.time()
        loss_sum = 0.0
        num = 0.001
        # 遍历dataloader
        for id, (x, y) in enumerate(dataloader):
            # 前向传播
            y_pre = model(x)
            # 计算损失
            loss = error(y_pre, y)
            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            loss_sum += loss.item()
            num += 1
        loss_mean = loss_sum / num
        # 输出日志
        print('Epoch: {}/{}, Loss: {:.4f},time:{}'.format(epoch + 1, epochs, loss_mean, time.time() - start))
    # 模型保存
    torch.save(model.state_dict(), 'model.pth')


# 模型评估

def test(dataset):
    # 加载训练好的模型
    model = Model(input_size=20, output_size=4)
    weights = torch.load('model.pth')
    model.load_state_dict(weights)
    # 获取测试集数据
    dataloader = DataLoader(dataset, batch_size=8, shuffle=True)
    # 预测
    correct = 0
    for x, y in dataloader:
        y_pred = model(x)
        y_pred = torch.argmax(y_pred, dim=1)
        correct_batch = (y_pred == y).sum()
        correct += correct_batch
    # 准确率
    acc = correct / len(dataset)
    return acc


if __name__ == '__main__':
    train_dataset, val_dataset = create_dataset()
    # # Dataloader
    # train_dataloader = DataLoader(dataset=train_dataset, batch_size=4, shuffle=True)
    # val_dataloader = DataLoader(dataset=val_dataset, batch_size=4, shuffle=True)
    #
    # for (x, y) in train_dataloader:
    #     print(x)
    #     print(y)
    #     break
    # model = Model(input_size=20,output_size=4)
    # print(model)
    # summary(model,input_size=(20,),batch_size=5)
    # train(train_dataset)
    acc = test(val_dataset)
    print(acc)

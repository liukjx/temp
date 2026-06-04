from torch import nn
import torch
from torchsummary import summary


# 类
class model(nn.Module):
    # 初始化 定义层
    def __init__(self):
        super(model, self).__init__()
        self.Linear1 = nn.Linear(in_features=5, out_features=3)
        self.norm1 = nn.LayerNorm(3)
        self.dropout1 = nn.Dropout(0.4)
        # self.tanh = nn.Tanh()
        self.Linear2 = nn.Linear(in_features=3, out_features=2)
        self.norm2 = nn.LayerNorm(2)
        self.dropout2 = nn.Dropout(0.8)
        # self.relu = nn.ReLU()
        self.out = nn.Linear(in_features=2, out_features=2)
        # self.softmax = nn.Softmax(dim=1)

    # forward 数据流动
    def forward(self, x):
        # x = self.tanh(self.Linear1(x))
        x = torch.tanh(self.norm1(self.Linear1(x)))
        # print(x)
        # x = self.dropout1(x)
        # print(x)
        # x = self.relu(self.Linear2(x))
        x = torch.relu(self.Linear2(x))
        print(x)
        x = self.norm2(x)
        print(x)
        x = self.dropout2(x)
        print(x)

        # out = self.softmax(self.out(x))
        out = torch.softmax(self.out(x), dim=1)
        return out


if __name__ == '__main__':
    model = model()
    print(model)
    data = torch.randn(1, 5)
    out = model(data)
    # print(out.shape)
    # print(out)
    # summary(model, input_size=(5,),batch_size=5)

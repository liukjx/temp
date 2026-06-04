# 训练
from dataprocess import dataset_dict, collate_fn
from torch.utils.data import DataLoader
from model import Model, pretrained_model
from torch import optim
import torch.nn as nn
import torch
import time


def train_model():
    # 数据
    dataloader = DataLoader(dataset=dataset_dict['valid'], shuffle=True, batch_size=8, collate_fn=collate_fn)
    # 模型
    bert_model = Model()
    # 优化器
    optimizer = optim.AdamW(bert_model.parameters(), lr=0.000001)
    for param in pretrained_model.parameters():
        param.requires_grad_(False)
    # 损失
    loss_function = nn.CrossEntropyLoss()
    bert_model.train()
    # 遍历 epoch
    epochs = 2
    for epoch in range(epochs):
        loss_sum = 0
        start = time.time()
        # 遍历batch
        for id, (input_ids, attention_mask_ids, token_type_ids, labels) in enumerate(dataloader):
            # 前向传播
            out = bert_model(input_ids, attention_mask_ids, token_type_ids)

            # 损失计算
            loss = loss_function(out, labels)
            loss_sum += loss.item()
            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if id % 5 == 0:
                acc = evaluate_model(dataset_dict['valid'], model=bert_model)
                print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f},acc: {:.4f} ,time: {:.4f}'.format(epoch + 1, epochs,
                                                                                                   id + 1,
                                                                                                   len(dataloader),
                                                                                                   loss_sum / (id + 0.1),
                                                                                                   acc,
                                                                                                   time.time() - start))
                start = time.time()

    torch.save(bert_model.state_dict(), 'weight/model_eval.pth')


def evaluate_model(dataset, model):
    # 设置下游任务模型为评估模式
    model.eval()
    # 设置评估参数
    correct = 0
    total = 0
    # 实例化化my_dataloader
    loader = DataLoader(dataset,
                        batch_size=8,
                        collate_fn=collate_fn,
                        shuffle=True,
                        drop_last=True)

    # 给模型送数据 测试预测结果
    for i, (input_ids, attention_mask, token_type_ids, labels) in enumerate(loader):
        # 预训练模型进行特征抽取
        with torch.no_grad():
            my_out = model(input_ids=input_ids,
                           attention_mask=attention_mask,
                           token_type_ids=token_type_ids)
        # 求预测结果
        out = my_out.argmax(dim=1)
        # 计算准确率
        correct += (out == labels).sum().item()
        total += len(labels)
    return correct / total


if __name__ == '__main__':
    # train_model()
    # 模型评估
    bert_model = Model()
    weights = torch.load('weight/model_eval.pth')
    bert_model.load_state_dict(weights)
    acc = evaluate_model(dataset_dict['test'], bert_model)
    print(acc)

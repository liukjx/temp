import jieba
from torch import nn
import torch

# 词表
vocab = {
    '<UNK>': 0,
    '教育': 1,
    '猫': 2,
    '狗': 3,
    '鱼': 4,
    '老鼠': 5,
    '跑': 6,
    '游泳': 7,
    '传智': 8
}

# 实例化nn.embeding
emb = nn.Embedding(len(vocab), 5)

# 句子-》分词-》嵌入-》获取嵌入结果
text = '猫吃老鼠'
words = jieba.lcut(text)

ids = []
for word in words:
    if word in vocab:
        ids.append(vocab[word])
    else:
        ids.append(0)

ids_tensor=torch.tensor(ids)

print(emb(ids_tensor).detach().numpy())

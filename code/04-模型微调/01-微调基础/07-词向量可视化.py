import jieba
from torch import nn
import torch
from sklearn.manifold import TSNE
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体，
# 设置font.sans-serif 或 font.family 均可
mpl.rcParams["font.sans-serif"] = ["Arial Unicode MS"] ## mac
plt.rcParams['font.family']=['Arial Unicode MS'] ## mac
mpl.rcParams["font.sans-serif"] = ["SimHei"] ## win
plt.rcParams['font.family']=['SimHei'] ## win
mpl.rcParams["axes.unicode_minus"] = False

# 词表-》句子-》词嵌入-》可视化

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
text = '猫吃老鼠,狗钓鱼，猫喜欢游泳'
words = jieba.lcut(text)

ids = []
labels = []
for word in words:
    if word in vocab:
        ids.append(vocab[word])
        labels.append(word)
    else:
        ids.append(0)
        labels.append('unknow')

ids_tensor = torch.tensor(ids)

vector = emb(ids_tensor).detach().numpy()
print(vector)
print(vector.shape)

tsne = TSNE(n_components=2, perplexity=2)
vector_tsne=tsne.fit_transform(vector)
print(vector_tsne.shape)

# 绘图
plt.figure(figsize=(12, 8))
plt.scatter(vector_tsne[:, 0], vector_tsne[:, 1], alpha=0.7)

for i, label in enumerate(labels):
    plt.annotate(label, (vector_tsne[i, 0], vector_tsne[i, 1]),
                 xytext=(5, 5), textcoords='offset points',
                 fontsize=12, alpha=0.8)

plt.title('词向量可视化 (t-SNE)')
plt.xlabel('t-SNE 维度 1')
plt.ylabel('t-SNE 维度 2')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()



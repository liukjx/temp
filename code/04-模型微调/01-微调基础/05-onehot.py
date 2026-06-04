import jieba
import numpy as np

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

# 句子
text = '猫吃老鼠'
words = jieba.lcut(text)
print(words)

# onehot
def onehot(w, vocab):
    vector = np.zeros(len(vocab))
    # print(vector)
    if w in vocab:
        id = vocab[w]
        vector[id] = 1
    else:
        id = vocab['<UNK>']
        vector[id] = 1
    print(vector)
    return vector

# 遍历分词结果
for w in words:
    onehot(w,vocab)



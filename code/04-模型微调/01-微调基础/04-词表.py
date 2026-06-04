import jieba
from collections import Counter

# 文本
texts = ['华为机器肯定不错，但第一次碰上京东最糟糕的服务，以后不想到京东购物了',
         '感觉还可以，没有磨损，应该是新机，用一段时间再评论。']

word_freq = Counter()
# 分词
for text in texts:
    words = jieba.lcut(text)
    word_freq.update(words)

# 统计词频
print(word_freq)


# 过滤次数少的
# word_freq = [item for item in word_freq.items() if item[1] > 1]
# print(word_freq)
# 构建词表
# print({word:id for id,(word, freq) in enumerate(word_freq)})
print({word:id for id,(word, freq) in enumerate([item for item in word_freq.items() if item[1] > 0])})

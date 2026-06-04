import jieba

text = '当时是因为要写读书报告 所以上网到处抄 就发现这本书感觉以前自己没看过中文版的骆驼祥子就看过电影所以决定买个英文的看看本来以为 是中文翻译过来的 不会太地道结果'

word_list = jieba.lcut(text)
print(word_list)

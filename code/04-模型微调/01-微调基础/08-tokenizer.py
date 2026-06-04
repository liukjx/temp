from transformers import AutoTokenizer,AutoModel


# 句子
texts = ['猫吃鱼','猫吃老鼠']
# text = '猫吃鱼'

# 分词
tokenizer = AutoTokenizer.from_pretrained(r'D:\北京java428\02-code\bert-base-chinese')
model = AutoModel.from_pretrained(r'D:\北京java428\02-code\bert-base-chinese')
print(model)

for text in texts:
    tokenized_text = tokenizer.tokenize(text)
    print(tokenized_text)
    tokenized_ids =tokenizer.encode(text)
    print(tokenized_ids)
    print(tokenizer.decode(tokenized_ids))
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
# 文本分类
# 加载分词器
tokenizer = AutoTokenizer.from_pretrained(
    r'D:\北京java428\02-code\02-AE\weights\models--distilbert-base-uncased-finetuned-sst-2-english')

# 模型
model = AutoModelForSequenceClassification.from_pretrained(
    r'D:\北京java428\02-code\02-AE\weights\models--distilbert-base-uncased-finetuned-sst-2-english')

# 数据预处理
text = 'I love this movie! The acting is amazing.'
tokenized_text = tokenizer(text, return_tensors='pt',padding=True) # 文本-》id
print(tokenized_text)
# 模型预测
# dropout
model.eval()
# w.grad
with torch.no_grad():
    model_output = model(**tokenized_text)
print(model_output)

# model(input_ids = tokenized_text['input_ids'], attention_mask = tokenized_text['attention_mask'])

# 后处理
logits = model_output.logits
# 概率值 [[0.0002,0.9998]]
props = torch.softmax(logits, dim=-1)
# 预测类别id=1
id = torch.argmax(props, dim=-1)
# 类别名称
label = model.config.id2label[id.item()]
# 概率值
prop = props[0][id.item()]
print([{'label': label, 'prob': prop.item()}])
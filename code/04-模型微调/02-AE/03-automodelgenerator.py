from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
# 分词器
tokenizer = AutoTokenizer.from_pretrained(r'D:\北京java428\\02-code\\02-AE\weights\gpt2-medium')
# 模型
model = AutoModelForCausalLM.from_pretrained(r'D:\北京java428\02-code\02-AE\weights\gpt2-medium')

# 处理数据
text = 'The future of AI is'
tokenized_text = tokenizer(text, return_tensors='pt') # 文本->id
print(tokenized_text)
# 模型预测
model.eval()
with torch.no_grad():
    generate_ids = model.generate(**tokenized_text,max_length=100)
print(generate_ids)
# model.generate(input_ids=tokenized_text['input_ids'], attention_mask=tokenized_text['attention_mask'])

# 解码文本
print(tokenizer.decode(generate_ids[0]))

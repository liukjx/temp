# 推理
from model import Model
import torch
from transformers import BertTokenizer


def predict(text):
    # 加载训练好的的模型
    bert_model = Model()
    weights = torch.load(r'D:\北京java428\02-code\02-AE\情感分析案例\weight\model_eval.pth')
    bert_model.load_state_dict(weights)
    bert_model.eval()
    # 数据处理
    tokenizer = BertTokenizer.from_pretrained(r'D:\北京java428\02-code\bert-base-chinese')
    inputs = tokenizer.encode_plus(text, return_tensors='pt')
    print(inputs)
    # 模型预测
    # out = bert_model(**inputs)
    out = bert_model(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'],
                     token_type_ids=inputs['token_type_ids'])

    # 后处理
    prop = torch.softmax(out, dim=1)
    id = torch.argmax(prop, dim=1).item()
    confidence = prop[0][id].item()
    if id ==0:
        class_name = '反面'
    else:
        class_name = '正面'
    return class_name, confidence


if __name__ == '__main__':
    class_name, confidence=predict('非常好')
    print(class_name, confidence)

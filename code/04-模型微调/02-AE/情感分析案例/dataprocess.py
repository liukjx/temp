# 数据
from datasets import load_dataset
from torch.utils.data import DataLoader
from transformers import BertTokenizer
import torch

dataset_dict = load_dataset('csv', data_files={
    'train': r'data\train.csv',
    'test': r'data\test.csv',
    'valid': r'data\validation.csv',
})

# print(dataset_dict['test'])
#
# for data in dataset_dict['test']:
#     print(data)
#     break

def collate_fn(data):
    # 文本
    texts = [i['text'] for i in data]
    # 分词-》id
    tokenizer = BertTokenizer.from_pretrained(r'D:\北京java428\02-code\bert-base-chinese')
    inputs = tokenizer.batch_encode_plus(batch_text_or_text_pairs=texts, max_length=32, padding='max_length',
                                         truncation=True,
                                         return_tensors='pt')
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']
    token_type_ids = inputs['token_type_ids']

    # 目标：int64
    labels = [i['label'] for i in data]
    labels = torch.LongTensor(labels)
    return input_ids, attention_mask, token_type_ids, labels


if __name__ == '__main__':
    dataloader = DataLoader(dataset=dataset_dict['valid'], batch_size=4, shuffle=True, collate_fn=collate_fn)
    for input_ids, attention_mask, token_type_ids, labels in dataloader:
        print(input_ids, attention_mask, token_type_ids, labels)
        print(input_ids.shape)
        print(attention_mask.shape)
        print(token_type_ids.shape)
        break

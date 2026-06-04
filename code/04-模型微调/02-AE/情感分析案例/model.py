# 模型
from torch import nn
from transformers import BertModel
import torch
from dataprocess import dataset_dict, collate_fn
from torch.utils.data import DataLoader

pretrained_model = BertModel.from_pretrained(r'D:\北京java428\02-code\bert-base-chinese')


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        # self.linear = nn.Linear(768, 256)
        # self.dropout = nn.Dropout(0.2)
        # self.out = nn.Linear(256, 2)
        self.out = nn.Linear(768, 2)

    def forward(self, input_ids, attention_mask, token_type_ids):
        with torch.no_grad():
            pooled_output = pretrained_model(input_ids, attention_mask, token_type_ids)
        # x = self.dropout(torch.relu(self.linear(pooled_output.pooler_output)))
        # output = self.out(x)
        output = self.out(pooled_output.pooler_output)
        return output


if __name__ == '__main__':
    dataloader = DataLoader(dataset=dataset_dict['valid'], batch_size=4, shuffle=True, collate_fn=collate_fn)
    model = Model()
    for input_ids, attention_mask, token_type_ids, labels in dataloader:
        # print(input_ids, attention_mask, token_type_ids, labels)
        # print(input_ids.shape)
        # print(attention_mask.shape)
        # print(token_type_ids.shape)
        out = model(input_ids, attention_mask, token_type_ids)
        print(out.shape)
        print(out)
        break

from datasets import load_dataset

# dataset = load_dataset('imdb')
# print(dataset['train'])

# for data in dataset['train']:
#     print(data['text'])

dataset = load_dataset('csv', data_files=r'D:\北京java428\02-code\02-AE\data\财经评论.csv')
print(dataset['train'])

for data in dataset['train']:
    print(data)
    break

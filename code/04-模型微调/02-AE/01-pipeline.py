from transformers import pipeline

# 文本分类
# classifier = pipeline(task='text-classification',
#                     model='distilbert/distilbert-base-uncased-finetuned-sst-2-english',device='cpu')

# classifier = pipeline(task='text-classification',
#                       model=r'D:\北京java428\02-code\02-AE\weights\models--distilbert-base-uncased-finetuned-sst-2-english',
#                       device='cpu')
#
# results = classifier('I love this movie! The acting is amazing.')
# print(results)

generator = pipeline('text-generation',
                    model=r'D:\北京java428\02-code\02-AE\weights\gpt2-medium',
                    device='cpu')
generated_text = generator('未来',max_length=100,temperature=0.7)
print(generated_text)

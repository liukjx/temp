# 需求：基于LangChain调用Tongyi，实现文本问答，Prompt：世界上最高的山峰是哪一座？

# 1. 导包.
from langchain_community.llms import Tongyi

# 2. 创建LLM模型.
llm = Tongyi(model='qwen-max')

# 3. 用while True死循环, 改成循环版
while True:
    # 4. 提示用户录入 提示词, 并接收.
    prompt = input('请输入您的问题: ')

    # 5. 向llm模型发起请求, 获取响应(处理)结果.
    result = llm.invoke(prompt)
    # 6. 打印结果.
    print(f'结果是: {result}')
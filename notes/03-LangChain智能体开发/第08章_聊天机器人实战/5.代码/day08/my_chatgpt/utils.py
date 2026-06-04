# 这里写的是: 核心业务逻辑, 即: 接收用户录入的 提示词(prompt), 调用模型, 然后获取结果.

# 1. 导包
from langchain_community.llms import Tongyi             # llm(大语言模型): 通义模型
from langchain.chains import ConversationChain          # 会话链, llm模型 + 记忆体
from langchain.prompts import ChatPromptTemplate        # 聊天模板
from langchain.memory import ConversationBufferMemory   # 会话记忆体

# 2. 定义1个函数, 用于根据用户录入的提示词, 调用模型, 获取结果.
def get_response(prompt, memory, api_key):
    """
    该函数用于根据用户录入的提示词, 调用模型, 获取结果.
    :param prompt: 用户录入的提示词
    :param memory: 会话记忆体
    :param api_key: 模型API密钥
    :return: 模型返回的结果
    """
    # 3. 创建模型对象.
    llm = Tongyi(model='qwen-max', dashscope_api_key=api_key)
    # 4. 创建会话链对象.
    chain = ConversationChain(llm=llm, memory=memory)
    # 5. 调用会话链对象, 获取结果.
    response = chain.invoke({'input': prompt})
    # 6. 返回结果.
    # return response              # 返回所有的结果, 包括: 提示词, 模型返回的结果, 以及会话历史记录.
    return response['response']  # 返回模型处理后的的结果.


# 在main函数中测试代码.
if __name__ == '__main__':
    # 1. 创建提示词对象.
    prompt = '世界上跑的最快的汽车是什么车?'

    # 2. 创建会话记忆体对象, return_messages: 是否返回会话历史记录.
    memory = ConversationBufferMemory(return_messages=True)

    # 3. 指定API_KEY
    api_key = 'sk-7e6996eb9a3643ce996b72e23cdc534a'

    # 4. 调用函数, 获取结果.
    result = get_response(prompt, memory, api_key)
    # 5. 打印结果.
    print(result)










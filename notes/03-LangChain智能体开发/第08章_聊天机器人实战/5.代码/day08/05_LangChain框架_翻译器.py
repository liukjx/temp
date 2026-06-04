# 需求：基于LangChain中的ChatPromptTemplate构建一个翻译器，英语翻译汉语 Prompt：I'm so hungry I could eat a horse

# 细节: 之所以有消息模板类, 是为了让用户更加精准的, 按照指定模板格式进行提问, 可以实现模型的精准查找等...

# 1. 导包.
from langchain_community.llms import Tongyi         # 通义模型
from langchain.prompts import ChatPromptTemplate    # 聊天模板

# 2. 构建模型对象.
llm = Tongyi(model='qwen-max')

# 3. 创建消息模板类的格式.
prompt_template = ChatPromptTemplate.from_messages([
    ('system', '你是一个专业的翻译器, 可以高效合理的把{input_language}翻译成{output_language}:'),
    ('human', '文本内容:{text}\n, 翻译的风格:{style}')
])

# 4. 构建消息模板, 传入指定的参数, 获取到具体的: prompt(提示词, 消息内容)
# 接收用户录入的要翻译的内容.
text = input('请输入要翻译的文本内容:')
prompt_value = prompt_template.invoke({
    'input_language': '英语',
    'output_language': '汉语',
    'text': text,
    'style': '文言文'
})

# 5. 调用模型, 获取翻译结果.
result = llm.invoke(prompt_value)
print(f'翻译后结果为: {result}')


# 上午代码写法, 没有指定模板类, 可能LLM(大语言模型)无法理解我们的文本含义
# prompt = "I'm so hungry I could eat a horse"
# print(llm.invoke(prompt))

# 上述的代码, 等价于这个代码.
prompt = """
你是一个专业的翻译器, 可以高效合理的把 英语 翻译成 汉语
文本内容: I\'m so hungry I could eat a horse
翻译的风格: 文言文
"""

prompt = """
你是一个专业的翻译器, 可以高效合理的把 英语 翻译成 汉语
文本内容: Good Good Study, Day Day Up!
翻译的风格: 文言文
"""

# 需求: 基于LangChain调用Tongyi，实现文本生成（文本扩写），Prompt：从前有一个美丽的小村庄，那里的人们过着宁静的生活。

# 1. 导包
from langchain_community.llms import Tongyi         # Large Language Models: 大语言模型

# 2. 创建提示词.
prompt = '从前有座山, 山里有座庙.'

# 3. 创建LLM模型，并调用接口。
# 参1: 模型名称, 参2: API密钥
# llm = Tongyi(
#     model='qwen-max',
#     dashscope_api_key='sk-51c83607d18d43b3873ce45fcc5956ee'
# )

# 细节1: 如果配置的有 密钥的Path环境变量(变量名必须是: DASHSCOPE_API_KEY), 则创建模型时, 可以省略密钥不写.
# 细节2: 部分Mac如果写 dashscope_api_key 参数不OK, 则将参数名改成: api_key
# 细节3: 配置完Path环境变量后, 记得重启PyCharm或者你的电脑后有效.
llm = Tongyi(model='qwen-max')

# 4. 调用接口，生成文本。 发起请求给模型, 获取响应.
result = llm.invoke(prompt)

# 5. 打印结果
print(f'提示词: {prompt}')
print(f'生成结果: {result}')
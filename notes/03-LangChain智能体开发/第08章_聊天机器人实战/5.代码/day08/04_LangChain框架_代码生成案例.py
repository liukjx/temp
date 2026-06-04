# 需求：基于LangChain调用Tongyi，实现代码生成，Prompt：请为以下功能生成Python代码：功能：计算两个数的最大公约数（GCD）

# 1. 导包.
from langchain_community.llms import Tongyi

# 2. 创建LLM模型
llm = Tongyi(model='qwen-max')

# 3. 定义 提示词.
# prompt = '''
# 请为以下功能生成Python代码：
# 功能：计算两个数的最大公约数（GCD）
# '''

prompt = '请为以下功能生成Python代码：冒泡排序'

# 4. 发起请求, 获取响应(处理)结果.
result = llm.invoke(prompt)

# 5. 打印结果.
print(result)
"""
该模块用来充当聊天机器人的后端模块，即接受前端（streamlit）消息传过来给用户
交给大模型（qwen，deepseek）获取对应的结果，返回给前端
"""

#1.导包
import ollama

#2.定义函数，给大语言模型发送请求，获取其处理结果（聊天机器人回答）
#解释：接受用户从前端传过来提示词
# def get_response(prompt):
#     #指定模型 ，   传递角色  和提示词
#     response=ollama.chat(model="qwen2:1.5b",
#                 messages=[{"role": "user","content": prompt}])
#     return response

def get_response(prompt):
    #指定模型 ，   传递角色  和提示词
    response=ollama.chat(model="qwen2:1.5b",
                messages=prompt)
    return response.message.content


#魔术方法  __name__ 脚本程序入口 打印 __main__
if __name__ =='__main__':
    prompt="你知道周杰伦吗？"
    response= get_response(prompt)
    print(response)









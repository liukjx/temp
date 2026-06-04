# 这里写的是: Python代码 -> 通过Streamlit, 绘制Web页面.

# 导包
import streamlit as st                                  # 把Python代码 -> Web页面的
from langchain.memory import ConversationBufferMemory   # 会话记忆体
from utils import get_response

# 1. 设置左侧的侧边栏.
with st.sidebar:
    # 让用户录入他/她的API KEY
    api_key = st.text_input('请输入Tongyi账号的API Key:', type='password')
    # 设置链接提示, 用户点击后, 会跳转到: 获取API Key的页面.
    st.markdown('[获取Tongyi账号的API Key](https://bailian.console.aliyun.com/?apiKey=1#/api-key)')

# 2. 设置页面标题.
st.title('通义聊天机器人')

# 3. 创建会话记忆体, 即: 会话保持对象, 记录: 聊天记录.
if 'memory' not in st.session_state:
    # 走这里, 说明用户第一次访问该页面, 则创建一个会话记忆体.
    st.session_state['memory'] = ConversationBufferMemory()
    st.session_state['messages'] = [{'role': 'ai', 'content': '你好, 我是你的AI助手, 有什么可以帮助你的吗?'}]

# 4. 创建消息区, 即: 遍历会话记忆体中的所有聊天记录, 并打印到消息区即可.
for message in st.session_state['messages']:
    # message的数据格式: {'role': 'ai', 'content': '你好, 我是你的AI助手, 有什么可以帮助你的吗?'}
    with st.chat_message(message['role']):  # 设置角色, 即: 显示消息来源.
        st.write(message['content'])        # 显示消息内容.

# 5. 创建文本框, 接收用户录入的问题.
prompt = st.chat_input('请录入您的问题: ')
# 6. 判断如果用户录入的内容不为空, 程序就继续执行.
if prompt:
    # 7. 判断用户是否已经录入了API KEY, 如果没有录入, 则提示用户录入.
    if not api_key:
        st.warning('请先录入API KEY!')
        st.stop()       # 程序停止运行.

    # 8. 走到这里, 说明:  ①: 用户录入了API Key    ②: 用户录入了具体的问题
    # 把用户录入的信息, 添加到: 会话记忆体中.
    st.session_state['messages'].append({'role': 'human', 'content': prompt})
    # 把用户录入的信息, 打印到: 消息区中.
    st.chat_message('human').markdown(prompt)

    # 9. 调用自定义函数, 获取AI回复的结果.
    # 细节: 加入等待提示.
    with st.spinner('AI正在思考中...'):
        response = get_response(prompt, st.session_state['memory'], api_key)

    # 10. 把AI的回复, 添加到: 会话记忆体中, 并打印到: 消息区中.
    st.session_state['messages'].append({'role': 'ai', 'content': response})
    st.chat_message('ai').markdown(response)

# 目的: 带着大家回顾下昨天讲解的Streamlit框架.
# 1. 导包
import streamlit as st

# 2. 搭建左侧的导航栏(侧边栏)
with st.sidebar:
    api_key = st.text_input('请输入Tongyi账号的API KEY:', type='password')

# 3. 设置标题.
st.title('通义聊天机器人')
# st.markdown('### 通义聊天机器人')    # streamlit支持markdown格式, 这里的### 表示三级主题.

# 4. 绘制分割线.
st.divider()

# 5. 创建一个文本输出框, 输出机器人的回答.
with st.chat_message("assistant"):  # assistant: 助理 -> 机器人.
    st.write('您好, 我是您的AI助手, 有什么可以帮助您的吗?')

# 6. 创建一个文本输入框, 输入要提问的问题.
with st.chat_message("user"):       # user: 用户
    st.write("Hello 👋")

# 7. 创建提问消息的文本框.
st.chat_input('请录入您要提问的问题: ')
import  streamlit as st
#1.聊天信息框
input_str=st.chat_input("请输入您要问的问题")
if input_str:
    st.write(f"您是输入的问题是{input_str}")

#2。角色信息框
with st.chat_message("user"):
    st.write("hello AI，我是人")

with st.chat_message("assistant"):
    st.write("hello 人，我是AI")
#这是另一种写法，除了写法不同，其他的都一样
symsg = st.chat_message("user")
symsg.write("很高兴认识你")
symsg = st.chat_message("assistant")
symsg.write("我也很高兴认识你")
symsg = st.chat_message("user")
symsg.write("/bye")
symsg = st.chat_message("assistant")
symsg.write("不讲武德")




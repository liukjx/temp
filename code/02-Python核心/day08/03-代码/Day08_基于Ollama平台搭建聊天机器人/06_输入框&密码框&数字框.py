import streamlit as st
#1.文本框
#输入普通文本
input_str =st.text_input("请输入您要问的问题？")
if input_str:  #input_str如果为空，结果false ，否则True
    print(f"您的问题是{input_str}")

#2.密码输入框
input_pwd=st.text_input("请输入您的登录密码",type="password")
if input_pwd:
    print(f"您的密码是{input_pwd}")

#3.数字输入框
# 参1：标题  参2：最小值  参3：最大值  参4：默认值  参5：步长
st.number_input("请录入您的年龄",min_value=18,max_value=80,value=18,step=1)

#4.多行文本
msg=st.text_area("请输入您的留言")
if msg:
    print(msg)
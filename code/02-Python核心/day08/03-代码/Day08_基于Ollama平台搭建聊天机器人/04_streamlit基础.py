import streamlit as st
"""
部署格式：
        在终端中运行 streamlit run 模块名称 
"""
#1.标题
st.title("streamlit 初体验")
#2.段落
st.write("鹅鹅鹅，曲项向天歌")
st.write("白毛浮绿水")
#3.标题
'# 1级标题'
'## 我是二级标题'
'### 我是三级标题'
'##### 我是五级标题'
#4.分割线
st.divider()

#4.演示markdown 函数 等价write
st.markdown("# 一级标题")
st.markdown("## 二级标题")

#5.展示图片
st.image("E:\\workspace\\AI35\\Day08_基于Ollama平台搭建聊天机器人\\a.jpg",width=400)


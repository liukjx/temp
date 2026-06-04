"""
案例： streamlit 输入框相关

步骤：
    ①导包
    ②：调用对应功能  st.table
"""
import streamlit as st
import pandas as pd
st.table(
        {'name':['张三','李四','王五'],
          'age':[23,34,56],
          'gender':['男','男','男']}
)

st.markdown("静态表格之pandas演示")
#拓展： 可以使用pandas dataframe
df=pd.DataFrame(
{'name':['张三','李四','王五'],
  'age':[23,34,56],
  'gender':['男','男','男']}
)
#静态
st.table(df)


st.markdown("动态表格演示")
#st.dataframe 创建动态表格
st.dataframe({'name':['张三','李四','王五'],
  'age':[23,34,56],
  'gender':['男','男','男']})

#使用pandas DataFrame
st.markdown("动态表格演示之DataFrame")
df=pd.DataFrame({'name':['张三','李四','王五'],
  'age':[23,34,56],
  'gender':['男','男','男']})
st.dataframe(df)

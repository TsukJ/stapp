import streamlit as st
from PIL import Image


class Page:
    def __init__(self, exp_id):
        self.exp_id = exp_id

    def run(self):
        st.title('制药工程实验辅助系统')
        st.text('作者：华南理工大学 19级应用化学 冯铠杰')
        st.text('指导老师：华南理工大学 方利国')
        st.header('使用指南')
        st.text('←拉出侧边栏后可以选择实验与页面')
        st.text('学习页面')
        st.text('点击学习开始按钮开始计时，点击学习结束按钮结束计时')
        st.text('测试页面')
        st.text('做完题目后点击结束测试按钮显示成绩')
        st.text('数据处理页面')
        st.text('在数据输入框中输入数据并按下回车键确认后得到结果')

import streamlit as st
import settings


class Menu:
    def __init__(self):
        self.user_id = None
        self.user_name = None
        self.exp_name = None
        self.exp_id = 0
        self.page_name = None
        self.page = None

    def run(self):
        e_l = settings.exp_list
        p_l = settings.page_list
        # 调用设置
        self.exp_name = st.sidebar.selectbox(
            label='选择实验↓',
            options=e_l
        )
        # 实验选择箱
        for i in range(len(e_l)):
            if self.exp_name == e_l[i]:
                self.exp_id = i
        # 将实验名转换为实验编码
        self.page_name = st.sidebar.selectbox(
            label='选择页面↓',
            options=list(p_l.keys())
        )
        # 页面选择箱
        self.page = p_l[self.page_name].Page(self.exp_id)
        # 创建页面对象
        self.user_id = st.sidebar.text_input('学号↓', value='200100010001')
        self.user_name = st.sidebar.text_input('姓名↓', value='张三')
        st.session_state['dev_mode'] = st.sidebar.checkbox('开发者模式（仅单机可用）')
        # 判断开发者模式开关
        if st.session_state['dev_mode']:
            d_l = settings.page_list_dev
            self.page_name = st.sidebar.selectbox(
                label='选择页面↓',
                options=list(d_l.keys())
            )
            self.page = d_l[self.page_name].Page()
        # 选择并创建开发者模式页面对象


if __name__ == '__main__':
    menu = Menu()  # 创建菜单对象
    menu.run()  # 菜单运行方法
    menu.page.run()  # 页面运行方法

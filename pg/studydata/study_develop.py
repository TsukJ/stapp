import json
import streamlit as st
from PIL import Image


class Page:
    def __init__(self):
        self.file = "pg/studydata/datafile.json"
        with open(self.file, 'r') as file:
            self.data = json.load(file)
        file.close()
        self.init_dict = {"实验目的": [],
                          "实验原理": [],
                          "实验仪器": [],
                          "实验步骤": [],
                          "注意事项": [],
                          "实验结果与讨论": [],
                          "思考题": []}
        if 'adding_data' not in st.session_state:
            st.session_state['adding_data'] = self.init_dict

    def getData(self):
        self.data: list = json.load(open(self.file, 'r'))

    def writeData(self):
        with open(self.file, "w") as file:
            json.dump(st.session_state['adding_data'], file, ensure_ascii=False, indent=2)
        file.close()

    def run(self):
        adding_step = st.radio('要增加的数据为', st.session_state['adding_data'].keys(),
                               horizontal=True)
        adding_text = st.text_area("请输入" + adding_step)
        col_l1, col_r1 = st.columns([9, 1])
        with col_l1:
            adding_type = st.radio(label='格式为:', options=["文本", "图片", "标题"], horizontal=True)
        with col_r1:
            if st.button('应用'):
                st.session_state['adding_data'][adding_step].append({adding_type: adding_text})
            if st.button('返回'):
                st.session_state['adding_data'].update({adding_step: []})

        st.header('文件内容预览↓')
        st.write(st.session_state['adding_data'])
        col_l2, col_r2 = st.columns([9, 1])
        with col_r2:
            if st.button('刷新'):
                st.session_state['adding_data'] = self.init_dict
        self.writeData()

        st.header('效果预览↓')
        st.write('---')
        ad = st.session_state['adding_data']
        url = 'pg/studydata/'
        for title in ad.keys():
            if ad[title] != []:
                st.header(title)
            for i in ad[title]:
                if i.get('文本', None) is not None:
                    st.write(i['文本'])
                elif i.get('标题', None) is not None:
                    st.header(i['标题'])
                else:
                    st.image(Image.open(url + i['图片']))

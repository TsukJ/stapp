import json
import streamlit as st


class Page:
    def __init__(self):
        self.file = "pg/studydata/exam.json"
        self.data = []
        self.init_list = []
        if 'exam_data' not in st.session_state:
            st.session_state['exam_data'] = []

    def getData(self):
        self.data: list = json.load(open(self.file, 'r'))

    def writeData(self, json_data):
        if st.button('写入'):
            json.dump(json_data, open(self.file, 'w'))

    def run(self):
        self.init_list.append(st.text_area("请输入题干"))
        self.init_list.append(str(st.text_area("请输入A选项")))
        self.init_list.append(str(st.text_area("请输入B选项")))
        self.init_list.append(str(st.text_area("请输入C选项")))
        self.init_list.append(str(st.text_area("请输入D选项")))
        dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
        raw_ans = st.radio('答案为', ['A', 'B', 'C', 'D'], horizontal=True)
        self.init_list.append(dic[raw_ans])
        col_l1, col_r1 = st.columns([9, 1])
        with col_r1:
            if st.button('应用'):
                st.session_state['exam_data'].append(self.init_list)

        data = json.dumps(st.session_state['exam_data'])
        st.text_area('预览', data)
        col_l2, col_r2 = st.columns([9, 1])
        with col_r2:
            if st.button('刷新'):
                st.session_state['exam_data'] = []
        with col_l2:
            self.writeData(data)

        ad = st.session_state['exam_data']
        col_l3, col_r3 = st.columns([9, 1])
        all_mark = 0
        with col_l3:
            for index in range(len(ad)):
                i = ad[index]
                op = [i[1], i[2], i[3], i[4]]
                res = st.radio(label=str(index+1) + '.' + i[0], options=op)
                ans = i[5]
                if res == i[ans]:
                    all_mark += 1
        with col_r3:
            if ad:
                st.header("你的成绩是")
                st.header(all_mark)

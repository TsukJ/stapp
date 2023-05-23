import streamlit as st
import json
import random


class Page:
    def __init__(self, exp_id):
        self.exp_id = exp_id

    def run(self):
        url = 'pg/studydata/exp' + str(self.exp_id) + '/'
        data_raw = json.load(open(url + 'exam.json', 'r'))
        data = json.loads(data_raw)
        data_length = len(data)
        all_mark = 0
        with st.container():
            colMid, colRight = st.columns([8, 2])
        with colRight:
            if st.button('刷新题库'):
                if data_length > 10:
                    index_selected = random.sample(range(data_length), 10)
                else:
                    index_selected = random.sample(range(data_length), data_length)
                    st.session_state['exam_data_selected'] = []
                    for i in index_selected:
                        st.session_state['exam_data_selected'].append(data[i])
        if st.session_state.get('exam_data_selected') is None:
            if data_length > 10:
                index_selected = random.sample(range(data_length), 10)
            else:
                index_selected = random.sample(range(data_length), data_length)
            st.session_state['exam_data_selected'] = []
            for i in index_selected:
                st.session_state['exam_data_selected'].append(data[i])
        with colMid:
            dt = st.session_state['exam_data_selected']
            for index in range(len(dt)):
                i = dt[index]
                op = [i[1], i[2], i[3], i[4]]
                res = st.radio(label=str(index + 1) + '.' + i[0], options=op)
                ans = i[5]
                if res == i[ans]:
                    all_mark += 1
        with colRight:
            if st.button("结束测试"):
                st.header("正确率:")
                percent = all_mark/len(dt)
                st.header("{:.2%}".format(percent))
                st.header("得分:")
                st.header(int(percent*100))

import streamlit as st
import json


class Page:
    def __init__(self, exp_id):
        self.exp_id = exp_id

    def run(self):
        url = 'pg/studydata/exp' + str(self.exp_id) + '/'
        data_raw = json.load(open(url + 'exam.json', 'r'))
        data = json.loads(data_raw)
        all_mark = 0
        with st.container():
            colMid, colRight = st.columns([8, 2])
        with colMid:
            for index in range(len(data)):
                i = data[index]
                op = [i[1], i[2], i[3], i[4]]
                res = st.radio(label=str(index + 1) + '.' + i[0], options=op)
                ans = i[5]
                if res == i[ans]:
                    all_mark += 1
        with colRight:
            if st.button("结束测试"):
                st.header("你的成绩是")
                st.header(all_mark)

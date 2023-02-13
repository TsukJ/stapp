import streamlit as st
from pg.examdata import test_main as test


def exampg(expID, uID, uName):
    allMark = 0
    data = test.data(expID=expID)
    with st.container():
        colMid, colRight = st.columns([8, 2])
    with colMid:
        with st.container():
            for i in data:
                op = [i[1], i[2], i[3], i[4]]
                res = st.radio(label=i[0], options=op)
                ans = i[5]
                if res == i[ans]:
                    allMark += 1
    with colRight:
        if st.button("结束测试"):
            st.header("你的成绩是")
            st.header(allMark)

import streamlit as st
import pandas as pd

def exampg(expID, uID, uName):
    allMark = 0
    data = pd.read_csv("./pg/examdata/test{}.csv".format(expID))
    with st.container():
        colMid,colRight = st.columns([8,2])
    with colMid :
        with st.container():
            for i in data.index.to_list():
                op =[("A:"+data.iat[i,1]),
                    ("B:"+data.iat[i,2]),
                    ("C:"+data.iat[i,3]),
                    ("D:"+data.iat[i,4])]
                res = st.radio(label=str(data.iat[i,0]),options=op,args=(1,2,3,4))
                ans = data.iat[i,5] - 1
                if res == op[ans]:
                    allMark += 1
    with colRight:
        if st.button("结束测试"):
            st.header("你的成绩是")
            st.header(allMark)


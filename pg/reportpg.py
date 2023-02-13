import streamlit as st
import pandas as pd
from tools import mathtools

def reportpg(expID, uID, uName):
    if expID == 0:
        with st.container():
            st.header('样品含量测定')
            y = st.number_input(label='样品吸光度', value=1.000)
            st.text_input(label='样品含量mg/L', value=(y - 0.0025)/0.0275)
            st.header('单线态氧含量测定')
            with st.container():
                st.subheader('标准曲线')
                st.write('浓度单位 10^-5 mol/L')
                col1, col2, col3, col4, col5,col6 = st.columns([1,1,1,1,1,1])
                with col1:
                    c1 = st.number_input(label='浓度1', value=1.25)
                    A1 = st.number_input('吸光度1')
                with col2:
                    c2 = st.number_input(label='浓度2', value=2.5)
                    A2 = st.number_input('吸光度2')
                with col3:
                    c3 = st.number_input(label='浓度3', value=5)
                    A3 = st.number_input('吸光度3')
                with col4:
                    c4 = st.number_input(label='浓度4', value=10)
                    A4 = st.number_input('吸光度4')
                with col5:
                    c5 = st.number_input(label='浓度5', value=20)
                    A5 = st.number_input('吸光度5')
                with col6:
                    c6 = st.number_input(label='浓度6', value=40)
                    A6 = st.number_input('吸光度6')
            argsx1 = [c1, c2, c3, c4, c5, c6]
            argsy1 = [A1, A2, A3, A4, A5, A6]
            result1 = mathtools.Lineindex(argsx1, argsy1)
            a1 = format(result1[0], '.3f')
            b1 = format(result1[1], '.3f')
            argsy1a = mathtools.Linedata(argsx1,result1[0],result1[1])
            st.write('拟合方程为')
            st.write('y = '+a1+'+'+b1+'x')
            dic1 = {
                '原始数据' : argsy1,
                '拟合曲线' : argsy1a
            }
            dt1 = pd.DataFrame(dic1,index=argsx1)
            st.line_chart(dt1)
            st.subheader('样品曲线')
            st.write('时间单位 min')
            col1a, col2a, col3a, col4a, col5a, col6a = st.columns([1, 1, 1, 1, 1, 1])
            with col1a:
                t1 = st.number_input(label='时间1', value=10)
                A1a = st.number_input('吸光度1',key='1a')
            with col2a:
                t2 = st.number_input(label='时间2', value=20)
                A2a = st.number_input('吸光度2',key='2a')
            with col3a:
                t3 = st.number_input(label='时间3', value=30)
                A3a = st.number_input('吸光度3',key='3a')
            with col4a:
                t4 = st.number_input(label='时间4', value=40)
                A4a = st.number_input('吸光度4',key='4a')
            with col5a:
                t5 = st.number_input(label='时间5', value=50)
                A5a = st.number_input('吸光度5',key='5a')
            with col6a:
                t6 = st.number_input(label='时间6', value=60)
                A6a = st.number_input('吸光度6',key='6a')
            argsx2 = [t1, t2, t3, t4, t5, t6]
            argsy2 = [A1a, A2a, A3a, A4a, A5a, A6a]
            dic2 = {
                '原始数据': argsy2
            }
            dt2 = pd.DataFrame(dic2, index=argsx2)
            st.line_chart(dt2)
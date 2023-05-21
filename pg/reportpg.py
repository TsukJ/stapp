import streamlit as st
import pandas as pd
import math
import numpy as np
from tools import mathtools


def DataInput(series_num: int, data_num: int, data_name: str, init_data=None):
    if data_num <= 6:
        col_args = st.columns(data_num)
    else:
        col_args = st.columns(6)
    data_args = []
    for i in range(data_num):
        row_num = i % 6
        with col_args[row_num]:
            if init_data is not None and i < len(init_data):
                value = str(init_data[i])
            else:
                value = 0
            data = st.text_input(label=data_name + str(i + 1), key=str(series_num) + data_name + str(i + 1),
                                 value=value)
            data_args.append(eval(data))
    return data_args


def LineChart(argx, argy, result):
    a1 = format(result[0], '.3f')
    b1 = format(result[1], '.3f')
    argsy1a = mathtools.Linedata(argx, result[0], result[1])
    st.markdown("拟合方程为：:green[$" + 'y = ' + a1 + '+' + b1 + 'x' + "$]")
    st.markdown('相关系数为：:green[' + str(result[2]) + ']')
    dic1 = {
        '原始数据': argy,
        '拟合曲线': argsy1a
    }
    dt1 = pd.DataFrame(dic1, index=argx)
    st.line_chart(dt1)


class Page:
    def __init__(self, exp_id):
        self.exp_id = exp_id

    def run(self):
        if self.exp_id == 0:
            st.header('样品含量测定')
            y = st.number_input(label='样品吸光度', value=1)
            st.caption('样品含量mg/L ：:blue[' + str((y - 0.0025) / 0.0275) + ']')
            st.header('单线态氧含量测定')
            st.subheader('标准曲线')
            st.write('浓度单位 10^-5 mol/L')
            col_num1 = math.floor(st.number_input('数据量', value=6, key='数据量1', min_value=1))
            data_arg = [1.25, 2.5, 5, 10, 20, 40]
            argsx1 = DataInput(0, col_num1, '浓度', data_arg)
            argsy1 = DataInput(0, col_num1, '吸光度')
            result1 = mathtools.Lineindex(argsx1, argsy1)
            LineChart(argsx1, argsy1, result1)
            st.subheader('样品曲线')
            st.write('时间单位 min')
            col_num2 = math.floor(st.number_input('数据量', value=6, key='数据量2', min_value=1))
            argsx2 = DataInput(1, col_num2, '时间', [10, 20, 30, 40, 50, 60])
            argsy2 = DataInput(1, col_num2, '吸光度')
            dic2 = {
                '原始数据': argsy2
            }
            dt2 = pd.DataFrame(dic2, index=argsx2)
            st.line_chart(dt2)

        elif self.exp_id == 2:
            st.header('内标法')
            st.header('相对校正因子测定')
            col_args1 = st.columns(2)
            with col_args1[0]:
                Wi = eval(st.text_input('氯霉素重量', 0))
                hi0 = eval(st.text_input('氯霉素的峰面积（峰高）', 0))
            with col_args1[1]:
                Wn = eval(st.text_input('对硝基苯酚的重量', 0))
                hn0 = eval(st.text_input('对硝基苯酚的峰面积（峰高）', 0))
            if Wn and hn0 and hi0 != 0:
                fn = (Wi / hi0) / (Wn / hn0)
            else:
                fn = None
            st.markdown('相对校正因子为：:green[' + str(fn) + ']')
            st.header('样品含量测定')
            col_args2 = st.columns(2)
            with col_args2[0]:
                hi1 = eval(st.text_input('氯霉素的峰高', 0))
            with col_args2[1]:
                hn1 = eval(st.text_input('样品的峰面积（峰高）', 0))
                wn1 = eval(st.text_input('样品的重量', 0))
            if fn is not None and hn1 * wn1 != 0:
                han_liang = hi1 * Wn * fn / (hn1 * wn1)
            else:
                han_liang = None
            st.markdown('百分含量为：:green[' + str(han_liang) + ']')
            st.header('外标法')
            st.header('标准曲线')
            argsx1 = DataInput(0, 5, '浓度')
            argsy1 = DataInput(0, 5, '峰高')
            result1 = mathtools.Lineindex(argsx1, argsy1)
            LineChart(argsx1, argsy1, result1)
            st.header('样品测定')
            yang_pin = eval(st.text_input('样品的峰面积（峰高）（外）', 0))
            c0 = result1[0] + yang_pin * result1[2]
            st.markdown('浓度为：:green[' + str(c0) + ']')

        else:
            st.header('本节无数据处理')

import streamlit as st
from PIL import Image
import time
import json


class Page:
    def __init__(self, exp_id):
        self.exp_id = exp_id

    def run(self):
        colLeft, colRight = st.columns([7, 3])
        with colRight:
            # 记录开始时间
            if st.button('学习开始'):
                st.session_state['sTime'] = time.time()
            # 记录结束时间
            if st.button('学习结束'):
                st.session_state['eTime'] = time.time()
                allTime = int(st.session_state.eTime - st.session_state.sTime) # 计算总时长
                # 显示总时长
                st.subheader('您学习了')
                st.subheader(str(allTime) + 's')

        with colLeft:
            # 获取地址
            url = 'pg/studydata/exp' + str(self.exp_id) + '/'
            # 获取数据并将字符串转换为对象
            data_raw = json.load(open(url+'datafile.json', 'r'))
            data = json.loads(data_raw)
            # 按规则显示数据
            for title in data.keys():
                if data[title] != []:
                    st.header(title)
                for i in data[title]:
                    if i.get('文本', None) is not None:
                        st.write(i['文本'])
                    elif i.get('标题', None) is not None:
                        st.header(i['标题'])
                    else:
                        st.image(Image.open(url+i['图片']))

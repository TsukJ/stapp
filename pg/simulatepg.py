import streamlit as st


class Page:
    def __init__(self, exp_id):
        self.exp_id = exp_id
        self.material = ['蚕砂', '水', '丙酮', '乙醚', '30%HCL', 'NaOH饱和溶液', 'DMF溶液', 'DPA溶液']
        self.instrument = ['圆底烧瓶', '水浴锅', '抽滤瓶', '旋转蒸发仪', '分液漏斗', '烧杯', '离心器', '干燥箱',
                           '天平', '容量瓶', '分光光度计', '控制时间']

    def run(self):
        if st.session_state.get('样品') is None:
            st.session_state['样品'] = []
        if st.session_state.get('实验模拟数据') is None:
            st.session_state['实验模拟数据'] = {}
            st.session_state['实验模拟数据']['按钮'] = {}
            st.session_state['实验模拟数据']['打开中'] = '蚕砂'
            for i in self.instrument:
                st.session_state['实验模拟数据'][i] = {}
        c1 = st.container()
        st.header('药品')
        col_args_1 = st.columns(4)
        for i in range(len(self.material)):
            row_num = i % 4
            with col_args_1[row_num]:
                st.session_state['实验模拟数据']['按钮'][self.material[i]] = st.button(self.material[i],
                                                                                       use_container_width=True)
        st.header('仪器')
        col_args_2 = st.columns(4)
        for i in range(len(self.instrument)):
            row_num = i % 4
            with col_args_2[row_num]:
                st.session_state['实验模拟数据']['按钮'][self.instrument[i]] = st.button(self.instrument[i],
                                                                                         use_container_width=True)
        st.header('操作')
        col_args_3 = st.columns(4)
        for i in st.session_state['实验模拟数据']['按钮']:
            if st.session_state['实验模拟数据']['按钮'][i]:
                st.session_state['实验模拟数据']['打开中'] = i
        if st.session_state['实验模拟数据']['打开中'] in self.material:
            with col_args_3[0]:
                amount = st.number_input('提取量', step=50.0)
            with col_args_3[3]:
                if st.button('确认提取', use_container_width=True):
                    st.session_state['实验模拟数据']['手中'] = [st.session_state['实验模拟数据']['打开中'], amount]


        elif st.session_state['实验模拟数据']['打开中'] == '圆底烧瓶':
            if st.session_state['实验模拟数据'].get('圆底烧瓶') is None:
                st.session_state['实验模拟数据']['圆底烧瓶'] = {}
            with col_args_3[0]:
                if st.button('放入物质', use_container_width=True) and st.session_state['实验模拟数据'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据']['圆底烧瓶'][st.session_state['实验模拟数据']['手中'][0]] = \
                        st.session_state['实验模拟数据']['圆底烧瓶'].get(st.session_state['实验模拟数据']['手中'][0],
                                                                         0) + st.session_state['实验模拟数据']['手中'][
                            1]
                    st.session_state['实验模拟数据']['手中'] = None
            with col_args_3[1]:
                if st.button('倒出物质', use_container_width=True):
                    st.session_state['实验模拟数据']['圆底烧瓶'] = {}
            with col_args_3[2]:
                if st.button('拿起仪器', use_container_width=True):
                    st.session_state['实验模拟数据']['手中'] = ['圆底烧瓶', 1]
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据']['圆底烧瓶'])


        elif st.session_state['实验模拟数据']['打开中'] == '水浴锅':
            with col_args_3[0]:
                temp = st.number_input('设定温度（℃）', step=5.0)
            with col_args_3[1]:
                if st.button('设定温度', use_container_width=True):
                    st.session_state['实验模拟数据']['水浴锅']['温度'] = temp
            with col_args_3[2]:
                if st.button('放入仪器', use_container_width=True) and st.session_state['实验模拟数据'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据']['水浴锅'][st.session_state['实验模拟数据']['手中'][0]] = \
                        st.session_state['实验模拟数据']['水浴锅'].get(st.session_state['实验模拟数据']['手中'][0],
                                                                       0) + st.session_state['实验模拟数据']['手中'][
                            1]
                    st.session_state['实验模拟数据']['手中'] = None
            with col_args_3[3]:
                if st.button('初始化', use_container_width=True):
                    st.session_state['实验模拟数据']['水浴锅'] = {}
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据']['水浴锅'])


        elif st.session_state['实验模拟数据']['打开中'] == '抽滤瓶':
            with col_args_3[0]:
                if st.button('放入仪器', use_container_width=True) and st.session_state['实验模拟数据'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据']['抽滤瓶'][st.session_state['实验模拟数据']['手中'][0]] = \
                        st.session_state['实验模拟数据']['抽滤瓶'].get(st.session_state['实验模拟数据']['手中'][0],
                                                                       0) + st.session_state['实验模拟数据']['手中'][
                            1]
                    st.session_state['实验模拟数据']['手中'] = None
                if st.button('初始化', use_container_width=True):
                    st.session_state['实验模拟数据']['抽滤瓶'] = {}
            with col_args_3[1]:
                st.session_state['实验模拟数据']['抽滤'] = st.button('抽滤', use_container_width=True)
            with col_args_3[2]:
                if st.button('提滤液', use_container_width=True) and '滤液' in st.session_state['实验模拟数据']['抽滤瓶']:
                    st.session_state['实验模拟数据']['手中'] = [st.session_state['实验模拟数据']['抽滤瓶'].get('滤液')[0],st.session_state['实验模拟数据']['抽滤瓶'].get('滤液')[1]]
            with col_args_3[3]:
                if st.button('提滤渣', use_container_width=True) and '滤渣' in st.session_state['实验模拟数据']['抽滤瓶']:
                    st.session_state['实验模拟数据']['手中'] = [st.session_state['实验模拟数据']['抽滤瓶'].get('滤渣')[0],st.session_state['实验模拟数据']['抽滤瓶'].get('滤渣')[1]]
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据']['抽滤瓶'])


        elif st.session_state['实验模拟数据']['打开中'] == '控制时间':
            with col_args_3[0]:
                time = st.number_input('反应时间(min)', step=10.0)
            with col_args_3[3]:
                st.session_state['实验模拟数据']['反应'] = [st.button('确认反应', use_container_width=True), time]

        st.header('任务清单')
        with st.expander('浸提'):
            if st.session_state['实验模拟数据']['圆底烧瓶'] == {'蚕砂': 100.0, '水': 200.0} and \
                    st.session_state['实验模拟数据'].get('反应', [False, 0])[0] and \
                    st.session_state['实验模拟数据'].get('反应', [False, 0])[1] == 120.0 or \
                    st.session_state['实验模拟数据'].get('任务0', False):
                st.markdown(':green[取中药材蚕砂 100g 于 1000ml 圆底烧瓶中，加 200ml 水软化2h]')
                st.session_state['实验模拟数据']['任务0'] = True
            else:
                st.markdown(':red[取中药材蚕砂 100g 于 1000ml 圆底烧瓶中，加 200ml 水软化2h]')

            if st.session_state['实验模拟数据'].get('任务0', False) and \
                    st.session_state['实验模拟数据']['圆底烧瓶'] == {'蚕砂': 100.0, '水': 200.0, '丙酮': 300.0} and \
                    st.session_state['实验模拟数据']['水浴锅'] == {'圆底烧瓶': 1, '温度': 70.0} and \
                    st.session_state['实验模拟数据'].get('反应', [False, 0])[0] and \
                    st.session_state['实验模拟数据'].get('反应', [False, 0])[1] == 60.0:
                st.markdown(':green[加入 300ml 丙酮，在 70℃恒温水浴中回流浸提 60min]')
                st.session_state['实验模拟数据']['任务1'] = True
                st.session_state['实验模拟数据']['圆底烧瓶'] = {'滤液': 1, '滤渣': 1}
            elif st.session_state['实验模拟数据'].get('任务1', False):
                st.markdown(':green[加入 300ml 丙酮，在 70℃恒温水浴中回流浸提 60min]')
            else:
                st.markdown(':red[加入 300ml 丙酮，在 70℃恒温水浴中回流浸提 60min]')

            if st.session_state['实验模拟数据'].get('任务1', False) and \
                    st.session_state['实验模拟数据']['圆底烧瓶'] == {'滤液': 1, '滤渣': 1} and \
                    st.session_state['实验模拟数据']['抽滤瓶'] == {'圆底烧瓶': 1} and \
                    st.session_state['实验模拟数据'].get('抽滤', False):
                st.markdown(':green[抽滤]')
                st.session_state['实验模拟数据']['抽滤瓶']['滤液'] = ['浸提液A', 1]
                st.session_state['实验模拟数据']['抽滤瓶']['滤渣'] = ['滤渣', 1]
                st.session_state['实验模拟数据']['圆底烧瓶'] = {}
                st.session_state['实验模拟数据']['任务2'] = True
            elif st.session_state['实验模拟数据'].get('任务2', False):
                st.markdown(':green[抽滤]')
            else:
                st.markdown(':red[抽滤]')

        with c1:
            if st.session_state['实验模拟数据'].get('手中') is not None:
                st.markdown('手中有:red[' + str(st.session_state['实验模拟数据']['手中'][1]) + ']的:red[' +
                            st.session_state['实验模拟数据']['手中'][0] + ']')

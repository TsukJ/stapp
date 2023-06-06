import streamlit as st


class ExpSimulate:
    def __init__(self, exp_id):
        self.exp_id = exp_id
        self.exp_list = [self.exp1, self.exp2]

    def run(self):
        self.exp_list[self.exp_id]()

    def exp1(self):
        self.material = ['蚕砂', '水', '丙酮', '乙醚', '30%HCL', 'NaOH饱和溶液', 'DMF溶液', 'DPA溶液', '乙醇',
                         '脱镁叶绿酸溶液']
        self.instrument = ['圆底烧瓶', '水浴锅', '抽滤瓶', '旋转蒸发仪', '分液漏斗', '烧杯', '离心器', '干燥箱',
                           '天平', '容量瓶', '分光光度计', '紫外光谱仪', '荧光光谱仪', '控制时间']
        if st.session_state.get('样品') is None:
            st.session_state['样品'] = []
        if st.session_state.get('实验模拟数据1') is None:
            st.session_state['实验模拟数据1'] = {}
            st.session_state['实验模拟数据1']['按钮'] = {}
            st.session_state['实验模拟数据1']['打开中'] = '蚕砂'
        for i in self.instrument:
            if i not in st.session_state['实验模拟数据1']:
                st.session_state['实验模拟数据1'][i] = {}
        c1 = st.container()
        st.header('药品')
        col_args_1 = st.columns(4)
        for i in range(len(self.material)):
            row_num = i % 4
            with col_args_1[row_num]:
                st.session_state['实验模拟数据1']['按钮'][self.material[i]] = st.button(self.material[i],
                                                                                        use_container_width=True)
        st.header('仪器')
        col_args_2 = st.columns(4)
        for i in range(len(self.instrument)):
            row_num = i % 4
            with col_args_2[row_num]:
                st.session_state['实验模拟数据1']['按钮'][self.instrument[i]] = st.button(self.instrument[i],
                                                                                          use_container_width=True)
        st.header('操作')
        col_args_3 = st.columns(4)
        for i in st.session_state['实验模拟数据1']['按钮']:
            if st.session_state['实验模拟数据1']['按钮'][i]:
                st.session_state['实验模拟数据1']['打开中'] = i
        if st.session_state['实验模拟数据1']['打开中'] in self.material:
            with col_args_3[0]:
                amount = st.number_input('提取量', step=50.0)
            with col_args_3[3]:
                if st.button('确认提取', use_container_width=True):
                    st.session_state['实验模拟数据1']['手中'] = [st.session_state['实验模拟数据1']['打开中'], amount]


        elif st.session_state['实验模拟数据1']['打开中'] == '圆底烧瓶':
            if st.session_state['实验模拟数据1'].get('圆底烧瓶') is None:
                st.session_state['实验模拟数据1']['圆底烧瓶'] = {}
            with col_args_3[0]:
                if st.button('放入物质', use_container_width=True) and st.session_state['实验模拟数据1'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据1']['圆底烧瓶'][st.session_state['实验模拟数据1']['手中'][0]] = \
                        st.session_state['实验模拟数据1']['圆底烧瓶'].get(st.session_state['实验模拟数据1']['手中'][0],
                                                                          0) + \
                        st.session_state['实验模拟数据1']['手中'][
                            1]
                    st.session_state['实验模拟数据1']['手中'] = None
            with col_args_3[1]:
                if st.button('倒出物质', use_container_width=True):
                    st.session_state['实验模拟数据1']['圆底烧瓶'] = {}
            with col_args_3[2]:
                if st.button('拿起仪器', use_container_width=True):
                    st.session_state['实验模拟数据1']['手中'] = ['圆底烧瓶', 1]
            with col_args_3[3]:
                if st.button('倒入物质', use_container_width=True) and st.session_state['实验模拟数据1']['手中'] == [
                    '烧杯', 1]:
                    for i in st.session_state['实验模拟数据1']['烧杯']:
                        st.session_state['实验模拟数据1']['圆底烧瓶'][i] = \
                            st.session_state['实验模拟数据1']['圆底烧瓶'].get(i, 0) + \
                            st.session_state['实验模拟数据1']['烧杯'][i]
                    st.session_state['实验模拟数据1']['手中'] = None
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['圆底烧瓶'])


        elif st.session_state['实验模拟数据1']['打开中'] == '烧杯':
            if st.session_state['实验模拟数据1'].get('烧杯') is None:
                st.session_state['实验模拟数据1']['烧杯'] = {}
            with col_args_3[0]:
                if st.button('放入物质', use_container_width=True) and st.session_state['实验模拟数据1'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据1']['烧杯'][st.session_state['实验模拟数据1']['手中'][0]] = \
                        st.session_state['实验模拟数据1']['烧杯'].get(st.session_state['实验模拟数据1']['手中'][0],
                                                                      0) + st.session_state['实验模拟数据1']['手中'][
                            1]
                    st.session_state['实验模拟数据1']['手中'] = None
                if st.button('滴入物质', use_container_width=True) and st.session_state['实验模拟数据1'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据1']['烧杯']['滴加中'] = st.session_state['实验模拟数据1'].get(
                        '手中')[0]
            with col_args_3[1]:
                if st.button('倒出物质', use_container_width=True):
                    st.session_state['实验模拟数据1']['烧杯'] = {}
                if st.button('搅拌', use_container_width=True):
                    st.session_state['实验模拟数据1']['烧杯']['是否搅拌中'] = True
            with col_args_3[2]:
                if st.button('拿起仪器', use_container_width=True):
                    st.session_state['实验模拟数据1']['手中'] = ['烧杯', 1]
                if st.button('测pH', use_container_width=True) and \
                        st.session_state['实验模拟数据1']['烧杯'].get('是否搅拌中', False) and \
                        st.session_state['实验模拟数据1']['烧杯'].get('滴加中', None) == 'NaOH饱和溶液':
                    st.session_state['实验模拟数据1']['烧杯']['是否搅拌中'] = False
                    st.session_state['实验模拟数据1']['烧杯']['滴加中'] = None
                    st.session_state['实验模拟数据1']['烧杯']['PH'] = \
                        st.session_state['实验模拟数据1']['烧杯'].get('PH', 1) + 0.5
            with col_args_3[3]:
                if st.button('冰水浴', use_container_width=True):
                    st.session_state['实验模拟数据1']['烧杯']['是否冰水浴'] = True
                st.session_state['实验模拟数据1']['红光照射中'] = st.button('红光照射10min', use_container_width=True)
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['烧杯'])


        elif st.session_state['实验模拟数据1']['打开中'] == '水浴锅':
            with col_args_3[0]:
                temp = st.number_input('设定温度（℃）', step=5.0)
            with col_args_3[1]:
                if st.button('设定温度', use_container_width=True):
                    st.session_state['实验模拟数据1']['水浴锅']['温度'] = temp
            with col_args_3[2]:
                if st.button('放入仪器', use_container_width=True) and st.session_state['实验模拟数据1'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据1']['水浴锅'][st.session_state['实验模拟数据1']['手中'][0]] = \
                        st.session_state['实验模拟数据1']['水浴锅'].get(st.session_state['实验模拟数据1']['手中'][0],
                                                                        0) + st.session_state['实验模拟数据1']['手中'][
                            1]
                    st.session_state['实验模拟数据1']['手中'] = None
            with col_args_3[3]:
                if st.button('初始化', use_container_width=True):
                    st.session_state['实验模拟数据1']['水浴锅'] = {}
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['水浴锅'])


        elif st.session_state['实验模拟数据1']['打开中'] == '抽滤瓶':
            with col_args_3[0]:
                if st.button('放入仪器', use_container_width=True) and st.session_state['实验模拟数据1'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据1']['抽滤瓶'][st.session_state['实验模拟数据1']['手中'][0]] = \
                        st.session_state['实验模拟数据1']['抽滤瓶'].get(st.session_state['实验模拟数据1']['手中'][0],
                                                                        0) + st.session_state['实验模拟数据1']['手中'][
                            1]
                    st.session_state['实验模拟数据1']['手中'] = None
                if st.button('初始化', use_container_width=True):
                    st.session_state['实验模拟数据1']['抽滤瓶'] = {}
            with col_args_3[1]:
                st.session_state['实验模拟数据1']['抽滤'] = st.button('抽滤', use_container_width=True)
            with col_args_3[2]:
                if st.button('提滤液', use_container_width=True) and '滤液' in st.session_state['实验模拟数据1'][
                    '抽滤瓶']:
                    st.session_state['实验模拟数据1']['手中'] = [
                        st.session_state['实验模拟数据1']['抽滤瓶'].get('滤液')[0],
                        st.session_state['实验模拟数据1']['抽滤瓶'].get('滤液')[1]]
            with col_args_3[3]:
                if st.button('提滤渣', use_container_width=True) and '滤渣' in st.session_state['实验模拟数据1'][
                    '抽滤瓶']:
                    st.session_state['实验模拟数据1']['手中'] = [
                        st.session_state['实验模拟数据1']['抽滤瓶'].get('滤渣')[0],
                        st.session_state['实验模拟数据1']['抽滤瓶'].get('滤渣')[1]]
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['抽滤瓶'])


        elif st.session_state['实验模拟数据1']['打开中'] == '旋转蒸发仪':
            with col_args_3[0]:
                temp = st.number_input('设定温度（℃）', step=5.0, key='旋转蒸发仪温度')
            with col_args_3[1]:
                if st.button('设定温度', use_container_width=True):
                    st.session_state['实验模拟数据1']['旋转蒸发仪']['温度'] = temp
            with col_args_3[2]:
                if st.button('放入仪器', use_container_width=True) and st.session_state['实验模拟数据1'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据1']['旋转蒸发仪'][st.session_state['实验模拟数据1']['手中'][0]] = \
                        st.session_state['实验模拟数据1']['旋转蒸发仪'].get(
                            st.session_state['实验模拟数据1']['手中'][0],
                            0) + \
                        st.session_state['实验模拟数据1']['手中'][
                            1]
                    st.session_state['实验模拟数据1']['手中'] = None
            with col_args_3[3]:
                st.session_state['实验模拟数据1']['旋蒸浓缩'] = st.button('浓缩', use_container_width=True)
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['旋转蒸发仪'])


        elif st.session_state['实验模拟数据1']['打开中'] == '分液漏斗':
            with col_args_3[0]:
                if st.button('放入物质', use_container_width=True) and st.session_state['实验模拟数据1'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据1']['分液漏斗'][st.session_state['实验模拟数据1']['手中'][0]] = \
                        st.session_state['实验模拟数据1']['分液漏斗'].get(st.session_state['实验模拟数据1']['手中'][0],
                                                                          0) + \
                        st.session_state['实验模拟数据1']['手中'][
                            1]
                    st.session_state['实验模拟数据1']['手中'] = None
                if st.button('初始化', use_container_width=True):
                    st.session_state['实验模拟数据1']['分液漏斗'] = {}
            with col_args_3[1]:
                if st.button('倒入物质', use_container_width=True) and \
                        st.session_state['实验模拟数据1']['手中'] == ['圆底烧瓶', 1]:
                    for i in st.session_state['实验模拟数据1']['圆底烧瓶']:
                        st.session_state['实验模拟数据1']['分液漏斗'][i] = \
                            st.session_state['实验模拟数据1']['分液漏斗'].get(i, 0) + \
                            st.session_state['实验模拟数据1']['圆底烧瓶'][i]
                    st.session_state['实验模拟数据1']['手中'] = None
                if st.button('取上层', use_container_width=True) and '上层液' in st.session_state['实验模拟数据1'][
                    '分液漏斗']:
                    st.session_state['实验模拟数据1']['手中'] = [
                        '上层液', st.session_state['实验模拟数据1']['分液漏斗'].get('上层液')]
            with col_args_3[2]:
                if st.button('震荡', use_container_width=True):
                    st.session_state['实验模拟数据1']['分液漏斗']['震荡'] = True
                if st.button('取下层', use_container_width=True) and '下层液' in st.session_state['实验模拟数据1'][
                    '分液漏斗']:
                    st.session_state['实验模拟数据1']['手中'] = [
                        '下层液', st.session_state['实验模拟数据1']['分液漏斗'].get('下层液')]
            with col_args_3[3]:
                if st.button('静置', use_container_width=True) and st.session_state['实验模拟数据1']['分液漏斗'].get(
                        '震荡', False):
                    st.session_state['实验模拟数据1']['分液漏斗']['静置'] = True
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['分液漏斗'])


        elif st.session_state['实验模拟数据1']['打开中'] == '离心器':
            with col_args_3[0]:
                st.session_state['实验模拟数据1']['离心器']['设定转速'] = \
                    st.number_input('设定转速（rpm）', step=1000,
                                    value=st.session_state['实验模拟数据1']['离心器'].get('设定转速', 0))
            with col_args_3[1]:
                st.session_state['实验模拟数据1']['离心器']['设定时间'] = \
                    st.number_input('设定时间（min）', step=5,
                                    value=st.session_state['实验模拟数据1']['离心器'].get('设定时间', 0))
            with col_args_3[2]:
                if st.button('倒入物质', use_container_width=True) and \
                        st.session_state['实验模拟数据1']['手中'] == ['烧杯', 1]:
                    for i in st.session_state['实验模拟数据1']['烧杯']:
                        st.session_state['实验模拟数据1']['离心器'][i] = \
                            st.session_state['实验模拟数据1']['离心器'].get(i, 0) + \
                            st.session_state['实验模拟数据1']['烧杯'][i]
                    st.session_state['实验模拟数据1']['手中'] = None
                if st.button('初始化', use_container_width=True):
                    st.session_state['实验模拟数据1']['离心器'] = {}
            with col_args_3[3]:
                st.session_state['实验模拟数据1']['离心器启动状态'] = st.button('开始离心', use_container_width=True)
                if st.button('取液相', use_container_width=True) and '液相C' in st.session_state['实验模拟数据1'][
                    '离心器']:
                    st.session_state['实验模拟数据1']['手中'] = [
                        '液相C', st.session_state['实验模拟数据1']['离心器'].get('液相C')]
                if st.button('取固相', use_container_width=True) and '脱镁叶绿酸（固态）' in \
                        st.session_state['实验模拟数据1'][
                            '离心器']:
                    st.session_state['实验模拟数据1']['手中'] = [
                        '脱镁叶绿酸（固态）', st.session_state['实验模拟数据1']['离心器'].get('脱镁叶绿酸（固态）')]
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['离心器'])


        elif st.session_state['实验模拟数据1']['打开中'] == '干燥箱':
            with col_args_3[0]:
                st.session_state['实验模拟数据1']['干燥箱']['设定温度'] = \
                    st.number_input('设定温度（℃）', step=1000,
                                    value=st.session_state['实验模拟数据1']['干燥箱'].get('设定温度', 0))
            with col_args_3[1]:
                st.session_state['实验模拟数据1']['干燥箱']['设定时间'] = \
                    st.number_input('设定时间（min）', step=5,
                                    value=st.session_state['实验模拟数据1']['干燥箱'].get('设定时间', 0))
            with col_args_3[2]:
                if st.button('放入物质', use_container_width=True) and st.session_state['实验模拟数据1'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据1']['干燥箱'][st.session_state['实验模拟数据1']['手中'][0]] = \
                        st.session_state['实验模拟数据1']['干燥箱'].get(st.session_state['实验模拟数据1']['手中'][0],
                                                                        0) + st.session_state['实验模拟数据1']['手中'][
                            1]
                    st.session_state['实验模拟数据1']['手中'] = None
                if st.button('初始化', use_container_width=True):
                    st.session_state['实验模拟数据1']['干燥箱'] = {}
            with col_args_3[3]:
                st.session_state['实验模拟数据1']['干燥箱启动状态'] = st.button('开始干燥', use_container_width=True)
                if st.button('拿出产物', use_container_width=True):
                    for i in st.session_state['实验模拟数据1']['干燥箱'].keys():
                        if i != ('设定温度' or '设定时间') and i is not None:
                            st.session_state['实验模拟数据1']['手中'] = [i,
                                                                         st.session_state['实验模拟数据1']['干燥箱'][i]]
                            break
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['干燥箱'])


        elif st.session_state['实验模拟数据1']['打开中'] == '天平':
            with col_args_3[0]:
                amount = st.number_input('称取量（mg）', step=10.0)
            with col_args_3[1]:
                if st.button('放入物质', use_container_width=True) and st.session_state['实验模拟数据1'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据1']['天平'][st.session_state['实验模拟数据1']['手中'][0]] = \
                        st.session_state['实验模拟数据1']['天平'].get(st.session_state['实验模拟数据1']['手中'][0],
                                                                      0) + st.session_state['实验模拟数据1']['手中'][
                            1]
                    st.session_state['实验模拟数据1']['手中'] = None
            with col_args_3[2]:
                st.session_state['实验模拟数据1']['天平称重状态'] = st.button('开始称重', use_container_width=True)
            with col_args_3[3]:
                if st.button('确认提取', use_container_width=True) and \
                        '脱镁叶绿酸（干燥后）' in st.session_state['实验模拟数据1']['天平']:
                    st.session_state['实验模拟数据1']['手中'] = ['脱镁叶绿酸（干燥后）', amount]
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['天平'])


        elif st.session_state['实验模拟数据1']['打开中'] == '分光光度计':
            with col_args_3[0]:
                st.session_state['实验模拟数据1']['分光光度计']['测量波长'] = \
                    st.number_input('测量波长（nm）', step=10.0,
                                    value=st.session_state['实验模拟数据1']['分光光度计'].get('测量波长', 0.0))
            with col_args_3[1]:
                if st.button('倒入物质', use_container_width=True) and \
                        st.session_state['实验模拟数据1']['手中'] == ['烧杯', 1]:
                    for i in st.session_state['实验模拟数据1']['烧杯']:
                        st.session_state['实验模拟数据1']['分光光度计'][i] = \
                            st.session_state['实验模拟数据1']['分光光度计'].get(i, 0) + \
                            st.session_state['实验模拟数据1']['烧杯'][i]
                    st.session_state['实验模拟数据1']['手中'] = None
                if st.button('放入物质', use_container_width=True) and st.session_state['实验模拟数据1'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据1']['分光光度计'][st.session_state['实验模拟数据1']['手中'][0]] = \
                        st.session_state['实验模拟数据1']['分光光度计'].get(
                            st.session_state['实验模拟数据1']['手中'][0],
                            0) + \
                        st.session_state['实验模拟数据1']['手中'][
                            1]
                    st.session_state['实验模拟数据1']['手中'] = None
            with col_args_3[2]:
                st.session_state['实验模拟数据1']['吸光度测量状态'] = st.button('开始测量', use_container_width=True)
            with col_args_3[3]:
                if st.button('倒出物质', use_container_width=True):
                    def remake():
                        d = []
                        for item in st.session_state['实验模拟数据1']['分光光度计']:
                            if item != '测量波长':
                                d.append(item)
                        for j in d:
                            del st.session_state['实验模拟数据1']['分光光度计'][j]

                    remake()
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['分光光度计'])


        elif st.session_state['实验模拟数据1']['打开中'] == '紫外光谱仪':
            with col_args_3[0]:
                st.session_state['实验模拟数据1']['紫外光谱仪']['测量波长起点'] = \
                    st.number_input('测量波长起点（nm）', step=10.0,
                                    value=st.session_state['实验模拟数据1']['紫外光谱仪'].get('测量波长起点', 0.0))
            with col_args_3[1]:
                st.session_state['实验模拟数据1']['紫外光谱仪']['测量波长终点'] = \
                    st.number_input('测量波长终点（nm）', step=10.0,
                                    value=st.session_state['实验模拟数据1']['紫外光谱仪'].get('测量波长终点', 0.0))
            with col_args_3[2]:
                if st.button('倒入物质', use_container_width=True) and \
                        st.session_state['实验模拟数据1']['手中'] == ['烧杯', 1]:
                    for i in st.session_state['实验模拟数据1']['烧杯']:
                        st.session_state['实验模拟数据1']['紫外光谱仪'][i] = \
                            st.session_state['实验模拟数据1']['紫外光谱仪'].get(i, 0) + \
                            st.session_state['实验模拟数据1']['烧杯'][i]
                    st.session_state['实验模拟数据1']['手中'] = None
                if st.button('放入物质', use_container_width=True) and st.session_state['实验模拟数据1'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据1']['紫外光谱仪'][st.session_state['实验模拟数据1']['手中'][0]] = \
                        st.session_state['实验模拟数据1']['紫外光谱仪'].get(
                            st.session_state['实验模拟数据1']['手中'][0],
                            0) + \
                        st.session_state['实验模拟数据1']['手中'][
                            1]
                    st.session_state['实验模拟数据1']['手中'] = None
            with col_args_3[3]:
                st.session_state['实验模拟数据1']['紫外光测量状态'] = st.button('开始测量', use_container_width=True)
                if st.button('倒出物质', use_container_width=True):
                    def remake():
                        d = []
                        for item in st.session_state['实验模拟数据1']['紫外光谱仪']:
                            if item != ('测量波长起点' or '测量波长终点'):
                                d.append(item)
                        for j in d:
                            del st.session_state['实验模拟数据1']['紫外光谱仪'][j]

                    remake()
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['紫外光谱仪'])


        elif st.session_state['实验模拟数据1']['打开中'] == '荧光光谱仪':
            with col_args_3[0]:
                st.session_state['实验模拟数据1']['荧光光谱仪']['测量波长起点'] = \
                    st.number_input('测量波长起点（nm）', step=10.0,
                                    value=st.session_state['实验模拟数据1']['荧光光谱仪'].get('测量波长起点', 0.0))
            with col_args_3[1]:
                st.session_state['实验模拟数据1']['荧光光谱仪']['测量波长终点'] = \
                    st.number_input('测量波长终点（nm）', step=10.0,
                                    value=st.session_state['实验模拟数据1']['荧光光谱仪'].get('测量波长终点', 0.0))
            with col_args_3[2]:
                if st.button('倒入物质', use_container_width=True) and \
                        st.session_state['实验模拟数据1']['手中'] == ['烧杯', 1]:
                    for i in st.session_state['实验模拟数据1']['烧杯']:
                        st.session_state['实验模拟数据1']['荧光光谱仪'][i] = \
                            st.session_state['实验模拟数据1']['荧光光谱仪'].get(i, 0) + \
                            st.session_state['实验模拟数据1']['烧杯'][i]
                    st.session_state['实验模拟数据1']['手中'] = None
                if st.button('放入物质', use_container_width=True) and st.session_state['实验模拟数据1'].get(
                        '手中') is not None:
                    st.session_state['实验模拟数据1']['荧光光谱仪'][st.session_state['实验模拟数据1']['手中'][0]] = \
                        st.session_state['实验模拟数据1']['荧光光谱仪'].get(
                            st.session_state['实验模拟数据1']['手中'][0],
                            0) + \
                        st.session_state['实验模拟数据1']['手中'][
                            1]
                    st.session_state['实验模拟数据1']['手中'] = None
            with col_args_3[3]:
                st.session_state['实验模拟数据1']['荧光测量状态'] = st.button('开始测量', use_container_width=True)
                if st.button('倒出物质', use_container_width=True):
                    def remake():
                        d = []
                        for item in st.session_state['实验模拟数据1']['荧光光谱仪']:
                            if item != ('测量波长起点' or '测量波长终点'):
                                d.append(item)
                        for j in d:
                            del st.session_state['实验模拟数据1']['荧光光谱仪'][j]

                    remake()
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['荧光光谱仪'])


        elif st.session_state['实验模拟数据1']['打开中'] == '容量瓶':
            def rongliangping():
                if '预输入' not in st.session_state['实验模拟数据1']['容量瓶']:
                    st.session_state['实验模拟数据1']['容量瓶']['预输入'] = {}
                if '容量瓶组' not in st.session_state['实验模拟数据1']['容量瓶']:
                    st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'] = {}
                tabs_args = [st.container(), st.container(), st.container(), st.container(), st.container(),
                             st.container()]
                index = 1
                for tabs in tabs_args:
                    name = '容量瓶' + str(index)
                    if name not in st.session_state['实验模拟数据1']['容量瓶']['容量瓶组']:
                        st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'][name] = {}
                    cols_args = st.columns(4)
                    st.write("------------------------------------------------------")
                    with tabs:
                        with cols_args[0]:
                            st.session_state['实验模拟数据1']['容量瓶']['预输入'][name] = \
                                st.number_input(name + ':预设浓度（x10^-5mol/L）', step=10.0,
                                                value=st.session_state['实验模拟数据1']['容量瓶']['预输入'].get(name,
                                                                                                                0.0))
                        with cols_args[1]:
                            if st.button('加入目标物质', use_container_width=True, key=name + '目标物质') and \
                                    st.session_state['实验模拟数据1']['手中'] is not None:
                                st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'][name]['目标物'] = \
                                    st.session_state['实验模拟数据1']['手中'][0]
                        with cols_args[2]:
                            if st.button('定容（使用手中物质）', use_container_width=True, key=name + '定容物质') and \
                                    st.session_state['实验模拟数据1']['手中'] is not None:
                                st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'][name]['定容物'] = \
                                    st.session_state['实验模拟数据1']['手中'][0]
                                if st.session_state['实验模拟数据1']['容量瓶']['预输入'].get(name, 0.0) != 0 and \
                                        st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'][name].get(
                                            '目标物', None) is not None and \
                                        st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'][name].get(
                                            '定容', False) is False:
                                    st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'][name]['定容'] = True
                                    st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'][name]['浓度'] = \
                                        st.session_state['实验模拟数据1']['容量瓶']['预输入'][name]
                        with cols_args[3]:
                            if st.button('提取', use_container_width=True, key=name + '提取') and \
                                    st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'][name].get('定容', False):
                                num = format(st.session_state['实验模拟数据1']['容量瓶']['预输入'][name], '.2f')
                                num_string = '（' + num + 'x10^-5mol/L）'
                                full_name = st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'][name][
                                                '目标物'] + '/' + \
                                            st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'][name]['定容物']
                                st.session_state['实验模拟数据1']['手中'] = [full_name + num_string, 1]
                            if st.button('倒掉', use_container_width=True, key=name + '倒出'):
                                st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'][name] = {}
                    index += 1

            rongliangping()
            st.header('仪器状态')
            st.write(st.session_state['实验模拟数据1']['容量瓶']['容量瓶组'])


        elif st.session_state['实验模拟数据1']['打开中'] == '控制时间':
            with col_args_3[0]:
                time = st.number_input('反应时间(min)', step=10.0)
            with col_args_3[3]:
                st.session_state['实验模拟数据1']['反应'] = [st.button('确认反应', use_container_width=True), time]

        col_args_4 = st.columns([8, 2])
        task_num = 19

        def get_accomplish_num(num):
            for i in range(num):
                if st.session_state['实验模拟数据1'].get('任务' + str(i), False) is False:
                    return i
            return num

        accomplish_rate = "{:.2%}".format(get_accomplish_num(task_num) / task_num)
        with col_args_4[0]:
            st.header('任务清单')
        with col_args_4[1]:
            st.write('--')
            st.write(':green[完成度：{0}]'.format(accomplish_rate))
        with st.expander('浸提'):
            if st.session_state['实验模拟数据1'].get('反应', [False, 0])[0] and \
                    st.session_state['实验模拟数据1'].get('反应', [False, 0])[1] == 120.0 and \
                    st.session_state['实验模拟数据1']['圆底烧瓶'] == {'蚕砂': 100.0, '水': 200.0}:
                st.markdown(':green[取中药材蚕砂 100g 于 1000ml 圆底烧瓶中，加 200ml 水软化2h]')
                st.session_state['实验模拟数据1']['任务0'] = True
            elif st.session_state['实验模拟数据1'].get('任务0', False):
                st.markdown(':green[取中药材蚕砂 100g 于 1000ml 圆底烧瓶中，加 200ml 水软化2h]')
            else:
                st.markdown(':red[取中药材蚕砂 100g 于 1000ml 圆底烧瓶中，加 200ml 水软化2h]')

            if st.session_state['实验模拟数据1'].get('任务0', False) and \
                    st.session_state['实验模拟数据1']['圆底烧瓶'] == {'蚕砂': 100.0, '水': 200.0, '丙酮': 300.0} and \
                    st.session_state['实验模拟数据1']['水浴锅'] == {'圆底烧瓶': 1, '温度': 70.0} and \
                    st.session_state['实验模拟数据1'].get('反应', [False, 0])[0] and \
                    st.session_state['实验模拟数据1'].get('反应', [False, 0])[1] == 60.0:
                st.markdown(':green[加入 300ml 丙酮，在 70℃恒温水浴中回流浸提 60min]')
                st.session_state['实验模拟数据1']['任务1'] = True
                st.session_state['实验模拟数据1']['圆底烧瓶'] = {'液相A': 1, '固相A': 1}
            elif st.session_state['实验模拟数据1'].get('任务1', False):
                st.markdown(':green[加入 300ml 丙酮，在 70℃恒温水浴中回流浸提 60min]')
            else:
                st.markdown(':red[加入 300ml 丙酮，在 70℃恒温水浴中回流浸提 60min]')

            if st.session_state['实验模拟数据1'].get('任务1', False) and \
                    st.session_state['实验模拟数据1']['圆底烧瓶'] == {'液相A': 1, '固相A': 1} and \
                    st.session_state['实验模拟数据1']['抽滤瓶'] == {'圆底烧瓶': 1} and \
                    st.session_state['实验模拟数据1'].get('抽滤', False):
                st.markdown(':green[抽滤]')
                st.session_state['实验模拟数据1']['抽滤瓶']['滤液'] = ['浸提液A', 1]
                st.session_state['实验模拟数据1']['抽滤瓶']['滤渣'] = ['滤渣', 1]
                st.session_state['实验模拟数据1']['圆底烧瓶'] = {}
                st.session_state['实验模拟数据1']['任务2'] = True
            elif st.session_state['实验模拟数据1'].get('任务2', False):
                st.markdown(':green[抽滤]')
            else:
                st.markdown(':red[抽滤]')

            if st.session_state['实验模拟数据1'].get('任务2', False) and \
                    st.session_state['实验模拟数据1']['圆底烧瓶'] == {'滤渣': 1, '水': 100.0, '丙酮': 200.0} and \
                    st.session_state['实验模拟数据1']['水浴锅'] == {'圆底烧瓶': 1, '温度': 70.0} and \
                    st.session_state['实验模拟数据1'].get('反应', [False, 0])[0] and \
                    st.session_state['实验模拟数据1'].get('反应', [False, 0])[1] == 60.0:
                st.markdown(
                    ':green[收集滤液，滤渣倒回圆底烧瓶中，再加入 100ml 蒸馏水，200ml 丙酮，在 70℃恒温水浴中回流浸提 60min]')
                st.session_state['实验模拟数据1']['圆底烧瓶'] = {'液相B': 1, '固相B': 1}
                st.session_state['实验模拟数据1']['任务3'] = True
            elif st.session_state['实验模拟数据1'].get('任务3', False):
                st.markdown(
                    ':green[收集滤液，滤渣倒回圆底烧瓶中，再加入 100ml 蒸馏水，200ml 丙酮，在 70℃恒温水浴中回流浸提 60min]')
            else:
                st.markdown(
                    ':red[收集滤液，滤渣倒回圆底烧瓶中，再加入 100ml 蒸馏水，200ml 丙酮，在 70℃恒温水浴中回流浸提 60min]')

            if st.session_state['实验模拟数据1'].get('任务3', False) and \
                    st.session_state['实验模拟数据1']['圆底烧瓶'] == {'液相B': 1, '固相B': 1} and \
                    st.session_state['实验模拟数据1']['抽滤瓶'] == {'圆底烧瓶': 1} and \
                    st.session_state['实验模拟数据1'].get('抽滤', False):
                st.markdown(':green[抽滤]')
                st.session_state['实验模拟数据1']['抽滤瓶']['滤液'] = ['浸提液B', 1]
                st.session_state['实验模拟数据1']['抽滤瓶']['滤渣'] = ['滤渣', 1]
                st.session_state['实验模拟数据1']['圆底烧瓶'] = {}
                st.session_state['实验模拟数据1']['任务4'] = True
            elif st.session_state['实验模拟数据1'].get('任务4', False):
                st.markdown(':green[抽滤]')
            else:
                st.markdown(':red[抽滤]')

            if st.session_state['实验模拟数据1'].get('任务4', False) and \
                    st.session_state['实验模拟数据1']['圆底烧瓶'] == {'浸提液A': 1, '浸提液B': 1}:
                st.markdown(':green[合并浸提液]')
                st.session_state['实验模拟数据1']['圆底烧瓶'] = {'浸提液（合并）': 1}
                st.session_state['实验模拟数据1']['任务5'] = True
            elif st.session_state['实验模拟数据1'].get('任务5', False):
                st.markdown(':green[合并浸提液]')
            else:
                st.markdown(':red[合并浸提液]')

        with st.expander('萃取'):
            if st.session_state['实验模拟数据1'].get('任务5', False) and \
                    st.session_state['实验模拟数据1']['圆底烧瓶'] == {'浸提液（合并）': 1} and \
                    st.session_state['实验模拟数据1']['旋转蒸发仪'] == {'圆底烧瓶': 1, '温度': 50} and \
                    st.session_state['实验模拟数据1'].get('旋蒸浓缩', False):
                st.markdown(':green[用旋转蒸发仪在 50℃下将浸提液浓缩至 50ml]')
                st.session_state['实验模拟数据1']['圆底烧瓶'] = {'浓缩液': 50.0}
                st.session_state['实验模拟数据1']['任务6'] = True
            elif st.session_state['实验模拟数据1'].get('任务6', False):
                st.markdown(':green[用旋转蒸发仪在 50℃下将浸提液浓缩至 50ml]')
            else:
                st.markdown(':red[用旋转蒸发仪在 50℃下将浸提液浓缩至 50ml]')

            if st.session_state['实验模拟数据1'].get('任务6', False) and \
                    st.session_state['实验模拟数据1']['分液漏斗'] == {'浓缩液': 50.0, '乙醚': 150.0, '30%HCL': 100.0,
                                                                      '震荡': True, '静置': True}:
                st.markdown(
                    ':green[移至 500ml 分液漏斗 中，依次加入 150 ml 乙醚、30%HCl 100ml，振荡 5min，进行转溶萃取，静置至完全分层]')
                st.session_state['实验模拟数据1']['分液漏斗'] = {'上层液': 1, '下层液': 1}
                st.session_state['实验模拟数据1']['任务7'] = True
            elif st.session_state['实验模拟数据1'].get('任务7', False):
                st.markdown(
                    ':green[移至 500ml 分液漏斗 中，依次加入 150 ml 乙醚、30%HCl 100ml，振荡 5min，进行转溶萃取，静置至完全分层]')
            else:
                st.markdown(
                    ':red[移至 500ml 分液漏斗 中，依次加入 150 ml 乙醚、30%HCl 100ml，振荡 5min，进行转溶萃取，静置至完全分层]')

            if st.session_state['实验模拟数据1'].get('任务7', False) and \
                    st.session_state['实验模拟数据1']['烧杯'].get('下层液', 0) == 1 and \
                    st.session_state['实验模拟数据1']['烧杯'].get('是否冰水浴', False) and \
                    st.session_state['实验模拟数据1']['烧杯'].get('PH', None) == (2.5 or 3.0):
                st.markdown(
                    ':green[将下层水溶液放出置于烧杯，放入冰水浴中，慢慢滴入 NaOH 的饱和溶液，同时进行搅拌，直至pH值在 2.5-3之间]')
                st.session_state['实验模拟数据1']['烧杯'] = {'样品（液体）': 1}
                st.session_state['实验模拟数据1']['任务8'] = True
            elif st.session_state['实验模拟数据1'].get('任务8', False):
                st.markdown(
                    ':green[将下层水溶液放出置于烧杯，放入冰水浴中，慢慢滴入 NaOH 的饱和溶液，同时进行搅拌，直至pH值在 2.5-3之间]')
            else:
                st.markdown(
                    ':red[将下层水溶液放出置于烧杯，放入冰水浴中，慢慢滴入 NaOH 的饱和溶液，同时进行搅拌，直至pH值在 2.5-3之间]')

            if st.session_state['实验模拟数据1'].get('任务8', False) and \
                    st.session_state['实验模拟数据1']['离心器'] == {'设定转速': 3000.0, '设定时间': 10.0,
                                                                    '样品（液体）': 1}:
                st.markdown(
                    ':green[3000rpm 离心 10min，所得沉淀即为脱镁叶绿酸]')
                st.session_state['实验模拟数据1']['离心器'] = {'液相C': 1, '脱镁叶绿酸（固态）': 1}
                st.session_state['实验模拟数据1']['任务9'] = True
            elif st.session_state['实验模拟数据1'].get('任务9', False):
                st.markdown(
                    ':green[3000rpm 离心 10min，所得沉淀即为脱镁叶绿酸]')
            else:
                st.markdown(
                    ':red[3000rpm 离心 10min，所得沉淀即为脱镁叶绿酸]')

        with st.expander('干燥及含量测定'):
            if st.session_state['实验模拟数据1'].get('任务9', False) and \
                    st.session_state['实验模拟数据1']['干燥箱'] == {'设定温度': 60.0, '设定时间': 120.0,
                                                                    '脱镁叶绿酸（固态）': 1} and \
                    st.session_state['实验模拟数据1'].get('干燥箱启动状态', False):
                st.markdown(
                    ':green[将沉淀在 60℃下真空干燥箱中烘干 2h]')
                st.session_state['实验模拟数据1']['干燥箱'] = {'脱镁叶绿酸（干燥后）': 1}
                st.session_state['实验模拟数据1']['任务10'] = True
            elif st.session_state['实验模拟数据1'].get('任务10', False):
                st.markdown(
                    ':green[将沉淀在 60℃下真空干燥箱中烘干 2h]')
            else:
                st.markdown(
                    ':red[将沉淀在 60℃下真空干燥箱中烘干 2h]')

            if st.session_state['实验模拟数据1'].get('任务10', False) and \
                    st.session_state['实验模拟数据1']['天平'] == {'脱镁叶绿酸（干燥后）': 1} and \
                    st.session_state['实验模拟数据1'].get('天平称重状态', False):
                st.markdown(
                    ':green[称重]')
                st.session_state['实验模拟数据1']['任务11'] = True
            elif st.session_state['实验模拟数据1'].get('任务11', False):
                st.markdown(
                    ':green[称重]')
            else:
                st.markdown(
                    ':red[称重]')

            if st.session_state['实验模拟数据1'].get('任务11', False) and \
                    st.session_state['实验模拟数据1']['烧杯'] == {'脱镁叶绿酸（干燥后）': 10.0, 'DMF溶液': 100}:
                st.session_state['实验模拟数据1']['烧杯'] = {'样品（溶于DMF中）': 1}
                st.markdown(
                    ':green[准确称取 10mg 样品，溶于 100 ml DMF 溶液中]')
                st.session_state['实验模拟数据1']['任务12'] = True
            elif st.session_state['实验模拟数据1'].get('任务12', False):
                st.markdown(
                    ':green[准确称取 10mg 样品，溶于 100 ml DMF 溶液中]')
            else:
                st.markdown(
                    ':red[准确称取 10mg 样品，溶于 100 ml DMF 溶液中]')

            if st.session_state['实验模拟数据1'].get('任务12', False) and \
                    st.session_state['实验模拟数据1']['分光光度计'] == {'样品（溶于DMF中）': 1, '测量波长': 667.0} and \
                    st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                st.markdown(
                    ':green[波长 667nm测定吸光值]')
                st.session_state['实验模拟数据1']['任务13'] = True
            elif st.session_state['实验模拟数据1'].get('任务13', False):
                st.markdown(
                    ':green[波长 667nm测定吸光值]')
            else:
                st.markdown(
                    ':red[波长 667nm测定吸光值]')

            if st.session_state['实验模拟数据1'].get('任务13', False) and \
                    st.session_state['实验模拟数据1']['紫外光谱仪'] == {'样品（溶于DMF中）': 1, '测量波长起点': 300,
                                                                        '测量波长终点': 800} and \
                    st.session_state['实验模拟数据1'].get('紫外光测量状态', False):
                st.markdown(
                    ':green[取 10mg 脱镁叶绿酸 a 提取物粉末溶于 100mlDMF 溶液中，在 300nm—800nm 波长范围内进行紫外光扫描]')
                st.session_state['实验模拟数据1']['任务14'] = True
            elif st.session_state['实验模拟数据1'].get('任务14', False):
                st.markdown(
                    ':green[取 10mg 脱镁叶绿酸 a 提取物粉末溶于 100mlDMF 溶液中，在 300nm—800nm 波长范围内进行紫外光扫描]')
            else:
                st.markdown(
                    ':red[取 10mg 脱镁叶绿酸 a 提取物粉末溶于 100mlDMF 溶液中，在 300nm—800nm 波长范围内进行紫外光扫描]')

            if st.session_state['实验模拟数据1'].get('任务14', False) and \
                    st.session_state['实验模拟数据1']['荧光光谱仪'] == {'样品（溶于DMF中）': 1, '测量波长起点': 300,
                                                                        '测量波长终点': 800} and \
                    st.session_state['实验模拟数据1'].get('荧光测量状态', False):
                st.markdown(
                    ':green[取 10mg 脱镁叶绿酸 a 提取物粉末溶于 100mlDMF 溶液中，在 300nm—800nm 波长范围内进行荧光扫描]')
                st.session_state['实验模拟数据1']['任务15'] = True
            elif st.session_state['实验模拟数据1'].get('任务15', False):
                st.markdown(
                    ':green[取 10mg 脱镁叶绿酸 a 提取物粉末溶于 100mlDMF 溶液中，在 300nm—800nm 波长范围内进行荧光扫描]')
            else:
                st.markdown(
                    ':red[取 10mg 脱镁叶绿酸 a 提取物粉末溶于 100mlDMF 溶液中，在 300nm—800nm 波长范围内进行荧光扫描]')

        with st.expander('单线态氧的含量测定'):
            if st.session_state['实验模拟数据1'].get('任务15', False) and \
                    st.session_state['实验模拟数据1']['容量瓶']['容量瓶组']['容量瓶1'] == \
                    {"目标物": "DPA溶液", "定容物": "乙醇", "定容": True, "浓度": 1.25} and \
                    st.session_state['实验模拟数据1']['容量瓶']['容量瓶组']['容量瓶2'] == \
                    {"目标物": "DPA溶液", "定容物": "乙醇", "定容": True, "浓度": 2.5} and \
                    st.session_state['实验模拟数据1']['容量瓶']['容量瓶组']['容量瓶3'] == \
                    {"目标物": "DPA溶液", "定容物": "乙醇", "定容": True, "浓度": 5} and \
                    st.session_state['实验模拟数据1']['容量瓶']['容量瓶组']['容量瓶4'] == \
                    {"目标物": "DPA溶液", "定容物": "乙醇", "定容": True, "浓度": 10} and \
                    st.session_state['实验模拟数据1']['容量瓶']['容量瓶组']['容量瓶5'] == \
                    {"目标物": "DPA溶液", "定容物": "乙醇", "定容": True, "浓度": 20} and \
                    st.session_state['实验模拟数据1']['容量瓶']['容量瓶组']['容量瓶6'] == \
                    {"目标物": "DPA溶液", "定容物": "乙醇", "定容": True, "浓度": 40}:
                st.markdown(
                    ':green[配制一系列浓度（1.25×10-5、2.5×10-5、5×10-5、1×10-4、 2×10-4、4×10-4mol/L）的 9，10-二苯蒽（DPA）的乙醇溶液]')
                st.session_state['实验模拟数据1']['任务16'] = True
            elif st.session_state['实验模拟数据1'].get('任务16', False):
                st.markdown(
                    ':green[配制一系列浓度（1.25×10-5、2.5×10-5、5×10-5、1×10-4、 2×10-4、4×10-4mol/L）的 9，10-二苯蒽（DPA）的乙醇溶液]')
            else:
                st.markdown(
                    ':red[配制一系列浓度（1.25×10-5、2.5×10-5、5×10-5、1×10-4、 2×10-4、4×10-4mol/L）的 '
                    '9，10-二苯蒽（DPA）的乙醇溶液（请按浓度从小到大的顺序配置，不然可能会出错）]')

            if st.session_state['实验模拟数据1'].get('任务16', False):
                if '任务17组' not in st.session_state['实验模拟数据1']:
                    st.session_state['实验模拟数据1']['任务17组'] = {}
                if st.session_state['实验模拟数据1']['分光光度计'] == \
                        {'DPA溶液/乙醇（1.25x10^-5mol/L）': 1, '测量波长': 355.0} and \
                        st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                    st.session_state['实验模拟数据1']['任务17组']['1'] = True
                elif st.session_state['实验模拟数据1']['分光光度计'] == \
                        {'DPA溶液/乙醇（2.50x10^-5mol/L）': 1, '测量波长': 355.0} and \
                        st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                    st.session_state['实验模拟数据1']['任务17组']['2'] = True
                elif st.session_state['实验模拟数据1']['分光光度计'] == \
                        {'DPA溶液/乙醇（5.00x10^-5mol/L）': 1, '测量波长': 355.0} and \
                        st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                    st.session_state['实验模拟数据1']['任务17组']['3'] = True
                elif st.session_state['实验模拟数据1']['分光光度计'] == \
                        {'DPA溶液/乙醇（10.00x10^-5mol/L）': 1, '测量波长': 355.0} and \
                        st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                    st.session_state['实验模拟数据1']['任务17组']['4'] = True
                elif st.session_state['实验模拟数据1']['分光光度计'] == \
                        {'DPA溶液/乙醇（20.00x10^-5mol/L）': 1, '测量波长': 355.0} and \
                        st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                    st.session_state['实验模拟数据1']['任务17组']['5'] = True
                elif st.session_state['实验模拟数据1']['分光光度计'] == \
                        {'DPA溶液/乙醇（40.00x10^-5mol/L）': 1, '测量波长': 355.0} and \
                        st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                    st.session_state['实验模拟数据1']['任务17组']['6'] = True
                if len(st.session_state['实验模拟数据1']['任务17组'].keys()) == 6:
                    st.markdown(
                        ':green[将上述溶液于 355 nm 处测定吸光度值]')
                    st.session_state['实验模拟数据1']['任务17'] = True
                elif st.session_state['实验模拟数据1'].get('任务17', False):
                    st.markdown(
                        ':green[将上述溶液于 355 nm 处测定吸光度值]')
                else:
                    def markdown_17():
                        text = ''
                        lyst = ['1.25', '2.5', '5', '10', '20', '40']
                        for i in st.session_state['实验模拟数据1']['任务17组']:
                            text += str(lyst[eval(i) - 1]) + '丨'
                        st.markdown(
                            ':red[将上述溶液于 355 nm 处测定吸光度值]（已完成：:green[{0}]）'.format(text))

                    markdown_17()
            else:
                st.markdown(
                    ':red[将上述溶液于 355 nm 处测定吸光度值]')

            if st.session_state['实验模拟数据1'].get('任务17', False) and \
                    st.session_state['实验模拟数据1']['烧杯'] == {"脱镁叶绿酸溶液": 5, "DPA溶液": 5}:
                st.session_state['实验模拟数据1']['烧杯'] = {"脱镁叶绿酸溶液（DPA）": 10}
                st.markdown(
                    ':green[量取 5 mL 2×10-5 DPA 溶液，加入 5 mL 2×10-4 mol/L 的脱镁叶绿酸溶液混合均匀]')
                st.session_state['实验模拟数据1']['任务18'] = True
            elif st.session_state['实验模拟数据1'].get('任务18', False):
                st.markdown(
                    ':green[量取 5 mL 2×10-5 DPA 溶液，加入 5 mL 2×10-4 mol/L 的脱镁叶绿酸溶液混合均匀]')
            else:
                st.markdown(
                    ':red[量取 5 mL 2×10-5 DPA 溶液，加入 5 mL 2×10-4 mol/L 的脱镁叶绿酸溶液混合均匀]')

            if st.session_state['实验模拟数据1'].get('任务18', False):
                if st.session_state['实验模拟数据1']['烧杯'] == {"脱镁叶绿酸溶液（DPA）": 10} and \
                        st.session_state['实验模拟数据1'].get('红光照射中', False):
                    st.session_state['实验模拟数据1']['烧杯'] = {"脱镁叶绿酸溶液（DPA）（已照射10min）": 10}
                elif st.session_state['实验模拟数据1']['烧杯'] == {"脱镁叶绿酸溶液（DPA）（已照射10min）": 10} and \
                        st.session_state['实验模拟数据1'].get('红光照射中', False):
                    st.session_state['实验模拟数据1']['烧杯'] = {"脱镁叶绿酸溶液（DPA）（已照射20min）": 10}
                elif st.session_state['实验模拟数据1']['烧杯'] == {"脱镁叶绿酸溶液（DPA）（已照射20min）": 10} and \
                        st.session_state['实验模拟数据1'].get('红光照射中', False):
                    st.session_state['实验模拟数据1']['烧杯'] = {"脱镁叶绿酸溶液（DPA）（已照射30min）": 10}
                elif st.session_state['实验模拟数据1']['烧杯'] == {"脱镁叶绿酸溶液（DPA）（已照射30min）": 10} and \
                        st.session_state['实验模拟数据1'].get('红光照射中', False):
                    st.session_state['实验模拟数据1']['烧杯'] = {"脱镁叶绿酸溶液（DPA）（已照射40min）": 10}
                elif st.session_state['实验模拟数据1']['烧杯'] == {"脱镁叶绿酸溶液（DPA）（已照射40min）": 10} and \
                        st.session_state['实验模拟数据1'].get('红光照射中', False):
                    st.session_state['实验模拟数据1']['烧杯'] = {"脱镁叶绿酸溶液（DPA）（已照射50min）": 10}
                elif st.session_state['实验模拟数据1']['烧杯'] == {"脱镁叶绿酸溶液（DPA）（已照射50min）": 10} and \
                        st.session_state['实验模拟数据1'].get('红光照射中', False):
                    st.session_state['实验模拟数据1']['烧杯'] = {"脱镁叶绿酸溶液（DPA）（已照射60min）": 10}

                if '任务19组' not in st.session_state['实验模拟数据1']:
                    st.session_state['实验模拟数据1']['任务19组'] = {}
                if st.session_state['实验模拟数据1']['分光光度计'] == \
                        {"脱镁叶绿酸溶液（DPA）（已照射10min）": 10, '测量波长': 355.0} and \
                        st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                    st.session_state['实验模拟数据1']['任务19组']['1'] = True
                elif st.session_state['实验模拟数据1']['分光光度计'] == \
                        {"脱镁叶绿酸溶液（DPA）（已照射20min）": 10, '测量波长': 355.0} and \
                        st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                    st.session_state['实验模拟数据1']['任务19组']['2'] = True
                elif st.session_state['实验模拟数据1']['分光光度计'] == \
                        {"脱镁叶绿酸溶液（DPA）（已照射30min）": 10, '测量波长': 355.0} and \
                        st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                    st.session_state['实验模拟数据1']['任务19组']['3'] = True
                elif st.session_state['实验模拟数据1']['分光光度计'] == \
                        {"脱镁叶绿酸溶液（DPA）（已照射40min）": 10, '测量波长': 355.0} and \
                        st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                    st.session_state['实验模拟数据1']['任务19组']['4'] = True
                elif st.session_state['实验模拟数据1']['分光光度计'] == \
                        {"脱镁叶绿酸溶液（DPA）（已照射50min）": 10, '测量波长': 355.0} and \
                        st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                    st.session_state['实验模拟数据1']['任务19组']['5'] = True
                elif st.session_state['实验模拟数据1']['分光光度计'] == \
                        {"脱镁叶绿酸溶液（DPA）（已照射60min）": 10, '测量波长': 355.0} and \
                        st.session_state['实验模拟数据1'].get('吸光度测量状态', False):
                    st.session_state['实验模拟数据1']['任务19组']['6'] = True
                if len(st.session_state['实验模拟数据1']['任务19组'].keys()) == 6:
                    st.markdown(
                        ':green[用红光（630nm）照射 10，20，30，40，50，60min，测定355nm 处吸光度值变化]')
                    st.session_state['实验模拟数据1']['任务19'] = True
                elif st.session_state['实验模拟数据1'].get('任务19', False):
                    st.markdown(
                        ':green[用红光（630nm）照射 10，20，30，40，50，60min，测定355nm 处吸光度值变化]')
                else:
                    def markdown_19():
                        text = ''
                        lyst = ['10', '20', '30', '40', '50', '60']
                        for i in st.session_state['实验模拟数据1']['任务19组']:
                            text += str(lyst[eval(i) - 1]) + '丨'
                        st.markdown(
                            ':red[用红光（630nm）照射 10，20，30，40，50，60min，测定355nm 处吸光度值变化]（已完成：:green[{0}]）'.format(
                                text))

                    markdown_19()
            else:
                st.markdown(
                    ':red[用红光（630nm）照射 10，20，30，40，50，60min，测定355nm 处吸光度值变化]')

        with c1:
            if st.session_state['实验模拟数据1'].get('手中') is not None:
                st.markdown('手中有:red[' + str(st.session_state['实验模拟数据1']['手中'][1]) + ']的:red[' +
                            st.session_state['实验模拟数据1']['手中'][0] + ']')

    def exp2(self):
        self.material = ['水', '水杨酸', '醋酸酐', '浓硫酸', '冰水', '饱和NaHCO3溶液', '浓盐酸']
        self.instrument = ['锥形瓶1', '锥形瓶2', '水浴锅', '抽滤瓶', '烧杯', '干燥箱', '熔点仪', '控制时间']
        if st.session_state.get('实验模拟数据2', None) is None:
            st.session_state['实验模拟数据2'] = {}
            st.session_state['实验模拟数据2']['按钮'] = {}
            st.session_state['实验模拟数据2']['打开中'] = '水'
        dt = st.session_state['实验模拟数据2']
        for i in self.instrument:
            if i not in dt:
                dt[i] = {}
        c1 = st.container()
        st.header('药品')
        col_args_1 = st.columns(4)
        for i in range(len(self.material)):
            row_num = i % 4
            with col_args_1[row_num]:
                dt['按钮'][self.material[i]] = st.button(self.material[i], use_container_width=True)

        st.header('仪器')
        col_args_2 = st.columns(4)
        for i in range(len(self.instrument)):
            row_num = i % 4
            with col_args_2[row_num]:
                dt['按钮'][self.instrument[i]] = st.button(self.instrument[i], use_container_width=True)

        st.header('操作')
        col_args_3 = st.columns(4)
        for i in dt['按钮']:
            if dt['按钮'][i]:
                dt['打开中'] = i
        target = dt['打开中']
        if target in self.material:
            with col_args_3[0]:
                amount = st.number_input('提取量（ml或g）', step=50.0)
            with col_args_3[3]:
                if st.button('确认提取', use_container_width=True):
                    dt['手中'] = [target, amount]


        elif target == '锥形瓶1':
            with col_args_3[0]:
                if st.button('放入物质', use_container_width=True) and dt.get('手中') is not None:
                    dt[target][dt['手中'][0]] = dt[target].get(dt['手中'][0], 0) + dt['手中'][1]
                    dt['手中'] = None
                if st.button('滴入物质', use_container_width=True) and dt.get('手中') is not None:
                    name = dt['手中'][0] + '（滴）'
                    dt[target][name] = dt[target].get(name, 0) + 1
                    del name
                if st.button('冰水浴', use_container_width=True):
                    dt[target]['冰水浴'] = True
            with col_args_3[1]:
                if st.button('倒入物质', use_container_width=True) and dt['手中'] == ['烧杯', 1]:
                    for i in dt['烧杯']:
                        dt[target][i] = dt[target].get(i, 0) + dt['烧杯'][i]
                    dt['手中'] = None
                if st.button('慢慢滴入（1ml）', use_container_width=True) and dt.get('手中') is not None:
                    name = dt['手中'][0] + '（滴）'
                    dt[target][name] = dt[target].get(name, 0) + 20
                    del name
                if st.button('搅拌', use_container_width=True):
                    dt[target]['搅拌'] = True
            with col_args_3[2]:
                if st.button('拿起仪器', use_container_width=True):
                    dt['手中'] = ['锥形瓶1', 1]
                if st.button('摇荡', use_container_width=True):
                    dt[target]['摇荡'] = True
            with col_args_3[3]:
                if st.button('倒出物质', use_container_width=True):
                    dt[target] = {}
                if st.button('等待', use_container_width=True):
                    dt[target]['等待'] = True


        elif target == '锥形瓶2':
            with col_args_3[0]:
                if st.button('放入物质', use_container_width=True) and dt.get('手中') is not None:
                    dt[target][dt['手中'][0]] = dt[target].get(dt['手中'][0], 0) + dt['手中'][1]
                    dt['手中'] = None
                if st.button('滴入物质', use_container_width=True) and dt.get('手中') is not None:
                    name = dt['手中'][0] + '（滴）'
                    dt[target][name] = dt[target].get(name, 0) + 1
                    del name
                if st.button('冰水浴', use_container_width=True):
                    dt[target]['冰水浴'] = True
            with col_args_3[1]:
                if st.button('倒入物质', use_container_width=True) and dt['手中'] == ['烧杯', 1]:
                    for i in dt['烧杯']:
                        dt[target][i] = dt[target].get(i, 0) + dt['烧杯'][i]
                    dt['手中'] = None
                if st.button('慢慢滴入（1ml）', use_container_width=True) and dt.get('手中') is not None:
                    name = dt['手中'][0] + '（滴）'
                    dt[target][name] = dt[target].get(name, 0) + 20
                    del name
                if st.button('搅拌', use_container_width=True):
                    dt[target]['搅拌'] = True
            with col_args_3[2]:
                if st.button('拿起仪器', use_container_width=True):
                    dt['手中'] = ['锥形瓶1', 1]
                if st.button('摇荡', use_container_width=True):
                    dt[target]['摇荡'] = True
            with col_args_3[3]:
                if st.button('倒出物质', use_container_width=True):
                    dt[target] = {}
                if st.button('等待', use_container_width=True):
                    dt[target]['等待'] = True


        elif target == '水浴锅':
            with col_args_3[0]:
                dt[target]['温度'] = st.number_input('设定温度（℃）', step=5.0, value=dt[target].get('温度', 0.0))
            with col_args_3[1]:
                dt[target]['时间'] = st.number_input('设定时间（min）', step=5.0, value=dt[target].get('时间', 0.0))
            with col_args_3[2]:
                if st.button('放入仪器', use_container_width=True) and \
                        dt.get('手中', None) is not None and dt['手中'][0] in self.instrument:
                    dt[target][dt['手中'][0]] = dt[target].get(dt['手中'][0], 0) + dt['手中'][1]
                    dt['手中'] = None
                dt[target]['启动状态'] = st.button('开始加热', use_container_width=True)
            with col_args_3[3]:
                if st.button('拿出仪器', use_container_width=True):
                    def clearLyst():
                        lyst = []
                        for i in dt[target]:
                            if i not in ['温度', '时间', '启动状态']:
                                lyst.append(i)
                        return lyst

                    for i in clearLyst():
                        del dt[target][i]


        elif target == '抽滤瓶':
            with col_args_3[0]:
                if st.button('放入仪器', use_container_width=True) and \
                        dt.get('手中', None) is not None and dt['手中'][0] in self.instrument:
                    dt[target][dt['手中'][0]] = dt[target].get(dt['手中'][0], 0) + dt['手中'][1]
                    dt['手中'] = None
                if st.button('初始化', use_container_width=True):
                    dt[target] = {}
            with col_args_3[1]:
                dt[target]['抽滤'] = st.button('抽滤', use_container_width=True)
                if '洗涤' in dt[target]:
                    del dt[target]['洗涤']
                if st.button('洗涤（用手中物）', use_container_width=True) and \
                        dt.get('手中', None) is not None and dt['手中'][0] in self.material:
                    dt[target]['洗涤'] = dt['手中'][0]
            with col_args_3[2]:
                if st.button('提滤液', use_container_width=True) and '滤液' in dt[target]:
                    for i in dt[target]['滤液']:
                        dt['手中'] = [i, dt[target]['滤液'][i]]
            with col_args_3[3]:
                if st.button('提滤渣', use_container_width=True) and '滤渣' in dt[target]:
                    for i in dt[target]['滤渣']:
                        dt['手中'] = [i, dt[target]['滤渣'][i]]

        condition = st.container()

        if '任务' not in dt:
            dt['任务'] = {}
        task = dt['任务']
        col_args_4 = st.columns([8, 2])
        task_num = 10

        def get_accomplish_num(num):
            for i in range(num):
                if task.get('任务' + str(i + 1), False) is False:
                    return i
            return num

        with st.expander('制备', expanded=True):
            if dt['锥形瓶1'] == {'水杨酸': 2.0, '醋酸酐': 5.0, '浓硫酸（滴）': 5, '摇荡': True}:
                st.markdown(
                    ':green[在干燥的锥形瓶（锥形瓶1）中放入称量好的水杨酸 (2g/0.045mol)、醋酸酐(5ml/5.4g/0.053mol)，滴入 5 滴浓硫酸，轻轻摇荡锥形瓶使溶解]')
                task['任务1'] = True
                dt['锥形瓶1'] = {'水杨酸溶液': 7.0}
            elif task.get('任务1', False):
                st.markdown(
                    ':green[在干燥的锥形瓶（锥形瓶1）中放入称量好的水杨酸 (2g/0.045mol)、醋酸酐(5ml/5.4g/0.053mol)，滴入 5 滴浓硫酸，轻轻摇荡锥形瓶使溶解]')
            else:
                st.markdown(
                    ':red[在干燥的锥形瓶（锥形瓶1）中放入称量好的水杨酸 (2g/0.045mol)、醋酸酐(5ml/5.4g/0.053mol)，滴入 5 滴浓硫酸，轻轻摇荡锥形瓶使溶解]')

            if task.get('任务1', False) and 70 <= dt['水浴锅'].get('温度', 25) <= 80 and \
                    dt['水浴锅'].get('时间') == 15 and \
                    '锥形瓶1' in dt['水浴锅'] and dt['水浴锅'].get('启动状态', False):
                st.markdown(
                    ':green[在70~80℃水浴中加热约15min]')
                task['任务2'] = True
                dt['锥形瓶1'] = {'水杨酸溶液（热）': 7.0}
            elif task.get('任务2', False):
                st.markdown(
                    ':green[在70~80℃水浴中加热约15min]')
            else:
                st.markdown(
                    ':red[在70~80℃水浴中加热约15min]')

            if task.get('任务2', False) and '锥形瓶1' not in dt['水浴锅']:
                st.markdown(
                    ':green[从水浴中拿出锥形瓶]')
                task['任务3'] = True
            elif task.get('任务3', False):
                st.markdown(
                    ':green[从水浴中拿出锥形瓶]')
            else:
                st.markdown(
                    ':red[从水浴中拿出锥形瓶]')

            if task.get('任务3', False) and dt['锥形瓶1'] == {'水杨酸溶液（热）': 7.0, '等待': True}:
                dt['锥形瓶1'] = {'水杨酸溶液（温）': 7.0}
                st.markdown(
                    ':green[等待锥形瓶内容物至温热]')
                task['任务4'] = True
            elif task.get('任务4', False):
                st.markdown(
                    ':green[等待锥形瓶内容物至温热]')
            else:
                st.markdown(
                    ':red[等待锥形瓶内容物至温热]')

            if task.get('任务4', False) and \
                    dt['锥形瓶1'].get('水杨酸溶液（温）', None) == 7.0 and \
                    60 <= dt['锥形瓶1'].get('冰水（滴）', 0) <= 100:
                dt['锥形瓶1'] = {'水杨酸溶液（热）': 7.0}
                st.markdown(
                    ':green[慢慢滴入 3~5mL冰水，此时反应放热，甚至沸腾]')
                task['任务5'] = True
            elif task.get('任务5', False):
                st.markdown(
                    ':green[慢慢滴入 3~5mL冰水，此时反应放热，甚至沸腾]')
            else:
                st.markdown(
                    ':red[慢慢滴入 3~5mL冰水，此时反应放热，甚至沸腾]')

            if task.get('任务5', False) and \
                    dt['锥形瓶1'] == {'水杨酸溶液（温）': 7.0, '水': 40, '冰水浴': True, '搅拌': True}:
                dt['锥形瓶1'] = {'液相A': 1, '结晶A': 1}
                st.markdown(
                    ':green[等待反应平稳后，再加入40mL水，用冰水浴冷却，并用玻棒不停搅拌，使结晶完全析出]')
                task['任务6'] = True
            elif task.get('任务6', False):
                st.markdown(
                    ':green[等待反应平稳后，再加入40mL水，用冰水浴冷却，并用玻棒不停搅拌，使结晶完全析出]')
            else:
                st.markdown(
                    ':red[等待反应平稳后，再加入40mL水，用冰水浴冷却，并用玻棒不停搅拌，使结晶完全析出]')

            if task.get('任务6', False) and \
                    dt['抽滤瓶'] == {'锥形瓶1': 1, '抽滤': True} and \
                    dt['锥形瓶1'] == {'液相A': 1, '结晶A': 1}:
                dt['抽滤瓶']['滤液'] = {'液相A': 1}
                dt['抽滤瓶']['滤渣'] = {'阿斯匹林（未洗涤）': 1}
                st.markdown(
                    ':green[抽滤]')
                task['任务7'] = True
            elif task.get('任务7', False):
                st.markdown(
                    ':green[抽滤]')
            else:
                st.markdown(
                    ':red[抽滤]')

            if task.get('任务7', False) and \
                    dt['抽滤瓶'] == {'锥形瓶1': 1, '抽滤': False, '滤液': {'液相A': 1}, '滤渣': {'阿斯匹林（未洗涤）': 1},
                                     '洗涤': '冰水'} and \
                    dt['锥形瓶1'] == {'液相A': 1, '结晶A': 1}:
                dt['抽滤瓶']['滤渣'] = {'阿斯匹林（已洗涤一次）': 1}
                st.markdown(
                    ':red[用少量冰水洗涤两次]')
            elif task.get('任务7', False) and \
                    dt['抽滤瓶'] == {'锥形瓶1': 1, '抽滤': False, '滤液': {'液相A': 1},
                                     '滤渣': {'阿斯匹林（已洗涤一次）': 1},
                                     '洗涤': '冰水'} and \
                    dt['锥形瓶1'] == {'液相A': 1, '结晶A': 1}:
                dt['抽滤瓶']['滤渣'] = {'阿斯匹林（粗产物）': 1}
                st.markdown(
                    ':green[用少量冰水洗涤两次]')
                task['任务8'] = True
            elif task.get('任务8', False):
                st.markdown(
                    ':green[用少量冰水洗涤两次]')
            else:
                st.markdown(
                    ':red[用少量冰水洗涤两次]')

            if task.get('任务8', False) and \
                    dt['锥形瓶2'] == {'阿斯匹林（粗产物）': 1, '饱和NaHCO3溶液': 25, '搅拌': True}:
                dt['锥形瓶2'] = {'液相B': 1, '固相B': 1}
                st.markdown(
                    ':green[将阿斯匹林的粗产物移至另一锥形瓶中，加入 25mL饱和NaHCO3溶液，搅拌，直至无CO2气泡产生]')
                task['任务9'] = True
            elif task.get('任务9', False):
                st.markdown(
                    ':green[将阿斯匹林的粗产物移至另一锥形瓶中，加入 25mL饱和NaHCO3溶液，搅拌，直至无CO2气泡产生]')
            else:
                st.markdown(
                    ':red[将阿斯匹林的粗产物移至另一锥形瓶中，加入 25mL饱和NaHCO3溶液，搅拌，直至无CO2气泡产生]')

        with c1:
            if dt.get('手中') is not None:
                st.markdown('手中有:red[' + str(dt['手中'][1]) + ']的:red[' + dt['手中'][0] + ']')

        with condition:
            if target in self.instrument:
                st.header('仪器状态')
                st.write(dt[target])

        accomplish_rate = "{:.2%}".format(get_accomplish_num(task_num) / task_num)
        with col_args_4[0]:
            st.header('任务清单')
        with col_args_4[1]:
            st.write('--')
            st.write(':green[完成度：{0}]'.format(accomplish_rate))

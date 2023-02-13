import streamlit as st
from PIL import Image
import time
import os


def studypg(expID, uID, uName):
    colLeft, colRight = st.columns([7, 3])
    with colRight:
        if st.button('学习开始'):
            st.session_state['sTime'] = time.time()
        if st.button('学习结束'):
            st.session_state['eTime'] = time.time()
            allTime =int(st.session_state.eTime - st.session_state.sTime)
            st.subheader('您学习了')
            st.subheader(str(allTime) + 's')

    if expID == 0:
        with colLeft:
            st.header('实验目的')
            st.text('1.  了解蚕砂中脱镁叶绿酸提取分离原理和方法；')
            st.text('2.  了解脱镁叶绿酸的结构表征和含量分析测定方法；')
            st.text('3.  了解脱镁叶绿酸的荧光性质。')
            st.header('实验原理')
            st.write(
                '脱镁叶绿酸(Pheophorbide)是由叶绿素分子脱去镁离子后进一步水解而形成的化合物，具有显著的抗炎、抗肿瘤、保护胃肠粘膜等药理作用。\n中药蚕砂在乙醇、丙酮等有机溶剂的萃取下获得叶绿素粗品，然后在酸性条件下脱去植醇长链和金属离子，得到主要产物脱镁叶绿酸 a，再对产物进行盐酸乙醚转溶、真空干燥得到纯度很高的脱镁叶绿酸。')
            if  os.path.exists('pg/studydata/exp0/img0.png'):
                print ('yes')
            st.image('pg/studydata/exp0/img0.png')
            st.write(
                '脱镁叶绿酸具有特殊的荧光特性，即在一定波长光激发下可发射特定波长的荧光，可用于鉴别和含量分析。其在一定波长光激发下可产生单线态氧，破坏肿瘤细胞，因而是一种良好的光敏剂，可用于光动力治疗。')
            st.header('实验步骤')
            st.write(
                '<1>浸提：取中药材蚕砂 100g 于 1000ml 圆底烧瓶中，加 200ml 水软化 2h；加入 300ml 丙酮，在 70℃恒温水浴中回流浸提 60min，抽滤，得浸提液 A。滤渣倒回圆底烧瓶中，再加入 100ml 蒸馏水，200ml 丙酮，在 70℃恒温水浴中回流浸提 60min， 抽滤，得浸提液 B。合并浸提液；')
            st.write(
                '<2>萃取：用旋转蒸发仪在 50℃下将浸提液浓缩至 50ml，移至 500ml 分液漏斗 中，依次加入 150 ml 乙醚、30%HCl 100ml，振荡 5min，进行转溶萃取，静置至完全分层。将下层水溶液放出置于烧杯，放入冰水浴中，慢慢滴入 NaOH 的饱和溶液，同时进行搅拌，直至pH值在 2.5-3之间，3000rpm 离心 10min，所得沉淀即为脱镁叶绿酸。')
            st.write('<3>真空干燥：将沉淀在 60℃下真空干燥箱中烘干 2h，称重。')
            st.write(
                '<4>含量测定：准确称取 10mg 样品，溶于 100 ml DMF 溶液中，波长 667nm测定吸光值。含量计算方程 Y(吸光值)=0.0275X(mg/L)+0.0025')
            st.write(
                '<5>紫外和荧光光谱测定:对产物进行紫外荧光测试：取 10mg 脱镁叶绿酸 a 提取物粉末溶于 100mlDMF 溶液中，在 300nm—800nm 波长范围内进行紫外和荧光扫描。确定最大激发波长和发射波长。')
            st.write('<6>单线态氧的含量测定')
            st.write(
                '（1）标准曲线制备：配制一系列浓度（1.25×10-5、2.5×10-5、5×10-5、1×10-4、 2×10-4、4×10-4mol/L）的 9，10-二苯蒽（DPA）的乙醇溶液，于 355 nm 处测定吸 光度值，以吸光值对应浓度绘制 DPA 的标准曲线。')
            st.write(
                '（2）样品测定：量取 5 mL 2×10-5 DPA 溶液，加入 5 mL 2×10-4 mol/L 的脱镁叶绿酸溶液混合均匀后，用红光（630nm）照射 10，20，30，40，50，60min，测定355nm 处吸光度值变化，以变化值为纵坐标，照射时间为横坐标，绘图。')
            st.header('实验结果与讨论')
            st.text('1.  记录实验条件、现象、各试剂用量及产品的重量和含量。')
            st.text('2.  脱镁叶绿酸的紫外和荧光光谱。')
            st.text('3.  单线态氧的变化。')
            st.header('思考题')
            st.text('1. 试分析哪些因素影响产品的产率和纯度，怎样控制？')
            st.text('2.  脱镁叶绿酸具有什么光谱特征？')
            st.text('3.  单线态氧的产率与哪些因素有关？')

    elif expID == 1:
        st.header('实验目的')

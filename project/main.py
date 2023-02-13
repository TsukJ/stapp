import streamlit as st
import pandas as pd
from pg import exampg
from pg import studypg
from pg import reportpg
from multipage import MultiPage

st.set_page_config(page_title='制药工程专业实验', layout='wide')
expList = [
    '实验一	蚕砂中脱镁叶绿酸的提取分离和荧光特性',
    '实验二 乙酰水杨酸的制备及表征',
    '实验三  氯霉素眼药水的高效液相色谱分析法',
    '实验四  茶多酚的提取与精制工艺实验',
    '实验五  胆红素的提取及含量测定',
    '实验四 片剂的制备及质量监控',
    '实验六  白芍中芍药苷的提取分离',
    '实验七  散剂的制备及质量监控',
    '实验八 气相色谱法测定合成冰片的含量',
    '实验九  颗粒剂的制备及质量监控',
    '实验十 硝苯地平的合成',
    '实验十一  软膏剂的制备及质量监控',
    '实验十二  微囊的制备及质量监控',
]
expId = pd.Series(index=expList, data=range(0, 13))
app = MultiPage()
app.add_page('学习', studypg.studypg)
app.add_page('测试', exampg.exampg)
app.add_page('数据处理', reportpg.reportpg)
for i in expList:
    app.add_experiment(i, expId[i])
uID = st.sidebar.text_input('请输入学号', value='200100010001')
uName = st.sidebar.text_input('请输入姓名', value='张三')
if __name__ == '__main__':
    app.runpg(uID, uName)


from pg import studypg, exampg, reportpg, homepg, simulatepg
from pg.studydata import study_develop, exam_develop

exp_list = [
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
page_list = {'主页': homepg, '学习': studypg, '测试': exampg, '实验模拟': simulatepg, '数据处理': reportpg}
page_list_dev = {'开发：学习': study_develop, '开发：测试': exam_develop}
exp_file_list = ['exp0']

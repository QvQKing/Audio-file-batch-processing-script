import os
import matplotlib.pyplot as plt
plt.style.use('seaborn')
type=['Snoring-kaggle','No-Snoring-kaggle','Snoring-ESC50','No-Snoring-ESC50']
num=[500,500,40,40]
plt.figure()
x_ticks = range(len(type))
# plt.bar(x_ticks, num, color=['b','r','g','y','c','m','y','k','c','g','b'])
plt.bar(x_ticks, num,color=['cornflowerblue','cornflowerblue','c','c'])
# 修改x刻度
plt.xticks(x_ticks, type)
# 添加标题
plt.title("Snoring-Dataset")
# 添加网格显示
plt.grid(linestyle="--", alpha=0.7)
# plt.legend(loc='upper center', fontsize=15, ncol=2)
# 4、显示图像
plt.savefig('数量柱状图.png')
plt.show()
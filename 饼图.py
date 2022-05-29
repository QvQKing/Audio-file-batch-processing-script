import os
import matplotlib.pyplot as plt
plt.style.use('seaborn')
type=['Snoring-kaggle','No-Snoring-kaggle','Snoring-ESC50','No-Snoring-ESC50']
num=[500,500,40,40]
plt.figure()
# 2、创建画布


# 3、绘制饼图
plt.pie(num, labels=type, colors=['dodgerblue','red','springgreen','y'], autopct="%1.2f%%")

# 显示图例
plt.legend()

plt.axis('equal')
plt.savefig('饼图.png')
# 4、显示图像
plt.show()

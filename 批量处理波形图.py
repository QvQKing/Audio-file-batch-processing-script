import pyworld
import librosa
import librosa.display
from IPython.display import Audio
import numpy as np
from matplotlib import pyplot as plt
import math
import os
import matplotlib.pyplot as plt
# 图片风格
# plt.style.use('seaborn')
# 存放文件夹路径
path=r'D:\snoring-dataset\Snoring Dataset\音频数据\0/'
# 获取文件列表
waveforms=os.listdir(path)
pngpath=r'D:\snoring-dataset\Snoring Dataset\音频数据\波形图\no/'
names=[]

count=0
# 批量处理wav文件
for i,file in enumerate(waveforms):
    file_name=os.path.splitext(file)[0]
    file_type=os.path.splitext(file)[1]
    filename=path+file
    if count%10==0:
        print(count)
    # names.append(filename)
    # 生成波形图
    x, fs = librosa.load(filename, sr=16000)  # librosa load输出的waveform 是 float32
    x = x.astype(np.double)  # 格式转换
    fftlen = pyworld.get_cheaptrick_fft_size(fs)  # 自动计算适合的fftlen
    # plt.figure()
    # plt.figure(figsize=(26, 13), dpi=32)
    plt.figure(figsize=(16, 11), dpi=50)
    librosa.display.waveplot(x, sr=fs,)
    # 保存生成的波形图
    plt.savefig(pngpath+file_name+'.png')
    # plt.show()
    count+=1
# print(names)